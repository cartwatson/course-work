/**
 * @file hw52.cpp
 * @author Carter Watson
 * @date 2023-12-01
 * @brief transpose an image using a variety of methods
 * @todo
 * [X] read the image file
 * [X] write a CPU based serial transpose
 * [ ] write a kernel function to perform a matrix transposition of the input matrix using the GPU global memory
 * [ ] write a kernel function to perform a matrix transposition of the input matrix making use of tiling (using the GPU shared memory)
 * [X] write a function to validate the result of your transposition
 *       - (i.e., on the host CPU, comparing to a CPU based serial transpose) 
 * [X] write code to compute the bandwidth performance of both kernels (1 and 2), report and comment the result you obtained
 * [X] save the transposed matrix to a binary file
 * 
 * @note This program is only meant to be run on University of Utah CHPC machines
 *   Helper info to compile/run on CHPC
 *     0. ssh u1234567@notchpeak.chpc.utah.edu
 *     1. salloc -n 1 -N 1 -t 0:15:00 -p notchpeak-shared-short -A notchpeak-shared-short --gres=gpu
 *     2. module load nvhpc
 *     3. nvcc -o hw52 hw52.cu
 *     4. srun ./hw52
 * 
 * @note Notable Sources
 *   - https://developer.nvidia.com/blog/efficient-matrix-transpose-cuda-cc/
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <chrono>
#include <cuda_runtime.h>


/**
 * @brief validate image processing
 * 
 * checks two vectors of image data pixel by pixel to verify they are identical
 * 
 * @param validImage (std::vector<unsigned char>&) - vector of valid image data
 * @param checkImage (std::vector<unsigned char>&) - vector of image data to check
 * @param size (int) - size of image
 * 
 * @return bool - true if image processing is valid, otherwise false
 */
bool validateImageProcessing(std::vector<unsigned char>& validImage, std::vector<unsigned char>& checkImage, int size) {
    bool valid = true;
    for (int i = 0; i < size; i++) {
        if (validImage[i] != checkImage[i]) {
            valid = false;
        }
    }
    return valid;
}

/**
 * @brief convert regular image to rotated image using the cpu 
 * 
 * @param inputImage (std::vector<unsigned char>&) - vector of unmodified image data
 * @param outputImage (std::vector<unsigned char>&) - vector of serially modified image data
 * @param numPixels (int) - number of pixels in image
 * @param width (int) - width of image
 * @param height (int) - height of image
 * @param channels (int) - number of channels in image
 * 
 * @return void
 */
void serialTranposeImage(std::vector<unsigned char>& inputImage, std::vector<unsigned char>& outputImage, int numPixels, int width, int height, int channels) {
    // this is whats happening at a basic level
    // for x = 0 to N:
    //    for y = 0 to M:
    //      a_t[x][y] = a[y][x]
    for (int x = 0; x < width; x++) {
        for (int y = 0; y < height; y++) { 
            for (int c = 0; c < channels; c++) {
                outputImage[x * height * channels + y * channels + c] = inputImage[y * width * channels + x * channels + c];
            }
        }
    }
}

/**
 * @brief convert regular image to rotated image using the gpu global memory
 * 
 * @param inputImage (unsigned char *) - pointer to unmodified image data
 * @param outputImage (unsigned char *) - pointer to modified image data
 * @param width (int) - width of image
 * @param height (int) - height of image
 * 
 * @return void
*/
__global__
void globalTransposeImage(unsigned char * inputImage, unsigned char * outputImage, int width, int height) {
    // Calculate the global thread index
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    int col = blockIdx.y * blockDim.y + threadIdx.y;

    // Check if the thread is within the image dimensions
    if (row < height && col < width) {
        // Calculate the linear indices for accessing input and output images
        int inputIndex = row * width + col;
        int outputIndex = col * height + row;

        // Perform the pixel transposition by copying from input to output
        outputImage[outputIndex] = inputImage[inputIndex];
    }
}

/**
 * @brief convert regular image to rotated image using the gpu global memory
 * 
 * @param inputImage (std::vector<unsigned char>) unprocessed image
 * @param outputImage (std::vector<unsigned char>) allocated vector for converted image
 * @param blocksizeX (int)
 * @param blocksizeY (int)
 * @param size (int)
 * @param width (int)
 * @param height (int)
 *
 * @return void
*/
void globalCudaBlock(std::vector<unsigned char>& inputImage, std::vector<unsigned char>& outputImage, int blocksizeX, int blocksizeY, int width, int height, int size) {
    // cuda init/mem allocation/mem sharing
    unsigned char *d_inputImage, *d_outputImage;
    cudaMalloc((void **)&d_inputImage, size);
    cudaMalloc((void **)&d_outputImage, size);
    cudaMemcpy(d_inputImage, inputImage.data(), size, cudaMemcpyHostToDevice);

    // define block and grid sizes
    dim3 blockSize(blocksizeX, blocksizeY, 1);
    dim3 gridSize(ceil(width / blockSize.x), ceil(height / blockSize.y), 1);

    // start timer for bandwidth
    std::chrono::_V2::system_clock::time_point start = std::chrono::high_resolution_clock::now();

    // Convert the image to grayscale on device
    globalTransposeImage<<<gridSize, blockSize>>>(d_inputImage, d_outputImage, width, height);

    // sync up cuda and data
    cudaDeviceSynchronize();
    cudaMemcpy(outputImage.data(), d_outputImage, size, cudaMemcpyDeviceToHost);

    // stop timer and calculate bandwidth
    std::chrono::_V2::system_clock::time_point stop = std::chrono::high_resolution_clock::now();
    std::chrono::microseconds duration = std::chrono::duration_cast<std::chrono::microseconds>(start - stop);
    double bandwidth = size / duration.count() / 1e6;
    std::cout << "Global Memory Bandwidth: " << bandwidth << " bytes/second" << std::endl;

    // clean up
    cudaFree(d_inputImage);
    cudaFree(d_outputImage);
}

/**
 * @brief convert regular image to rotated image using the gpu shared memory
 * 
 * @param inputImage (unsigned char *) - pointer to unmodified image data
 * @param outputImage (unsigned char *) - pointer to modified image data
 * @param width (int) - width of image
 * @param height (int) - height of image
 * 
 * @return void
*/
// Define tile width as compile time const for cuda compiler
# define TILE_WIDTH 16
__global__
void sharedTransposeImage(unsigned char * input, unsigned char * output, int width, int height) {
    // Define shared memory
    __shared__ unsigned char tile[TILE_WIDTH][TILE_WIDTH + 1]; // +1 to avoid shared memory bank conflict

    // Calculate global row and column indices
    int xIndex = blockIdx.x * TILE_WIDTH + threadIdx.x;
    int yIndex = blockIdx.y * TILE_WIDTH + threadIdx.y;
    int index = yIndex * width + xIndex;

    // Load data into shared memory if within matrix bounds
    if (xIndex < width && yIndex < height) {
        tile[threadIdx.y][threadIdx.x] = input[index];
    }

    // Synchronize threads to ensure all data is loaded into shared memory
    __syncthreads();

    // Transpose block offset
    xIndex = blockIdx.y * TILE_WIDTH + threadIdx.x;
    yIndex = blockIdx.x * TILE_WIDTH + threadIdx.y;
    index = yIndex * height + xIndex; // Transposed index

    // Write transposed data to the output if within matrix bounds
    if (xIndex < height && yIndex < width) {
        output[index] = tile[threadIdx.x][threadIdx.y];
    }
}


/**
 * @brief convert regular image to rotated image using the gpu shared memory
 * 
 * @param inputImage (std::vector<unsigned char>) unprocessed image
 * @param outputImage (std::vector<unsigned char>) allocated vector for converted image
 * @param blocksizeX (int)
 * @param blocksizeY (int)
 * @param size (int)
 * @param width (int)
 * @param height (int)
 *
 * @return void
*/
void sharedCudaBlock(std::vector<unsigned char>& inputImage, std::vector<unsigned char>& outputImage, int blocksizeX, int blocksizeY, int width, int height, int size) {
    // cuda init/mem allocation/mem sharing
    unsigned char *d_inputImage, *d_outputImage;
    cudaMalloc((void **)&d_inputImage, size);
    cudaMalloc((void **)&d_outputImage, size);
    cudaMemcpy(d_inputImage, inputImage.data(), size, cudaMemcpyHostToDevice);

    // define block and grid sizes
    dim3 blockSize(blocksizeX, blocksizeY, 1);
    dim3 gridSize(ceil(width / blockSize.x), ceil(height / blockSize.y), 1);

    // start timer for bandwidth
    std::chrono::_V2::system_clock::time_point start = std::chrono::high_resolution_clock::now();

    // kernel function to perform a matrix transposition of the input matrix using tiling/GPU shared memory
    sharedTransposeImage<<<gridSize, blockSize>>>(d_inputImage, d_outputImage, width, height);

    // stop timer and calculate bandwidth
    std::chrono::_V2::system_clock::time_point stop = std::chrono::high_resolution_clock::now();
    std::chrono::microseconds duration = std::chrono::duration_cast<std::chrono::microseconds>(start - stop);
    double bandwidth = size / duration.count() / 1e6;
    std::cout << "Shared Memory Bandwidth: " << bandwidth << " bytes/second" << std::endl;

    // Copy over data
    cudaMemcpy(outputImage.data(), d_outputImage, size, cudaMemcpyDeviceToHost);

    // Free device memory
    cudaFree(d_inputImage);
    cudaFree(d_outputImage);
}


/**
* @brief 
* 
* @note the following values are hardcoded
*   - input file name = gc_conv_1024x1024.raw
*   - output file name = gc.raw
*   - image width = 1024
*   - image height = 1024
*   - number of channels = 3
* 
* @return error_code (int) 
* @retval 0 Success
* @retval 1 Invalid number of arguments
*/
int main(int argc, char *argv[]) {
    // sometimes hardcoding variables is okay
    std::string INPUT_FILE = "gc_1024x1024.raw";
    std::string OUTPUT_FILE = "gc.raw";
    const int WIDTH = 1024;
    const int HEIGHT = 1024;
    const int CHANNELS = 3;
    const int NUM_PIXELS = WIDTH * HEIGHT;
    const int SIZE = NUM_PIXELS * CHANNELS;

    // Check to see if valid # of params provided
    if (argc != 1) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }

    // init variables for start and final image
    std::vector<unsigned char> h_untouchedImage(SIZE);
    std::vector<unsigned char> h_serialConvImage(SIZE);
    std::vector<unsigned char> h_globalGPUMemoryConvImage(SIZE);
    std::vector<unsigned char> h_sharedGPUMemoryConvImage(SIZE);

    // get image data
    FILE *fp;
    fp = fopen(INPUT_FILE.c_str(), "rb");
    // make sure file exists
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << INPUT_FILE << std::endl;
        return 1;
    }
    // Read in the image file
    fread(&h_untouchedImage[0], sizeof(unsigned char), SIZE, fp);
    fclose(fp);

// ----- SERIAL IMPLEMENTATION -----
    serialTranposeImage(h_untouchedImage, h_serialConvImage, NUM_PIXELS, WIDTH, HEIGHT, CHANNELS);
    
// ----- GLOBAL MEMORY -----
    // kernel function to perform a matrix transposition of the input matrix using GPU global memory
    globalCudaBlock(h_untouchedImage, h_globalGPUMemoryConvImage, 32, 32, WIDTH, HEIGHT, SIZE * sizeof(unsigned char));

// ----- SHARED MEMORY -----
    // kernel function to perform a matrix transposition of the input matrix using tiling/GPU shared memory
    sharedCudaBlock(h_untouchedImage, h_sharedGPUMemoryConvImage, 32, 32, WIDTH, HEIGHT, SIZE * sizeof(unsigned char));

// ----- VALIDATE IMAGE PROCESSING -----
    if (!validateImageProcessing(h_serialConvImage, h_globalGPUMemoryConvImage, SIZE)) {
        std::cout << "ERROR: Global memory image processing failed!" << std::endl;
    }

    if (!validateImageProcessing(h_serialConvImage, h_sharedGPUMemoryConvImage, SIZE)) {
        std::cout << "ERROR: Global memory image processing failed!" << std::endl;
    }

// ----- SAVE IMAGES -----
    fp = fopen(OUTPUT_FILE.c_str(), "wb");
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << OUTPUT_FILE << std::endl;
        return 1;
    }
    fwrite(&h_globalGPUMemoryConvImage[0], sizeof(unsigned char), SIZE, fp);
    fclose(fp);

    
    fp = fopen("gc_global.raw", "wb");
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << "gc_global.raw" << std::endl;
        return 1;
    }
    fwrite(&h_globalGPUMemoryConvImage[0], sizeof(unsigned char), SIZE, fp);
    fclose(fp);

    fp = fopen("gc_shared.raw", "wb");
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << "gc_shared.raw" << std::endl;
        return 1;
    }
    fwrite(&h_sharedGPUMemoryConvImage[0], sizeof(unsigned char), SIZE, fp);
    fclose(fp);
}

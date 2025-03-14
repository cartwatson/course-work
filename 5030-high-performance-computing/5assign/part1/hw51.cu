/**
 * @file hw51.cpp
 * @author Carter Watson
 * @date nov-20-2023
 * @brief CUDA program to convert a color image to gray scale
 * @todo
 * PART 1: CUDA program to convert a color image to gray scale
 * - [X] read the image file
 * - [X] write a kernal function to perform the gray scale conversion using CUDA
 *   - remember to treat the matrices as 1D arrays and use the corresponding linearization of indexes for every memory access you perform
 *   - provide only the program with your comments as your solution. No need to attach input or output files
 * - [X] save the converted image in a binary file named gc.raw
 * 
 * PART 2: GPU Information
 * - Pick a particular GPU (e.g., from the ones available on a CHPC cluster) and report the information
 *   - [X] Max num of threads per SM
 *     - Assume max num of blocks per SM is 8
 * - [ ] choose three different block sizes and explain analytically how the different block sizes should affect the performance of the application made in Part 1
 * - [X] report experimental results using the three different block sizes
 *   - (i.e., run the kernel 200 times to assess the time accurately)
 * 
 * @note This program is only meant to be run on University of Utah CHPC machines
 *   Helper info to compile/run on CHPC
 *     0. ssh to a CHPC machine
 *     1. salloc -n 1 -N 1 -t 0:15:00 -p notchpeak-shared-short -A notchpeak-shared-short --gres=gpu
 *     2. module load nvhpc
 *     3. nvcc -o hw51 hw51.cu
 *     4. srun ./hw51
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <cuda_runtime.h>


/**
 * @brief CUDA function to convert a color image to gray scale
 * 
 * @param grayImage (unsigned char *) processed image
 * @param rgbImage (unsigned char *) unprocessed image
 * @param width (int) width of image
 * @param height (int) height of image
 * @param CHANNELS (int) number of channels per pixel
 * 
 * @note This function is directly from lecture notes
 */
__global__
void RGBToGrayscale(unsigned char * grayImage, unsigned char * rgbImage, int width, int height, int CHANNELS)
{
    int Col = threadIdx.x + blockIdx.x * blockDim.x;
    int Row = threadIdx.y + blockIdx.y * blockDim.y;

    if (Col < width && Row < height) {
        // get 1D coordinate for the grayscale image
        int grayOffset = Row*width + Col;

        // one can think of the RGB image having
        // CHANNEL times columns of the gray scale image
        int rgbOffset = grayOffset*CHANNELS;
        unsigned char r = rgbImage[rgbOffset ]; // red value for pixel
        unsigned char g = rgbImage[rgbOffset + 1]; // green value for pixel
        unsigned char b = rgbImage[rgbOffset + 2]; // blue value for pixel
        
        // perform the rescaling and store it
        // We multiply by floating point constants
        grayImage[grayOffset] = 0.21f*r + 0.71f*g + 0.07f*b;
    }
}


/**
 * @brief 
 * 
 * @param h_rgbImage (std::vector<unsigned char>) unprocessed rgb image
 * @param h_grayImage (std::vector<unsigned char>) allocated gray image, passed by reference 
 * @param blocksizeX (int)
 * @param blocksizeY (int)
 * @param NUM_PIXELS (int)
 * @param WIDTH (int)
 * @param HEIGHT (int)
 * @param CHANNELS (int) num of rgb channels
 *
*/
void cudaBlock(std::vector<unsigned char>& h_rgbImage, std::vector<unsigned char>& h_grayImage, int blocksizeX, int blocksizeY, int NUM_PIXELS, int WIDTH, int HEIGHT, int CHANNELS) {
    // cuda init/mem allocation/mem sharing
    unsigned char *d_rgbImage, *d_grayImage;
    cudaMalloc((void **)&d_rgbImage, NUM_PIXELS * CHANNELS * sizeof(unsigned char));
    cudaMalloc((void **)&d_grayImage, NUM_PIXELS * sizeof(unsigned char));
    cudaMemcpy(d_rgbImage, h_rgbImage.data(), NUM_PIXELS * CHANNELS * sizeof(unsigned char), cudaMemcpyHostToDevice);

    // define block and grid sizes
    dim3 blockSize(blocksizeX, blocksizeY, 1);
    dim3 gridSize(ceil(WIDTH / blockSize.x), ceil(HEIGHT / blockSize.y), 1);

    // Convert the image to grayscale on device
    RGBToGrayscale<<<gridSize, blockSize>>>(d_grayImage, d_rgbImage, WIDTH, HEIGHT, CHANNELS);

    // sync up cuda and data
    cudaDeviceSynchronize();
    cudaMemcpy(h_grayImage.data(), d_grayImage, NUM_PIXELS * sizeof(unsigned char), cudaMemcpyDeviceToHost);

    // clean up
    cudaFree(d_rgbImage);
    cudaFree(d_grayImage);
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
    std::string INPUT_FILE = "gc_conv_1024x1024.raw";
    std::string OUTPUT_FILE = "gc.raw";
    const int WIDTH = 1024;
    const int HEIGHT = 1024;
    const int CHANNELS = 3;
    const int NUM_PIXELS = WIDTH * HEIGHT;

    // Check to see if valid # of params provided
    if (argc != 1) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }
    
    // PART 1
    // init image variables
    std::vector<unsigned char> h_rgbImage(NUM_PIXELS * CHANNELS);
    std::vector<unsigned char> h_grayImage(NUM_PIXELS);

    // get image data
    FILE *fp;
    fp = fopen(INPUT_FILE.c_str(), "rb");
    // make sure file exists
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << INPUT_FILE << std::endl;
        return 1;
    }
    // Read in the image file
    fread(&h_rgbImage[0], sizeof(unsigned char), NUM_PIXELS * CHANNELS, fp);
    fclose(fp);

    // run cuda kernal
    cudaBlock(h_rgbImage, h_grayImage, 16, 16, NUM_PIXELS, WIDTH, HEIGHT, CHANNELS);

    // Save the converted image in a binary file named gc.raw
    fp = fopen(OUTPUT_FILE.c_str(), "wb");
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << OUTPUT_FILE << std::endl;
        return 1;
    }
    fwrite(&h_grayImage[0], sizeof(unsigned char), NUM_PIXELS, fp);
    fclose(fp);


    // PART 2
    // use device query.cu to get info
        // nvcc -o device_query device_query.cu
        // srun ./device_query
    // Tesla T4
        // Max num of threads per SM = 1024

    // Choose three different block sizes and explain analytically how the different block sizes should affect the performance
    /**
     * 8x8
     *   - Pros: 
     *   - Cons:
     * 16x16
     *   - Pros: 
     *   - Cons:
     * 32x32
     *   - Pros: 
     *   - Cons:
    */
    // Report experimental results using the three different block sizes
    std::vector<int> blockSizes = {8, 16, 32};
    float totalTime, elapsedTime;
    cudaEvent_t start, stop;

    // create CUDA events
    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    for (int i = 0; i < blockSizes.size(); i++) {
        totalTime = 0.0f;
        for (int j = 0; j < 200; j++) {
            cudaEventRecord(start, 0);

            // run CUDA kernel
            cudaBlock(h_rgbImage, h_grayImage, blockSizes[i], blockSizes[i], NUM_PIXELS, WIDTH, HEIGHT, CHANNELS);

            cudaEventRecord(stop, 0);
            cudaEventSynchronize(stop);
            cudaEventElapsedTime(&elapsedTime, start, stop);

            totalTime += elapsedTime;
        }
        std::cout << "Average time for block size " << blockSizes[i] << ": " << totalTime / 200.0f << " ms" << std::endl;
    }

    // Destroy CUDA events
    cudaEventDestroy(start);
    cudaEventDestroy(stop);
    
    return 0;
}

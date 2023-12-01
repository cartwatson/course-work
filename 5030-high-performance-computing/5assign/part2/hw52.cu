/**
 * @file hw52.cpp
 * @author Carter Watson
 * @date 2023-12-01
 * @brief 
 * @todo
 * [X] read the image file
 * [X] write a CPU based serial transpose
 * [ ] write a kernel function to perform a matrix transposition of the input matrix using the GPU global memory
 * [ ] write a kernel function to perform a matrix transposition of the input matrix making use of tiling (using the GPU shared memory)
 * [X] write a function to validate the result of your transposition
 *       - (i.e., on the host CPU, comparing to a CPU based serial transpose) 
 * [ ] write code to compute the bandwidth performance of both kernels (1 and 2), report and comment the result you obtained
 * [X] save the transposed matrix to a binary file
 * 
 * @note This program is only meant to be run on University of Utah CHPC machines
 *   Helper info to compile/run on CHPC
 *     0. ssh to a CHPC machine
 *     1. salloc -n 1 -N 1 -t 0:15:00 -p notchpeak-shared-short -A notchpeak-shared-short --gres=gpu
 *     2. module load nvhpc
 *     3. nvcc -o hw52 hw52.cu
 *     4. srun ./hw52
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iomanip>
// #include <cuda_runtime.h>


/**
 * @brief validate image processing
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
            std::cout << "ERROR: Image processing failed at index " << i << std::endl;
            std::cout << "Expected: " << std::setw(3) << (int)validImage[i] << " Actual: " << std::setw(3) << (int)checkImage[i] << std::endl;
            valid = false;
        }
    }
    return valid;
}

/**
 * @brief convert regular image to rotated image
 * 
 * @param h_untouchedImage (std::vector<unsigned char>&) - vector of unmodified image data
 * @param h_serialConvImage (std::vector<unsigned char>&) - vector of serially modified image data
 * @param numPixels (int) - number of pixels in image
 * @param width (int) - width of image
 * @param height (int) - height of image
 * @param channels (int) - number of channels in image
 * 
 * @return void
 */
void serial_tranpose(std::vector<unsigned char>& h_untouchedImage, std::vector<unsigned char>& h_serialConvImage, int numPixels, int width, int height, int channels) {
    // this is whats happening at a basic level
    // for x = 0 to N:
    //    for y = 0 to M:
    //      a_t[x][y] = a[y][x]
    for (int x = 0; x < width; x++) {
        for (int y = 0; y < height; y++) { 
            for (int c = 0; c < channels; c++) {
                h_serialConvImage[x * height * channels + y * channels + c] = h_untouchedImage[y * width * channels + x * channels + c];
            }
        }
    }
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

    // Check to see if valid # of params provided
    if (argc != 1) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }

    // init variables for start and final image
    std::vector<unsigned char> h_untouchedImage(NUM_PIXELS * CHANNELS);
    std::vector<unsigned char> h_serialConvImage(NUM_PIXELS * CHANNELS);
    std::vector<unsigned char> h_convImage(NUM_PIXELS * CHANNELS);

    // get image data
    FILE *fp;
    fp = fopen(INPUT_FILE.c_str(), "rb");
    // make sure file exists
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << INPUT_FILE << std::endl;
        return 1;
    }
    // Read in the image file
    fread(&h_untouchedImage[0], sizeof(unsigned char), NUM_PIXELS * CHANNELS, fp);
    fclose(fp);

    serial_tranpose(h_untouchedImage, h_serialConvImage, NUM_PIXELS, WIDTH, HEIGHT, CHANNELS);
    
    // 

    

    // validate image processing
    validateImageProcessing(h_serialConvImage, h_convImage, NUM_PIXELS * CHANNELS);
    validateImageProcessing(h_serialConvImage, h_convImage, NUM_PIXELS * CHANNELS);

    // Save the converted image in a binary file named gc.raw
    fp = fopen(OUTPUT_FILE.c_str(), "wb");
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << OUTPUT_FILE << std::endl;
        return 1;
    }
    fwrite(&h_convImage[0], sizeof(unsigned char), NUM_PIXELS * CHANNELS, fp);
    fclose(fp);
}

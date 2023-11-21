/**
 * @file hw51.cpp
 * @author Carter Watson
 * @date nov-20-2023
 * @brief CUDA program to convert a color image to gray scale
 * @todo
 * PART 1: CUDA program to convert a color image to gray scale
 * - [X] read the image file
 * - [ ] write a kernal function to perform the gray scale conversion using CUDA
 *   - remember to treat the matrices as 1D arrays and use the corresponding linearization of indexes for every memory access you perform
 *   - provide only the program with your comments as your solution. No need to attach input or output files
 * - [X] save the converted image in a binary file named gc.raw
 * 
 * PART 2: GPU Information
 * - Pick a particular GPU (e.g., from the ones available on a CHPC cluster) and report the information
 *   - [ ] Max num of threads per SM
 *   - [ ] Assume max num of blocks per SM is 8
 * - [ ] choose three different block sizes and explain analytically how the different block sizes should affect the performance of the application made in Part 1
 * - [ ] report experimental results using the three different block sizes
 *   - (i.e., run the kernel 200 times to assess the time accurately)
 * 
 * @note This program is only meant to be run on University of Utah CHPC machines
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iomanip>

#include "device_query.cu"


/**
 * @brief CUDA function to convert a color image to gray scale
 * 
 * @param rgbImage (std::vector<unsigned char>) unprocessed image
 * @param width (int) width of image
 * @param height (int) height of image
 * 
 * @return processed_image (std::vector<unsigned char>) processed image
 * 
 * @note This function is primarily from lecture notes
 */
std::vector<unsigned char> RGBToGrayscale(std::vector<unsigned char> rgbImage, int width, int height, int channels)
{
    std::vector<unsigned char> grayImage(width*height);
    int Col = threadIdx.x + blockIdx.x * blockDim.x;
    int Row = threadIdx.y + blockIdx.y * blockDim.y;

    if (Col < width && Row < height) {
        // get 1D coordinate for the grayscale image
        int grayOffset = Row*width + Col;

        // one can think of the RGB image having CHANNEL times columns of the gray scale image
        int rgbOffset = grayOffset * channels;
        unsigned char r = rgbImage[rgbOffset ]; // red value for pixel
        unsigned char g = rgbImage[rgbOffset + 1]; // green value for pixel
        unsigned char b = rgbImage[rgbOffset + 2]; // blue value for pixel

        // perform the rescaling and store it
        // NOTE: this implementation may result in rounding errors
        grayImage[grayOffset] = 0.21f*r + 0.71f*g + 0.07f*b;
    }

    return grayImage;
}


/**
* @brief 
* 
* @param input_file (str) name of the input file
* @param output_file (str) name of the output file
* @note param ordering: <input_file> <output_file>
* @note both params are optional, if not provided, default values will be used
* @note image is assumed to be 1024x1024 and have three channels, this is hardcoded
* 
* @return error_code (int) 
* @retval 0 Success
* @retval 1 Invalid number of arguments
*/
int main(int argc, char *argv[]) {
    // init variables
    std::string INPUT_FILE = "gc_conv_1024x1024.raw";
    std::string OUTPUT_FILE = "gc.raw";
    const int WIDTH = 1024;
    const int HEIGHT = 1024;
    const int NUM_PIXELS = WIDTH * HEIGHT;
    const int CHANNELS = 3;

    // Check to see if valid # of params provided
    if (argc > 4) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }
    // Assign file names as provided
    if (argc == 3) { OUTPUT_FILE = argv[2]; }
    if (argc >= 2) { INPUT_FILE = argv[1]; }
    
    // PART 1
    // init variables for reading in image
    std::vector<unsigned char> unprocessed_image(NUM_PIXELS * CHANNELS); // multiplied by 3 for RGB channels
    FILE *fp;
    fp = fopen(INPUT_FILE.c_str(), "rb");
    // make sure file exists
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << INPUT_FILE << std::endl;
        return 1;
    }
    // Read in the image file
    fread(&unprocessed_image[0], sizeof(unsigned char), NUM_PIXELS, fp);
    fclose(fp);

    // Convert the image to grayscale
    std::vector<unsigned char> processed_image = RGBToGrayscale(unprocessed_image, WIDTH, HEIGHT, CHANNELS);

    // Save the converted image in a binary file named gc.raw
    fp = fopen(OUTPUT_FILE.c_str(), "wb");
    if (fp == NULL) {
        std::cout << "ERROR: Could not open file " << OUTPUT_FILE << std::endl;
        return 1;
    }
    fwrite(&processed_image[0], sizeof(unsigned char), NUM_PIXELS, fp);
    fclose(fp);


    // PART 2
    // Pick a particular GPU (e.g., from the ones available on a CHPC cluster) and report the information
        // Max num of threads per SM
        // Assume max num of blocks per SM is 8
    // use device query.cu to get info

    // Choose three different block sizes and explain analytically how the different block sizes should affect the performance of the application made in Part 1
    // Report experimental results using the three different block sizes


    
    return 0;
}

/**
 * @file histogram.cpp
 * @author Carter Watson
 * @date oct-13-2023
 * @brief 
 * @todo [ ] 
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

/**
* @brief 
* 
* @param number_of_threads (int) the number of threads to use for the execution
* @param bin_count (int) the number of bins in the histogram
* @param min_meas (float) minimum value of the measurements
* @param max_meas (float) maximum value of the measurements
* @param data_count (int) number of measurements
* @note param ordering: <number of threads> <bin count> <min meas> <max meas> <data count>
* 
* @return error_code (int) 
* @retval 0 Success
* @retval 1 Invalid number of arguments
*/
int main(int argc, char *argv[]) {
    // Check to see if valid # of params provided
    if (argc != 3) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }

    // init params
    const int NUM_THREADS = std::stoi(argv[1]);
    const int NUM_ELEMENTS =  std::stoi(argv[2]);
}
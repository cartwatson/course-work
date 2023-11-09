/**
 * @file histogram.cpp
 * @author Carter Watson
 * @date nov-08-2023
 * @brief implementation of histogram using reduction summation
 * @todo
 * - [X] implement command line arg
 * - [ ] implement mpi
 *   - [ ] have process 0 read in the input data and dsitribute them among all processes
 *   - [ ] have process 0 populate an array of <data_count> float elements between <min_meas> and <max_meas>.
 *      - [] init with srand(100)
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <thread>
#include <mutex>


/**
* @brief prints results to std::cout after being passed computed bin_maxes and bin_counts
*
* @param bin_maxes (vector<float>) The maxes of each bin
* @param bin_counts (vector<int>) The counts of each bin
* 
* @return void
*/
void printResults(std::vector<float> bin_maxes, std::vector<int> bin_counts) {
    // print maxes
    std::cout << "bin_maxes:";
    for (int i = 0; i < bin_maxes.size(); i++) { std::cout << " " << std::fixed << std::setprecision(3) << bin_maxes[i]; }
    std::cout << std::endl;

    // print counts
    std::cout << "bin_counts:";
    for (int i = 0; i < bin_counts.size(); i++) { std::cout << " " << bin_counts[i]; }
    std::cout << std::endl << std::endl;

    return;
}

/**
 * @brief Function to generate a random float between two bounds
 * 
 * @param lower_bound (float) lower bound of the random float
 * @param upper_bound (float) upper bound of the random float
 * 
 * @return float
 */ 
float random_float(float lower_bound, float upper_bound) {
    float random = ((float) std::rand()) / (float) RAND_MAX;
    float diff = upper_bound - lower_bound;
    return lower_bound + random * diff;
}

/**
* @brief 
* 
* @param bin_count (int) the number of bins in the histogram
* @param min_meas (float) minimum value of the measurements
* @param max_meas (float) maximum value of the measurements
* @param data_count (int) number of measurements
* @note param ordering: <bin count> <min meas> <max meas> <data count>
* 
* @return error_code (int) 
* @retval 0 Success
* @retval 1 Invalid number of arguments
*/
int main(int argc, char *argv[]) {
    // Check to see if valid # of params provided
    if (argc != 5) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }

    // init params
    const int BIN_COUNT =  std::stoi(argv[1]);
    const float MIN_MEAS = std::stof(argv[2]);
    const float MAX_MEAS = std::stof(argv[3]);
    const int DATA_COUNT = std::stoi(argv[4]);

    // init data with srand
    srand(100);
    std::vector<std::vector<float>> data_chunks(BIN_COUNT);
    for (int i = 0; i < DATA_COUNT; ++i) {
        float randomValue = random_float(MIN_MEAS, MAX_MEAS);
        data_chunks[i % BIN_COUNT].push_back(randomValue);
    }

// mpi implementation
    // init variables for global sum
    std::vector<float> bin_maxes;
    std::vector<int> bin_counts(BIN_COUNT, 0); // init vector with 0s


    printResults(bin_maxes, bin_counts);
    return 0;
}

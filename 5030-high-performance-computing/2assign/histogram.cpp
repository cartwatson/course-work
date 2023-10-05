/**
 * @file histogram.cpp
 * @author Carter Watson
 * @date 2023-09-29
 * @brief This file uses multithreading to create histograms using various algorithms/methodologies
 * @todo [X] populate an array (data) of <data_count> float elements between <min_meas> and <max_meas>. Use srand(100) to initialize your pseudorandom sequence.
 * compute the histogram using using <number of threads> threads using a...
    * @todo [X] global sum
    * @todo [ ] tree structured sum 
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
* @param calculation_type (string) The type of calculation, used only for output 
* 
* @return void
*/
void printResults(std::vector<float> bin_maxes, std::vector<int> bin_counts, std::string calculation_type) {
    // prit calculation type used 
    std::cout << calculation_type << std::endl;

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
 * @brief Function to generate a histogram using a global summing techniques
 */
void generateHistogramGlobalSum(const std::vector<float>& data, int BIN_COUNT, float MIN_MEAS, float UPPER_BOUND, std::vector<int>& bin_counts_global, std::mutex& mutex_global_sum) {
    // Local histogram for this thread
    std::vector<int> local_histogram(BIN_COUNT, 0);

    // Categorize data into bins
    for (float value : data) {
        int binIndex = (int)((value - MIN_MEAS) / (UPPER_BOUND - MIN_MEAS) * BIN_COUNT);
        if (binIndex >= 0 && binIndex < BIN_COUNT) {
            local_histogram[binIndex]++;
        }
    }

    // Lock the mutex to safely update g_histogram
    std::lock_guard<std::mutex> lock(mutex_global_sum);
    for (int i = 0; i < BIN_COUNT; ++i) {
        bin_counts_global[i] += local_histogram[i];
    }

    return;
}

/**
 * @brief Function to generate a random float between two bounds
 */ 
float random_float(float lower_bound, float upper_bound) {
    float random = ((float) std::rand()) / (float) RAND_MAX;
    float diff = upper_bound - lower_bound;
    return lower_bound + random * diff;
}

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
    if (argc != 6) {
        std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
        return 1;
    }

    // init params
    const int NUM_THREADS = std::stoi(argv[1]);
    const int BIN_COUNT =  std::stoi(argv[2]);
    const float MIN_MEAS = std::stof(argv[3]);
    const float MAX_MEAS = std::stof(argv[4]);
    const int DATA_COUNT = std::stoi(argv[5]);

    // init data with srand
    srand(100);
    std::vector<std::vector<float>> data_chunks(BIN_COUNT);
    for (int i = 0; i < DATA_COUNT; ++i) {
        float randomValue = random_float(MIN_MEAS, MAX_MEAS);
        data_chunks[i % BIN_COUNT].push_back(randomValue);
    }

// GLOBAL SUM
    // init variables for global sum
    std::vector<float> bin_maxes_global;
    std::vector<int> bin_counts_global(BIN_COUNT, 0); // init vector with 0s
    std::mutex mutex_global_sum;

    // Create a vector of threads
    std::vector<std::thread> threads;

    // Launch NUM_THREADS threads
    for (int i = 0; i < NUM_THREADS; ++i) {
        threads.push_back(std::thread(generateHistogramGlobalSum, data_chunks[i], BIN_COUNT, MIN_MEAS, MAX_MEAS, std::ref(bin_counts_global), std::ref(mutex_global_sum)));
    }

    // Join all threads to ensure they complete before exiting main
    for (auto& thread : threads) { thread.join(); }

    // calculate bin_maxes
    for (int i = 0; i < BIN_COUNT; ++i) {
        bin_maxes_global.push_back(MIN_MEAS + (MAX_MEAS - MIN_MEAS) / BIN_COUNT * (i + 1));
    }

    printResults(bin_maxes_global, bin_counts_global, "Global Sum");

// TREE STRUCTURED SUM - binary tree
    // // init variables for tree structured sum
    // std::vector<float> bin_maxes_tree;
    // std::vector<int> bin_counts_tree;
    // std::mutex mutex_tree_structured_sum;

    // // Create a vector of threads
    // std::vector<std::thread> threads_tree;

    // // Launch NUM_THREADS threads
    // for (int i = 0; i < NUM_THREADS; ++i) {
    //     threads_tree.push_back(std::thread(generateHistogramTreeStructuredSum, ));
    // }

    // // calculate bin_maxes
    // for (int i = 0; i < BIN_COUNT; ++i) {
    //     bin_maxes_tree.push_back(MIN_MEAS + (MAX_MEAS - MIN_MEAS) / BIN_COUNT * (i + 1));
    // }

    // printResults(bin_maxes_tree, bin_counts_tree, "Tree Sturctured Sum");

    return 0;
}

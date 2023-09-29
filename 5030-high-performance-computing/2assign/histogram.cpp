/**
 * @file histogram.cpp
 * @author Carter Watson
 * @date 2023-09-29
 * @brief This file uses multithreading to create histograms using various algorithms/methodologies
 * @todo [X] populate an array (data) of <data_count> float elements between <min_meas> and <max_meas>. Use srand(100) to initialize your pseudorandom sequence.
 * compute the histogram using using <number of threads> threads using a...
    * @todo [ ] global sum
    * @todo [ ] tree structured sum 
 */

#include <iostream>
#include <cstdlib>
#include <stdio.h>

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
    if (argc != 6) {fprintf("ERROR: Inappropriate number of arguments provided!"); return 1;}

    // init params
    int num_of_threads = argv[1];
    int bin_count = argv[2];
    float min_meas = argv[3];
    float max_meas = argv[4];
    int data_count = argv[5];
    
    // init other variables
    std::vector<float> data;

    // init data with srand
    srand(100);
    for(int i = 0; i < data_count; i++) {
        // generates random number, puts its between 0 and 1, adds minimum value
        float temp = rand() / RAND_MAX + min_meas;
        if (temp > max_meas) {temp %= max_meas;}
        data.push_back(temp)
    }

// GLOBAL SUM
    // init variables for global sum
    std::vector<float> bin_maxes_global;
    std::vector<int> bin_counts_global;

    // divide data into N/P elements, take care of remainder where N is number of data points and P is num of threads
    // build local histogram
    // contribute local histogram to global
    printResults(bin_maxes_global, bin_counts_global, "Global Sum");

// TREE STRUCTURED SUM - binary tree
    // init variables for tree structured sum
    std::vector<float> bin_maxes_tree;
    std::vector<int> bin_counts_tree;

    // split into tree
    // add up every level
        // something to do with the powers of two
    printResults(bin_maxes_tree, bin_counts_tree, "Tree Sturctured Sum");

    return 0;
}

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
    std::cout << calculation_type << endl;

    // print maxes - configure decimal places
    std::cout << "bin_maxes:" << std::setprecision(3);
    for (int i = 0; i < bin_maxes.size(); i++) { std::cout << " " << bin_maxes[i]; }
    std::cout << std::endl;

    // print counts
    std::cout << "bin_counts:";
    for (int i = 0; i < bin_counts.size(); i++) { std::cout << " " << bin_counts[i]; }
    std::cout << std::endl;

    return;
}

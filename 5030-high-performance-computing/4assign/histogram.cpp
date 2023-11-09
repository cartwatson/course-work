/**
 * @file histogram.cpp
 * @author Carter Watson
 * @date nov-08-2023
 * @brief implementation of histogram using reduction summation
 * @todo
 * - [X] implement command line arg
 * - [X] implement mpi
 *   - [X] have process 0 read in the command line arguments and dsitribute them among all processes
 *   - [X] have process 0 populate an array of <data_count> float elements between <min_meas> and <max_meas>.
 *      - [X] init with srand(100)
 *  - [X] have process 0 distribute portions of the pseudorandom sequence to the other processors
 *    - note: do not share the entire array with all other processes
 *  - [X] compute the histogram
 *  - [X] have process 0 print the results
 *  - [X] verify and test
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <mpi.h>


/**
* @brief prints results to std::cout after being passed computed bin_maxes and bin_counts
*
* @param bin_maxes (vector<float>) The maxes of each bin
* @param bin_counts (vector<int>) The counts of each bin
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
 * @brief generate a random float between two bounds
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
 * @brief generate a vector of vectors of floats
 * 
 * @param BIN_COUNT (int) the number of bins in the histogram
 * @param MIN_MEAS (float) minimum value of the measurements
 * @param MAX_MEAS (float) maximum value of the measurements
 * @param DATA_COUNT (int) number of measurements
 * 
 * @return std::vector<float>
*/
std::vector<float> generateData(int BIN_COUNT, float MIN_MEAS, float MAX_MEAS, int DATA_COUNT) {
    std::vector<float> data(DATA_COUNT);

    srand(100);
    for (int i = 0; i < DATA_COUNT; ++i) {
        float randomValue = random_float(MIN_MEAS, MAX_MEAS);
        data[i] = randomValue;
    }

    return data;
}

/**
 * @brief generate a histogram serially
 * 
 * @param BIN_COUNT (int) the number of bins in the histogram
 * @param MIN_MEAS (float) minimum value of the measurements
 * @param MAX_MEAS (float) maximum value of the measurements
 * @param DATA_COUNT (int) number of measurements
 * @param data_chunks (std::vector<float>) the data to be used in the computation
 * 
 * @return void
*/
void serialImplementation(int BIN_COUNT, float MIN_MEAS, float MAX_MEAS, int DATA_COUNT, std::vector<float> data) {
    // init variables
    float binWidth = (MAX_MEAS - MIN_MEAS) / BIN_COUNT;
    std::vector<float> binMaxes(BIN_COUNT);
    std::vector<int> bin_counts(BIN_COUNT, 0);

    // compute binMaxes
    for (int i = 0; i < BIN_COUNT; ++i) { binMaxes[i] = MIN_MEAS + binWidth * (i + 1); }

    for (float value : data) {
        int binIndex = (int)((value - MIN_MEAS) / (MAX_MEAS - MIN_MEAS) * BIN_COUNT);
        if (binIndex >= 0 && binIndex < BIN_COUNT) {
            bin_counts[binIndex]++;
        }
    }

    // print results
    printResults(binMaxes, bin_counts, "Serial Implementation");
}

/**
* @brief run serial and mpi implementations of histogram computation
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
    // init mpi
    MPI_Init(&argc, &argv);

    // init rank and size for mpi
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // init var before for use in bcast
    int BIN_COUNT;
    float MIN_MEAS;
    float MAX_MEAS;
    int DATA_COUNT;
    std::vector<float> data;

    // only do the following on rank 0
    if (rank == 0) {
        // Check to see if valid # of params provided
        if (argc != 5) {
            std::cout << "ERROR: Inappropriate number of arguments provided!" << std::endl;
            return 1;
        }

        // read in input data
        BIN_COUNT  = std::stoi(argv[1]);
        MIN_MEAS   = std::stof(argv[2]);
        MAX_MEAS   = std::stof(argv[3]);
        DATA_COUNT = std::stoi(argv[4]);

        // generate psuedorandom data
        data = generateData(BIN_COUNT, MIN_MEAS, MAX_MEAS, DATA_COUNT);

        // run serial implementation
        serialImplementation(BIN_COUNT, MIN_MEAS, MAX_MEAS, DATA_COUNT, data);
    }

    // use bcast to send input data to all processes, includes process 0 as root
    MPI_Bcast(&BIN_COUNT, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&MIN_MEAS, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&MAX_MEAS, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&DATA_COUNT, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // init variables for each process
    const int chunkSize = DATA_COUNT / size;
    const float binWidth = (MAX_MEAS - MIN_MEAS) / BIN_COUNT;
    std::vector<float> localData(chunkSize);
    std::vector<int> localBinCounts(BIN_COUNT, 0);
    std::vector<float> binMaxes = std::vector<float>(BIN_COUNT);

    // distribute portions of the pseudorandom sequence to the other processors, includes process 0 as root
    MPI_Scatter(data.data(), chunkSize, MPI_INT, localData.data(), chunkSize, MPI_INT, 0, MPI_COMM_WORLD);

    // rank 0 processes the remainder data
    // NOTE: this is **not** the most efficient way to do this, causes load imbalance on root
    int remainder = DATA_COUNT % size;
    if (rank == 0) {
        for (int i = DATA_COUNT - remainder; i < DATA_COUNT; ++i) {
            localData.push_back(data[i]);
        }
    }

    // compute binMaxes
    for (int i = 0; i < BIN_COUNT; ++i) { binMaxes[i] = MIN_MEAS + binWidth * (i + 1); }

    // compute local histogram
    for (float value : localData) {
        int binIndex = (int)((value - MIN_MEAS) / (MAX_MEAS - MIN_MEAS) * BIN_COUNT);
        if (binIndex >= 0 && binIndex < BIN_COUNT) {
            localBinCounts[binIndex]++;
        }
    }

    // sum local histograms, only on rank 0
    std::vector<int> totalBinCounts(BIN_COUNT);
    MPI_Reduce(localBinCounts.data(), totalBinCounts.data(), BIN_COUNT, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    // print results, only on rank 0
    if (rank == 0) { printResults(binMaxes, totalBinCounts, "MPI Implementation"); }

    // end mpi and return
    MPI_Finalize();
    return 0;
}

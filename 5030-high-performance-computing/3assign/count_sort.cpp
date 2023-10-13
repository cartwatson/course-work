/**
 * @file histogram.cpp
 * @author Carter Watson
 * @date oct-13-2023
 * @brief 
 * @todo
 * - [X] Generate random integers in the range 1 to n (initialize with srand(100) ) 
 * - [X] print the original sequence
 * - [ ] sort the sequence using multithreading
 * - [X] print the ordered sequence
 */
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <omp.h>
#include <cstring>
#include <cstdlib>

/**
 * @brief sorts an array of integers using the count sort algorithm and uses multithreading
 * 
 * @param a (int[]) the array to sort
 * @param n (int) the number of elements in the array
 * 
 * @return void
*/
void count_sort(int a[], int n) {
    int *temp = (int *)malloc(n * sizeof(int));

    #pragma omp parallel
    {
        int i, j, count;

        #pragma omp for schedule(dynamic)
        for (i = 0; i < n; i++) {
            count = 0;
            for (j = 0; j < n; j++) {
                if (a[j] < a[i]) {
                    count++;
                } else if (a[j] == a[i] && j < i) {
                    count++;
                }
            }
            temp[count] = a[i];
        }
    }

    memcpy(a, temp, n * sizeof(int));
    free(temp);
}


/**
 * @brief print elements of vector to std::cout
 * 
 * @param elements (vector<int>) the vector to print
 * @param original (bool) whether or not the vector is the original data
 * 
 * @return void
 */
void printData(std::vector<int> elements, bool original = false) {
    std::cout << (original ? "original:" : "sorted:");

    for (int i = 0; i < elements.size(); i++) {
        std::cout << " " << elements[i];
    }

    std::cout << std::endl;
    return;
}


/**
* @brief 
* 
* @param number_of_threads (int) the number of threads to use for the execution
* @param number_of_elements (int) the number of elements
* @note param ordering: <number of threads> <number of elements>
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

    // init data with srand
    srand(100);
    std::vector<int> data;
    for (int i = 0; i < NUM_ELEMENTS; ++i) {
        data.push_back(std::rand() % 100);
    }

    printData(data, true); // print original data

    // sort data using multithreading
    count_sort(&data[0], NUM_ELEMENTS);

    printData(data); // print sorted data

    return 0;
}

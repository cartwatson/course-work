#include <iostream>
#include "Sorts.hpp"

Sorts::Sorts()
{
    //constructor
}

void Sorts::bubble(int* pArray, int length)
{
    //initialize variables
    int i, j; 
    bool swapped; 
    //cycle length of array
    for (i = 0; i < length-1; i++) 
    { 
        //initialize swapped each loop
        swapped = false; 
        //go through array length - i times
        for (j = 0; j < length-i-1; j++) 
        { 
            //if curr element is larger than next element 
            if (pArray[j] > pArray[j+1]) 
            { 
                //swap elements
                swap(&pArray[j], &pArray[j+1]); 
                //change swapped's value
                swapped = true; 
            } 
        } 

        // If no elements were swapped, then break 
        if (swapped == false)
        {
            break; 
        }
    }

}

void Sorts::selection(int* pArray, int length)
{
    //initialize variables
    int newMin;  
  
    // One by one move boundary of unsorted subarray  
    for (int i = 0; i < length-1; i++)  
    {  
        // Find the newMinimum element in unsorted array  
        newMin = i;  
        for (int j = i+1; j < length; j++)
        {
            if (pArray[j] < pArray[newMin])
            {
                newMin = j;
            }  
        }
        // Swap the found newMinimum element with the first element  
        swap(&pArray[newMin], &pArray[i]);  
    }
}

void Sorts::quick(int* pArray, int length)
{  
    
}  

void Sorts::swap(int* x, int* y)  
{  
    int temp = *x;
    *x = *y;
    *y = temp;
} 
#ifndef SORTS_HPP
#define SORTS_HPP

class Sorts
{
    public:
        Sorts();
        void bubble(int* pArray, int length);
        void selection(int* pArray, int length);
        void quick(int* pArray, int length);
    private:
        void swap(int* xp, int*yp);
};

#endif //SORTS_HPP
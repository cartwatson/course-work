# Unit 2
Line Drawing Algs
* Digital Differential Analyzer DDA
  1. compute delta X and delta Y
  2. determine how many points to compute
     * num = |dX| > |dY| ? |dX|+1 else |dY|+1 
  3. compute x and y increments
     * increment X = dX / num
     * increment Y = dY / num
  4. plot points
* Bresenham
  * pretty efficient
  * Steps
    1. find distance that is larger from (next pixel in x) and (next pixel in x where y++) to y-int
       1. center of x+1, y+1
       2. center of x+1, y
    2. bruh, just check slides
    3. starting point is always 0, 0
       * y_k and x_k are both 0
    * final equations on slides
  * symmetry on octants
  * limitations
    * 1 >= slope >= 0
    * assume pixel centers are half integers
    * if we start at a pixel that has already been written, only two canidates for next pixel, same Y or incremented Y
* Midpoint
  * not as efficient
  * cricle and ellipse based on this
* two step & symmetric two step
  * basically bresenham

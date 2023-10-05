# Introduction
In this assignment you'll be computing the digits of Pi, in parallel.  The purpose of this assignment is to have you write a multi-threaded application that utilizes all available cores of any computer in a coordinated effort to compute thousands of digits of the constant Pi.  Each core will work on a task to compute a single digit of the fractional part of Pi, while sharing a common data structure from which to obtain the tasks and another shared data structure into which the results should be placed.  This will help you become familiar with multi-threaded code, which includes coordination of shared resources.

# Assignment
Write a multi-threaded program that computes the first 1000 digits of Pi (to the right of the decimal).  The program must utilize all system CPU cores simultaneously, using a task-based scheme to distribute the work.  The program should be written according to the following specifications:

1. Create a FIFO queue that stores the compute tasks
   1. Name the class TaskQueue.
   2. Use a Java Collection LinkedList as the underlying data structure.  Use aggregation, rather than inheritance to create this queue.
      1. Reference: https://www.javatpoint.com/java-linkedlist (Links to an external site.)
   3. This queue must be protected against race conditions.
   4. At program startup, before creating any of the worker threads, fully populate this queue with 1 task per digit to be computed; 1000 tasks.  Each task will say which digit to compute.
   5. Before adding the numbers to the your task queue, randomize them so that each task that comes off the queue has a much different computational time than the one before it.  This doesn't affect the overall speed, but creates a slightly more interesting queue of tasks to work on (interesting to me, anyway).  You can do this by first putting the numbers into an ArrayList and the calling java.util.Collections.shuffle(myArray).  Then, loop through that array and add those numbers as tasks to your TaskQueue.
   6. This is a shared resource available to all worker threads, it must be protected against race conditions.  Pass a reference to the queue via the worker thread's constructor (not a global variable).
2. Create a hash table to store the results.  Each entry in the hash table has as its key the digit position and the computed Pi digit as its value.
   1. Name the class ResultTable.
   2. Use a Java HashMap as the underlying data structure.  Use aggregation, rather than inheritance.
   3. This hash table must be protected against race conditions.
   4. This is a shared resource available to all worker threads, it must be protected against race conditions. Pass a reference to the hashtable via the worker thread's constructor (not a global variable).
3. Create as many worker threads as there are CPU cores; rather than hard-coding the number of threads.  Each of these worker threads obtains a task from the FIFO task queue, computes the requested digit, then stores the result in the hash table.  It continues retrieving tasks from the queue until there are none, then it voluntarily terminates.
   1. Create a constructor on your worker thread class that accepts a reference to the task queue and the results table, storing a private reference to these objects.  Then, once the class is running in a thread, it will reference those objects for obtaining tasks and storing the results.
   2. Don't use an ExecutorService for these threads, I want you to create the worker threads yourself and ensure they don't cause a race condition while accessing the TaskQueue.
4. As work is completed on computing the digits, report a "." (a period, not including the quotes) to the screen for every 10th digit completed (overall, not by each worker thread).
   1. You might find it necessary to call System.out.flush() in order to ensure immediate display of the "." character.
5. When the FIFO queue is empty and all threads have finished their work, display the computed value of Pi.
6. Track the total wall clock time it took to compute the Pi digits and report that time after printing the digits of Pi.
7. After the display is complete, the program should gracefully exit.

# Notes
* Create a build.gradle file that can be used to build the project, including creating a runnable jar file.
* You can use the utility 'htop' to visually watch the CPU cores utilization on a Linux computer.  It can be installed by "sudo apt-get install htop".
* You should use the Bailey-Borwein-Plouffe formula for computing the nth digit of Pi.
  * Wiki link about the formula: https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula (Links to an external site.)
  * Java Implementation: https://github.com/feltocraig/BBP-Bellard (Links to an external site.)
    * Be aware that when the digit of interest is 0, the leading digit won't be zero.  You'll need to be aware of this and account for that condition as you extract the digit.  You can test either the magnitude of the value or the length of the value to determine if the computed digit should be a 0.
* Here is a link that provides reference files for the first (up to) 1 million digits of Pi.  You can use this to help verify your code is computing correctly: https://www.piday.org/million/ (Links to an external site.)
* There is another technique for computing the digits of PI, one I haven't tried.  It is supposed to be the standard for computing the digits FAST.  If anyone tries this code, let me know how it goes, I suspect it is significantly faster than the Java code I have referenced.  You can find code and discussion at the following links:
  * https://gmplib.org/pi-with-gmp.html (Links to an external site.)
  * https://en.wikipedia.org/wiki/Chudnovsky_algorithm (Links to an external site.)
  * http://www.craig-wood.com/nick/articles/pi-chudnovsky/ (Links to an external site.) (and it is "math" in the US, not "maths", that is British English).

import java.lang.Runtime;
import java.util.*;

public class ParallelPi {
    public static void main(String[] args) {
        // number of digits to compute
        final int numOfDigits = 1000;

        // get runtime instance
        Runtime runtime = Runtime.getRuntime();

        // start time
        long start = System.currentTimeMillis();

        // create queue
        TaskQueue taskQueue = new TaskQueue(numOfDigits);

        // create hash table
        ResultTable results = new ResultTable(numOfDigits);

        // number of worker threads = number of cores
        int processors = runtime.availableProcessors();
        Thread[] threads = new Thread[processors];
        for (int i = 0; i < processors; i++) {
            // create worker threads
            threads[i] = new Thread(new WorkerThread(taskQueue, results));
            threads[i].start();
        }

        // init counter for outputing loading symbols
        int x = 10;
        System.out.print("Loading");
        while (results.getSize() < numOfDigits) {
            // for every tenth digit computed ouput a period
            int digitsComputed = 0;
            if (results.getSize() >= x) {
                x += 10;
                System.out.print(".");
                System.out.flush();
            }
        }
        //end line after loading...
        System.out.print("."); // print for last set of ten
        System.out.println();
        
        // --- all digits computed, print results and exit ---
        long end = System.currentTimeMillis();
        // display computed value
        System.out.print("Computed Value of Pi: 3.");
        for (int i = 1; i <= numOfDigits; i++) {
            System.out.print(results.getValue(i));
        }
        System.out.println();
        // print total time
        System.out.println("Total Time (mS): " + (end - start));
    }
}

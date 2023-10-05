import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Assign5 {
    // init counters
    public static int FIFO_PF = 0;
    public static int LRU_PF = 0;
    public static int MRU_PF = 0;

    // max page fault counter
    public static int FIFO_MAX = 0;
    public static int LRU_MAX = 0;
    public static int MRU_MAX = 0;

    // init page faults array
    public static int[] FIFO_TOTAL_PF = new int[100];
    public static int[] LRU_TOTAL_PF = new int[100];
    public static int[] MRU_TOTAL_PF = new int[100];

    // init arrays to track Belady's Anomaly
    public static List<String> FIFO_Belady = new ArrayList<>();
    public static List<String> LRU_Belady = new ArrayList<>();
    public static List<String> MRU_Belady = new ArrayList<>();

    public static void main(String[] args) throws InterruptedException {
        // get # of cores
        int threadCount = Runtime.getRuntime().availableProcessors();
        ExecutorService executor = Executors.newFixedThreadPool(threadCount);

        // start timer
        long start = System.currentTimeMillis();

        // execute sim
        for (int i = 0; i < 1000; i++) {
            executor.execute(new Simulator());
        }
        executor.shutdown();
        while (!executor.isTerminated()){
            Thread.sleep(50);
        }

        // stop timer, report sim
        long finish = System.currentTimeMillis();
        report(finish - start);
    }

    static class Simulator implements Runnable {
        public void run() {
            // init var
            int maxPageReference = 250;

            // create random list; len 1000
            for (int i = 0; i < 100; i++) {
                int[] sequence = randomList(1000);
                int FIFO_Counter = (new TaskFIFO(sequence, i + 1, maxPageReference)).run();
                int LRU_Counter = (new TaskLRU(sequence, i + 1, maxPageReference)).run();
                int MRU_Counter = (new TaskMRU(sequence, i + 1, maxPageReference)).run();

                // Add each simulation to the tracking array
                FIFO_TOTAL_PF[i] = FIFO_Counter;
                LRU_TOTAL_PF[i] = LRU_Counter;
                MRU_TOTAL_PF[i] = MRU_Counter;

                // Determine what the most accurate simulation algorithm was
                int lowestCounter = Integer.MAX_VALUE;

                if (FIFO_Counter < lowestCounter) {
                    lowestCounter = FIFO_Counter;
                }
                if (LRU_Counter < lowestCounter) {
                    lowestCounter = LRU_Counter;
                }
                if (MRU_Counter < lowestCounter) {
                    lowestCounter = MRU_Counter;
                }

                // Increase the counter of each simulator if it is the lowest (allows for ties)
                if (FIFO_Counter == lowestCounter) {
                    FIFO_PF++;
                }
                if (LRU_Counter == lowestCounter) {
                    LRU_PF++;
                }
                if (MRU_Counter == lowestCounter) {
                    MRU_PF++;
                }
                if (FIFO_Counter > FIFO_MAX) {
                    FIFO_MAX = FIFO_Counter;
                }
            }

            // Check for Belady's Anomaly
            boolean FIFO_Checker = false;
            int FIFO_Belady_Counter = 0;
            boolean LRU_Checker = false;
            int LRU_Belady_Counter = 0;
            boolean MRU_Checker = false;
            int MRU_Belady_Counter = 0;

            if (FIFO_TOTAL_PF[99] > FIFO_TOTAL_PF[0]) {
                FIFO_Checker = true;
                FIFO_Belady_Counter = FIFO_TOTAL_PF[99];
            }
            if (LRU_TOTAL_PF[99] > LRU_TOTAL_PF[0]) {
                LRU_Checker = true;
                LRU_Belady_Counter = LRU_TOTAL_PF[99];
            }
            if (MRU_TOTAL_PF[99] > MRU_TOTAL_PF[0]) {
                MRU_Checker = true;
                MRU_Belady_Counter = MRU_TOTAL_PF[99];
            }

            // If Belady is found, add it to the list to be reported
            if (FIFO_Checker) {
                FIFO_Belady.add("Detected - found with a difference of " + FIFO_Belady_Counter);
            }
            if (LRU_Checker) {
                LRU_Belady.add("Detected - found with a difference of " + LRU_Belady_Counter);
            }
            if (MRU_Checker) {
                MRU_Belady.add("Detected - found with a difference of " + MRU_Belady_Counter);
            }
        }
    }


    // creates list of random ints
    public static int[] randomList(int listLen) {
        Integer[] sequence = new Integer[listLen];
        for (int i = 0; i < listLen; i++) {
            sequence[i] = i + 1;
        }

        // Converts the array to a list, so it can be shuffled
        List<Integer> intSequence = Arrays.asList(sequence);
        Collections.shuffle(intSequence);

        // Returns the shuffled list, converted back as an array
        return intSequence.stream().mapToInt(Integer::intValue).toArray();
    }

    // The final report for the program
    public static void report(long totalTime) {
        // calculate scaled pf
        int totalPageFaults = FIFO_PF + LRU_PF + MRU_PF;
        float scaledFIFO = ((float) FIFO_PF * ((float) FIFO_PF / (float) totalPageFaults));
        float scaledLRU = ((float) LRU_PF * ((float) LRU_PF / (float) totalPageFaults));
        float scaledMRU = ((float) MRU_PF * ((float) MRU_PF / (float) totalPageFaults));

        // print final report
        System.out.println("Simulation took " + (totalTime) + " milliseconds\n");
        System.out.println("FIFO min PF : " + ((int) scaledFIFO));
        System.out.println("LRU min PF  : " + ((int) scaledLRU));
        System.out.println("MRU min PF  : " + ((int) scaledMRU) + "\n");
        printBelady(FIFO_Belady, "FIFO", FIFO_MAX);
        printBelady(LRU_Belady, "LRU", LRU_MAX);
        printBelady(MRU_Belady, "MRU", MRU_MAX);
    }

    // Print items in report
    public static void printBelady(List<String> list, String name, int max) {
        System.out.println("Belady's Anomaly Report for " + name);
        for (String s : list) {
            System.out.println("\t" + s);
        }
        System.out.println("\tAnomaly detected " + list.size() + " times with a max difference of " + max + "\n");
    }
}

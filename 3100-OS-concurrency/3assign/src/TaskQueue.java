import java.util.*;

// FIFO Queue is a shared resource available to all worker threads,
    // it must be protected against race conditions.
    // Pass a reference to the queue via the worker thread's constructor
    // (not a global variable).
public class TaskQueue {
    private LinkedList<Task> queue = new LinkedList<>();

    public TaskQueue(int size) {
        // Create FIFO Queue
        // TODO: protect against race conditions
        // create array list so tasks can be randomized
        ArrayList<Task> tasks = new ArrayList<>();
        for (int i = 1; i <= size; i++) {
            tasks.add(new Task(i));
        }
        // randomize tasks
        java.util.Collections.shuffle(tasks);
        // loop through array and add to task queue
        for (int i = 0; i < tasks.size(); i++) {
            // fully populate with size tasks, each task should say what digit to compute
            queue.add(tasks.get(i));
        }
    }

    public synchronized boolean isEmpty() {
        return queue.isEmpty();
    }

    public synchronized Task pull() {
        return queue.poll();
    }
}
import java.util.*;


// This hash table must be protected against race conditions.
// This is a shared resource available to all worker threads,
    // it must be protected against race conditions.
    // Pass a reference to the hashtable via the worker thread's constructor
        // (not a global variable).
public class ResultTable {
    private HashMap results;
    // constuctor
    public ResultTable(int size) {
        // Use a Java HashMap as the underlying data structure.
            // Use aggregation, rather than inheritance.
        results = new HashMap<>(size);
    }

    public synchronized Object getValue(int i) {
        return results.get((Integer) i);
    }

    public synchronized int getSize() {
        return results.size();
    }

    public synchronized void insert(int key, int value) {
        results.put((Integer) key, (Integer) value);
    }
}

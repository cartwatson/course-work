/**
 * @author Carter Watson A02312565@usu.edu
 */
public class WorkerThread implements Runnable{
    private Task task = null;
    private TaskQueue taskQueue;
    private ResultTable resultTable;

    // constructor
    // TODO: pass queue and result table by reference
    public WorkerThread(TaskQueue q, ResultTable rt) {
        taskQueue = q;
        resultTable = rt; 
    }

    @Override
    public void run() {
        while (!taskQueue.isEmpty()) {
            task = taskQueue.pull();
            int result = task.getResult();
            int digit = task.getDigit();
            resultTable.insert(digit, result);
        }
    }
}

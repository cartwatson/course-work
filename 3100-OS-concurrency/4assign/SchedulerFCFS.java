import java.util.ArrayList;

public class SchedulerFCFS extends SchedulerBase implements Scheduler {
    // class variables
    private Platform platform;
    private ArrayList<Process> processes = new ArrayList<Process>();

    // constructor
    public SchedulerFCFS(Platform platform) {
        this.platform = platform;
    }

    // methods
    public void notifyNewProcess(Process p) {
        // add process to end of list
        processes.add(p);
    }

    public Process update(Process cpu) {
        // start of program, throw out first process
        if (cpu == null) { return getNext(); }

        // burst complete
        if (cpu.isBurstComplete()) {
            platform.log(" Process " + cpu.getName() + " burst complete");

            // take completed burst process off queue
            Process curr = processes.remove(0);
            contextSwitches++; // increment context switch
            
            // execution is compelete
            if (cpu.isExecutionComplete()) { platform.log(" Process " + cpu.getName() + " execution complete"); }
            // only re-add process to queue if process is not completed
            else { processes.add(curr); }
            
            // grab next process or return null
            return getNext();
        }
        return cpu;
    }

    private Process getNext() {
        // null check
        if (processes.isEmpty()) { return null; }

        // get next from list
        Process next = processes.get(0);
        contextSwitches++; // increment context switch
        platform.log(" Scheduled: " + next.getName());
        return next;
    }
}

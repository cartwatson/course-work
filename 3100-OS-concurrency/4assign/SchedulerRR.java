import java.util.ArrayList;

public class SchedulerRR extends SchedulerBase implements Scheduler {
    // class variables
    private Platform platform;
    private int timeQuantum;
    private ArrayList<Process> processes = new ArrayList<Process>();

    // constructor
    public SchedulerRR(Platform platform, int timeQuantum) {
        this.platform = platform;
        this.timeQuantum = timeQuantum;
    }

    // methods
    public void notifyNewProcess(Process p) {
        // add process to end of list
        processes.add(p);
    }

    public Process update(Process cpu) {
        // start of program, throw out first process
        if (cpu == null) { return getNext(); }

        if (cpu.isExecutionComplete()) {
            platform.log(" Process " + cpu.getName() + " execution complete");
            
            // remove from queue
            processes.remove(0);
            contextSwitches++;

            // grab next process or return null
            return getNext();
        }

        // if time quantum is up
        if (cpu.getElapsedBurst() % timeQuantum == 0) {
            platform.log(" Time Quantum complete for process " + cpu.getName());

            // take completed burst process off queue
            Process temp = processes.remove(0);
            contextSwitches++; // increment context switch

            // re-add because it's not done
            processes.add(temp);

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

import java.util.ArrayList;

public class SchedulerSRTF extends SchedulerBase implements Scheduler {
    // class variables
    private Platform platform;
    private ArrayList<Process> processes = new ArrayList<Process>();

    // constructor
    public SchedulerSRTF(Platform platform) {
        this.platform = platform;
    }

    // methods
    public void notifyNewProcess(Process p) {
        addToProcesses(p);
    }

    public Process update(Process cpu) {
        // start of program, throw out first process
        if (cpu == null) { return getNext(); }

        // preemtive removal
        if (processes.get(0) != cpu) {
            platform.log(" Preemptively removed: " + cpu.getName());
            processes.remove(cpu);
            contextSwitches++;

            // add back to queue and sort it's place
            addToProcesses(cpu);

            return getNext();
        }

        // burst complete
        if (cpu.isBurstComplete()) {
            platform.log(" Process " + cpu.getName() + " burst complete");

            // take completed burst process off queue
            Process temp = processes.remove(0);
            contextSwitches++; // increment context switch
            
            // execution is compelete
            if (cpu.isExecutionComplete()) { platform.log(" Process " + cpu.getName() + " execution complete"); }
            // only re-add process to queue if process is not completed
            else { processes.add(temp); }
            
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

    private void addToProcesses(Process p) {
        // first process added
        if (processes.isEmpty()) { processes.add(p); return; }

        // find process' place in queue
        for (int i = 0; i < processes.size(); i++) {
            // get remaining time of each process
            int iTR = processes.get(i).getTotalTime() - processes.get(i).getElapsedTotal();
            int pTR = p.getTotalTime() - p.getElapsedTotal();

            if (iTR > pTR) { processes.add(i, p); return; }
        }

        // longest remaining time, add at end
        processes.add(p);
    }
}

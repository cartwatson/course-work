public class TaskFIFO {
    private final int[] sequence;
    private final int maxMemoryFrames; // never used but needed for constructor as per assign desc
    private final int maxPageReference;
    private int pageFault = 0;

    public TaskFIFO (int[] sequence, int maxMemoryFrames, int maxPageReference) {
        this.sequence = sequence;
        this.maxMemoryFrames = maxMemoryFrames;
        this.maxPageReference = maxPageReference;
    }

    public int run() {
        // init sequence ref
        int[] sequenceReference = new int [maxPageReference];

        for (int i = 0; i < maxPageReference; i++) {
            sequenceReference[i] = i;
        }

        // run
        for (int i = 0; i < maxPageReference; i++) {
            boolean hit = false;

            for (int k : sequence) {
                if (k == sequenceReference[i]) {
                    hit = true;
                    break;
                }
            }

            if (!hit) {
                int count;
                for (count = 0; count < sequence.length - 1; count++) {
                    sequence[count] = sequence[count+1];
                }
                sequence[count] = sequenceReference[i];
                pageFault++;
            }
        }
        return pageFault;
    }
}

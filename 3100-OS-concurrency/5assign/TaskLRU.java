public class TaskLRU {
    private final int[] sequence;
    private final int maxMemoryFrames;
    private final int maxPageReference;
    private int pageFault = 0;

    public TaskLRU (int[] sequence, int maxMemoryFrames, int maxPageReference) {
        this.sequence = sequence;
        this.maxMemoryFrames = maxMemoryFrames;
        this.maxPageReference = maxPageReference;
    }

    public int run() {
        // init sequence ref and LRU
        int[] LRU = new int[maxPageReference];
        int[] sequenceReference = new int[maxPageReference];

        for (int i = 0; i < maxPageReference; i++) {
            sequenceReference[i] = Integer.MIN_VALUE;
        }

        // run
        for (int i = 0; i < maxPageReference; i++) {
            int hit = 0;
            for (int j = 0; j < maxMemoryFrames; j++) {
                if (sequence[j] == sequenceReference[i]) {
                    hit = 1;
                    break;
                }
            }

            if (hit == 0) {
                for (int j = 0; j < maxMemoryFrames; j++) {
                    boolean cap = false;
                    int currentPage = sequence[j];

                    for (int k = i; k < maxPageReference; k++) {
                        if (currentPage == sequenceReference[k]) {
                            LRU[j] = k;
                            cap = true;
                            break;
                        }
                    }

                    if (!cap) {
                        LRU[j] = Integer.MIN_VALUE;
                    }
                }
                int maximum = Integer.MAX_VALUE;
                int match = 0;

                for (int j = 0; j < maxMemoryFrames; j++) {
                    if (LRU[j] < maximum) {
                        maximum = LRU[j];
                        match = j;
                    }
                }
                sequence[match] = sequenceReference[i];
                pageFault++;
            }
        }
        return pageFault;
    }
}

public class TaskMRU {
    private final int[] sequence;
    private final int maxMemoryFrames;
    private final int maxPageReference;
    private int pageFault = 0;

    public TaskMRU (int[] sequence, int maxMemoryFrames, int maxPageReference) {
        this.sequence = sequence;
        this.maxMemoryFrames = maxMemoryFrames;
        this.maxPageReference = maxPageReference;
    }

    public int run() {
        // init sequence ref and MRU
        int[] MRU = new int[maxPageReference];
        int[] sequenceReference = new int[maxPageReference];

        for (int i = 0; i < maxPageReference; i++) {
            sequenceReference[i] = Integer.MAX_VALUE;
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
                for (int j = 0; j < maxPageReference; j++) {
                    boolean cap = false;
                    int currentPage = sequence[j];

                    for (int k = i; k < maxPageReference; k++) {
                        if (currentPage == sequenceReference[k]) {
                            MRU[j] = k;
                            cap = true;
                            break;
                        }
                    }

                    if (!cap) {
                        MRU[j] = Integer.MAX_VALUE;
                    }
                }
                int maximum = Integer.MIN_VALUE;
                int match = 0;

                for (int j = 0; j < maxMemoryFrames; j++) {
                    if (MRU[j] >= maximum) {
                        maximum = MRU[j];
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

public class Task {
    private int digitToCompute;
    private int result;

    // constructor
    public Task(int digit) {
        digitToCompute = digit;
    }

    public int getDigit() {
        return this.digitToCompute;
    }

    public int getResult() {
        Bpp bpp = new Bpp();
        // compute & return result
        this.result = bpp.getDecimal(digitToCompute);
        return this.result;
    }
}

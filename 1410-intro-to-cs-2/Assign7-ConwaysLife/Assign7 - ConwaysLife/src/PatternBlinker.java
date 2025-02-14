public class PatternBlinker extends Pattern {
    //1x3 line
    private boolean[][] blinker;

    public PatternBlinker() {
        blinker = new boolean[3][3];
        blinker[1][0] = true;
        blinker[1][1] = true;
        blinker[1][2] = true;
    }

    public int getSizeX() {
        return 3;
    }

    public int getSizeY() {
        return 3;
    }

    public boolean getCell(int x, int y) {
        return blinker[x][y];
    }
}

public class PatternBlock extends Pattern {
    //2x2 square
    private boolean[][] block;

    public PatternBlock() {
        block = new boolean[2][2];
        block[0][0] = true;
        block[0][1] = true;
        block[1][0] = true;
        block[1][1] = true;
    }

    public int getSizeX() {
        return 2;
    }

    public int getSizeY() {
        return 2;
    }

    public boolean getCell(int x, int y) {
        return block[x][y];
    }
}

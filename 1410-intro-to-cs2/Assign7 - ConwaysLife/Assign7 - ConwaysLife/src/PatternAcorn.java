public class PatternAcorn extends Pattern {
    //its an "acorn"
    private boolean[][] acorn;

    public PatternAcorn() {
        acorn = new boolean[7][3];
        acorn[0][2] = true;
        acorn[1][0] = true;
        acorn[1][2] = true;
        acorn[3][1] = true;
        acorn[4][2] = true;
        acorn[5][2] = true;
        acorn[6][2] = true;
    }

    public int getSizeX() {
        return 7;
    }

    public int getSizeY() {
        return 3;
    }

    public boolean getCell(int x, int y) {
        return acorn[x][y];
    }
}

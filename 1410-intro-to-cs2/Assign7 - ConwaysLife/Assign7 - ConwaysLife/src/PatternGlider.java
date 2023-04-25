public class PatternGlider extends Pattern {
        //funky glider
        private boolean[][] glider;

        public PatternGlider() {
            glider = new boolean[3][3];
            glider[0][1] = true;
            glider[1][2] = true;
            glider[2][0] = true;
            glider[2][1] = true;
            glider[2][2] = true;
        }

        public int getSizeX() {
            return 3;
        }

        public int getSizeY() {
            return 3;
        }

        public boolean getCell(int x, int y) {
            return glider[x][y];
        }
}

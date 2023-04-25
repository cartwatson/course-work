public class LifeSimulator {
    //variables
    private int sizeX;
    private int sizeY;
    private boolean[][] grid;

    //methods
    public LifeSimulator(int sizeXParameter, int sizeYParameter) {
        sizeX = sizeXParameter;
        sizeY = sizeYParameter;
        grid = new boolean[sizeX][sizeY];
    }

    public int getSizeX() {
        //return size of world
        return sizeX;
    }

    public int getSizeY() {
        //return size of world
        return sizeY;
    }

    public boolean getCell(int x, int y) {
        //returns true if the cell is alive
        return grid[x][y];
    }

    public void insertPattern(Pattern pattern, int startX, int startY) {
        //Adds the pattern to the world, with the upper left corner beginning at startX and startY.
        for (int i = 0; i < pattern.getSizeX(); i++) {
            for (int j = 0; j < pattern.getSizeY(); j++) {
                 if (pattern.getCell(i, j)) {
                     grid[i + startX][j + startY] = true;
                 }
            }
        }
    }

    public void update() {
        //Performs a single step update of the world, following the four rules specified in the wiki article
        //Make a new grid (array) that is the same size as the current grid
        boolean[][] temp;
        temp = new boolean[sizeX][sizeY];
        //For each cell in the original grid, use the 4 rules to decide the state of that cell in the updated grid.
            //two or three neighbors -- lives
            //dead with three -- lives
            //all else dies
            //loop to count neighbors
            //switch statement to decide what happens
        //check each cell in grid
        for (int i = 0; i < getSizeX(); i++) {
            for (int j = 0; j < getSizeY(); j++) {
                //check neighbors of that cells
                int neighbors = 0;
                boolean checked = false;
                //CHECK OUT OF BOUNDS
                //top left corner
                if (i == 0 && j == 0) {
                    checked = true;
                    if (grid[i][j+1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j]) {
                        neighbors++;
                    }
                    if (grid[i+1][j+1]) {
                        neighbors++;
                    }
                }
                //bottom left corner
                if (i == 0 && j == (getSizeY() - 1) && !checked) {
                    checked = true;
                    if (grid[i][j-1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j-1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j]) {
                        neighbors++;
                    }
                }
                //top right corner
                if (j == 0 && i == (getSizeX() - 1) && !checked) {
                    checked = true;
                    if (grid[i-1][j]) {
                        neighbors++;
                    }
                    if (grid[i-1][j+1]) {
                        neighbors++;
                    }
                    if (grid[i][j+1]) {
                        neighbors++;
                    }
                }
                //bottom right corner
                if (i == (getSizeX() - 1) && j == (getSizeY() - 1) && !checked) {
                    checked = true;
                    if (grid[i-1][j-1]) {
                        neighbors++;
                    }
                    if (grid[i-1][j]) {
                        neighbors++;
                    }
                    if (grid[i][j-1]) {
                        neighbors++;
                    }
                }
                //left wall
                if (i == 0 && !checked) {
                    checked = true;
                    if (grid[i][j-1]) {
                        neighbors++;
                    }
                    if (grid[i][j+1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j-1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j]) {
                        neighbors++;
                    }
                    if (grid[i+1][j+1]) {
                        neighbors++;
                    }
                }
                //ceiling
                if (j == 0 && !checked) {
                    checked = true;
                    if (grid[i-1][j]) {
                        neighbors++;
                    }
                    if (grid[i-1][j+1]) {
                        neighbors++;
                    }
                    if (grid[i][j+1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j]) {
                        neighbors++;
                    }
                    if (grid[i+1][j+1]) {
                        neighbors++;
                    }
                }
                //right wall
                if (i == (getSizeX() - 1) && !checked) {
                    checked = true;
                    if (grid[i-1][j-1]) {
                        neighbors++;
                    }
                    if (grid[i-1][j]) {
                        neighbors++;
                    }
                    if (grid[i-1][j+1]) {
                        neighbors++;
                    }
                    if (grid[i][j-1]) {
                        neighbors++;
                    }
                    if (grid[i][j+1]) {
                        neighbors++;
                    }
                }
                //floor
                if (j == (getSizeY() - 1) && !checked) {
                    checked = true;
                    if (grid[i - 1][j - 1]) {
                        neighbors++;
                    }
                    if (grid[i - 1][j]) {
                        neighbors++;
                    }
                    if (grid[i][j - 1]) {
                        neighbors++;
                    }
                    if (grid[i + 1][j - 1]) {
                        neighbors++;
                    }
                    if (grid[i + 1][j]) {
                        neighbors++;
                    }
                }
                //middle
                if (!checked) {
                    if (grid[i-1][j-1]) {
                        neighbors++;
                    }
                    if (grid[i-1][j]) {
                        neighbors++;
                    }
                    if (grid[i-1][j+1]) {
                        neighbors++;
                    }
                    if (grid[i][j-1]) {
                        neighbors++;
                    }
                    if (grid[i][j+1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j-1]) {
                        neighbors++;
                    }
                    if (grid[i+1][j]) {
                        neighbors++;
                    }
                    if (grid[i+1][j+1]) {
                        neighbors++;
                    }
                }

                boolean assigned = false;
                //testing
                //if cell is alive and has 2 or 3 neighbors, updated cell lives
                if (grid[i][j] && (neighbors == 2 || neighbors == 3)) {
                    temp[i][j] = true;
                    assigned = true;
                }
                //if cell is dead and has 3 neighbors, updated cell lives
                if (!grid[i][j] && neighbors == 3) {
                    temp[i][j] = true;
                    assigned = true;
                }
                //if neither of these cases are met cell is dead
                if (!assigned) {
                    temp[i][j] = false;
                }
            }
        }
        //When finished set the reference of 'original' to refer to the 'updated' grid.
        grid = temp;
    }
}
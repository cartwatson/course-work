public class Recursion {
    public static void main(String[] args) {

        int[] sumMe = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        System.out.printf("Array Sum: %d\n", arraySum(sumMe, 0));

        int[] minMe = { 0, 1, 1, 2, 3, 5, 8, -42, 13, 21, 34, 55, 89 };
        System.out.printf("Array Min: %d\n", arrayMin(minMe, 0));

        String[] amISymmetric =  {
                "You can cage a swallow can't you but you can't swallow a cage can you",
                "I still say cS 1410 is my favorite class"
        };
        for (String test : amISymmetric) {
            String[] words = test.toLowerCase().split(" ");
            System.out.println();
            System.out.println(test);
            System.out.printf("Is word symmetric: %b\n", isWordSymmetric(words, 0, words.length - 1));
        }

        double[][] weights = {
                { 51.18 },
                { 55.90, 131.25 },
                { 69.05, 133.66, 132.82 },
                { 53.43, 139.61, 134.06, 121.63 }
        };

        System.out.println();
        System.out.println("--- Weight Pyramid ---");
        for (int row = 0; row < weights.length; row++) {
            for (int column = 0; column < weights[row].length; column++) {
                double weight = computePyramidWeights(weights, row, column);
                System.out.printf("%.2f ", weight);
            }
            System.out.println();
        }

        char[][] image = {
                {'*','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ','*','*',' ',' '},
                {' ','*',' ',' ','*','*','*',' ',' ',' '},
                {' ','*','*',' ','*',' ','*',' ','*',' '},
                {' ','*','*',' ','*','*','*','*','*','*'},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ','*','*','*',' ',' ','*',' '},
                {' ',' ',' ',' ',' ','*',' ',' ','*',' '}
        };
        int howMany = howManyOrganisms(image);
        System.out.println();
        System.out.println("--- Labeled Organism Image ---");
        for (char[] line : image) {
            for (char item : line) {
                System.out.print(item);
            }
            System.out.println();
        }
        System.out.printf("There are %d organisms in the image.\n", howMany);

    }

    public static boolean isWordSymmetric(String[] words, int start, int end) {
        //word symmetry
        boolean wordsEqual = true;
        for (; start < end; start++, end--) {
            //make strings lowercase
            String startLower = words[start].toLowerCase();
            String endLower = words[end].toLowerCase();
            //evaluate
            if (startLower.equals(endLower)) {
                wordsEqual = true;
            } else {
                wordsEqual = false;
            }
            //if words are false immediately break
            if (!wordsEqual) {
                break;
            }
        }
        //return boolean wordsEqual
        return wordsEqual;
    }

    public static long arraySum(int[] data, int position) {
        //Write a recursive method that returns the total of all elements in the array.
        //set sum to zero
        long sum = 0;
        //add all values from array
        for (; position < data.length; position++) {
            sum += data[position];
        }
        //return sum
        return sum;
    }

    public static int arrayMin(int[] data, int position) {
        //write a recursive function that returns the minimum value of the elements in the array.
        //initialize i, set minimum to first data piece, increment i
        int min = data[position];
        position++;
        //loop through array
        for (; position < data.length; position++) {
            //if next int in array is smaller, make it the new value of min
            if (data[position] < min) {
                min = data[position];
            }
        }
        //return minimum
        return min;
    }

    public static double computePyramidWeights(double[][] weights, int row, int column) {
        //create temp array to work in
        double[][] newWeights;
        newWeights = new double [weights.length][weights.length];
        for (int i = 0; i < weights.length; i++) {
            System.arraycopy(weights[i], 0, newWeights[i], 0, weights[i].length);
        }

        //check for appropriate lengths and row and column values
        if (!(0 > row) && row < weights.length && !(0 > column) && column < weights[row].length) {
            //calculate every value
            for (int lRow = 0; lRow < weights.length; lRow++) {
                for (int lColumn = 0; lColumn < weights[lRow].length; lColumn++) {
                    //initialize weight's value
                    double weight = newWeights[lRow][lColumn];
                    //do NOT calculate top row
                    if (lRow > 0) {
                        //calculate new weight----two above it (same column and one to the left)
                        boolean calculated = false;
                        //left edge
                        if (lColumn == 0) {
                            calculated = true;
                            weight += (newWeights[lRow - 1][lColumn] / 2);
                        }
                        //right edge
                        if (lColumn == weights[lRow].length - 1 && !calculated) {
                            calculated = true;
                            weight += (newWeights[lRow - 1][lColumn - 1] / 2);
                        }
                        //middle
                        if (lColumn != 0 && lColumn != weights[lRow].length - 1 && !calculated) {
                            weight += (newWeights[lRow - 1][lColumn - 1] / 2);
                            weight += (newWeights[lRow - 1][lColumn] / 2);
                        }
                    }

                    //assign new weight to value
                    newWeights[lRow][lColumn] = weight;
                } //for lColumn
            } //for lRow

            //return value needed
            return newWeights[row][column];
        } else {
            //if indexes are wrong, return zero
            return 0.0;
        }
    }

    public static int howManyOrganisms(char[][] image) {
        //Given a 2d array of characters, where an asterisk (*) marks a non-empty cell.  An organism is defined as all cells connected directly to other cells in the up/down/left/right (not diagonal) directions
        int numOrganisms = 0;
        for (int i = 0; i < image.length; i++) {
            for (int j = 0; j < image[i].length; j++) {
                if (image[i][j] == '*') {
                    //cell alive
                    image = organismFinder(image, i, j, numOrganisms);
                    //if new organism increase counter
                    if (image[i][j] > (char)(numOrganisms + 96)) {
                        numOrganisms++;
                    }
                }
            }
        }
        return numOrganisms;
    }

    public static char[][] organismFinder(char[][] image, int row, int column, int numberFound) {
        //initialize booleans
        boolean checked;
        boolean organismFound;
        //reset booleans
        boolean foundAbove = false;
        boolean foundRight = false;
        boolean foundBelow = false;
        boolean foundLeft = false;
        checked = false;
        organismFound = false;
        //------------------------------checks------------------------------\\
        {
        //single celled
        if (row == 0 && row == image.length - 1 && column == 0 && column == image[row].length - 1) {
            checked = true;
            //do nothing
        }

        //left and right wall check
        if (column == 0 && column == image[row].length - 1 && !checked) {
            checked = true;
            //up check
            if (!(column >= image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
            //down check
            if (!(column >= image[row + 1].length - 1)) {
                if (image[row + 1][column] != ' ') {
                    if (image[row + 1][column] == '*') {
                        //asterisk
                        foundBelow = true;
                    } else {
                        //letter
                        image[row][column] = image[row + 1][column];
                        organismFound = true;
                    }
                }
            }
        }

        //top left corner
        if (row == 0 && column == 0 && !checked) {
            checked = true;
            //right check
            if (image[row][column + 1] != ' ') {
                if (image[row][column + 1] == '*') {
                    //asterisk
                    foundRight = true;
                } else {
                    //letter
                    image[row][column] = image[row][column + 1];
                    organismFound = true;
                }
            }
            //down check
            if (image.length != 1 ) {
                if (!(column >= image[row + 1].length - 1)) {
                    if (image[row + 1][column] != ' ') {
                        if (image[row + 1][column] == '*') {
                            //asterisk
                            foundBelow = true;
                        } else {
                            //letter
                            image[row][column] = image[row + 1][column];
                            organismFound = true;
                        }
                    }
                }
            }
        }

        //top right corner
        if (row == 0 && column == (image[row].length - 1) && !checked) {
            checked = true;
            //down check
            if (!(column >= image[row + 1].length - 1)) {
                if (image[row + 1][column] != ' ') {
                    if (image[row + 1][column] == '*') {
                        //asterisk
                        foundBelow = true;
                    } else {
                        //letter
                        image[row][column] = image[row + 1][column];
                        organismFound = true;
                    }
                }
            }
            //left check
            if (image[row][column - 1] != ' ') {
                if (image[row][column - 1] == '*') {
                    //asterisk
                    foundLeft = true;
                } else {
                    //letter
                    image[row][column] = image[row][column - 1];
                    organismFound = true;
                }
            }
        }

        //bottom left corner
        if (row == (image.length - 1) && column == 0 && !checked) {
            checked = true;
            //up check
            if (!(column >= image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
            //right check
            if (image[row][column + 1] != ' ') {
                if (image[row][column + 1] == '*') {
                    //asterisk
                    foundRight = true;
                } else {
                    //letter
                    image[row][column] = image[row][column + 1];
                    organismFound = true;
                }
            }
        }

        //bottom right corner
        if (row == (image.length - 1) && column == (image[row].length - 1) && !checked) {
            checked = true;
            //left check
            if (image[row][column - 1] != ' ') {
                if (image[row][column - 1] == '*') {
                    //asterisk
                    foundLeft = true;
                } else {
                    //letter
                    image[row][column] = image[row][column - 1];
                    organismFound = true;
                }
            }
            //up check
            if (!(column >= image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
        }

        //ceiling
        if (row == 0 && !checked) {
            checked = true;
            //right check
            if (image[row][column + 1] != ' ') {
                if (image[row][column + 1] == '*') {
                    //asterisk
                    foundRight = true;
                } else {
                    //letter
                    image[row][column] = image[row][column + 1];
                    organismFound = true;
                }
            }
            //down check
            if (!(column >= image[row + 1].length - 1)) {
                if (image[row + 1][column] != ' ') {
                    if (image[row + 1][column] == '*') {
                        //asterisk
                        foundBelow = true;
                    } else {
                        //letter
                        image[row][column] = image[row + 1][column];
                        organismFound = true;
                    }
                }
            }
            //left check
            if (image[row][column - 1] != ' ') {
                if (image[row][column - 1] == '*') {
                    //asterisk
                    foundLeft = true;
                } else {
                    //letter
                    image[row][column] = image[row][column - 1];
                    organismFound = true;
                }
            }
        }

        //left wall
        if (column == 0 && !checked) {
            checked = true;
            //up check
            if (!(column >= image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
            //right check
            if (image[row][column + 1] != ' ') {
                if (image[row][column + 1] == '*') {
                    //asterisk
                    foundRight = true;
                } else {
                    //letter
                    image[row][column] = image[row][column + 1];
                    organismFound = true;
                }
            }
            //down check
            if (!(column >= image[row + 1].length - 1)) {
                if (image[row + 1][column] != ' ') {
                    if (image[row + 1][column] == '*') {
                        //asterisk
                        foundBelow = true;
                    } else {
                        //letter
                        image[row][column] = image[row + 1][column];
                        organismFound = true;
                    }
                }
            }
        }

        //floor
        if (row == (image.length - 1) && !checked) {
            checked = true;
            //right check
            if (image[row][column + 1] != ' ') {
                if (image[row][column + 1] == '*') {
                    //asterisk
                    foundRight = true;
                } else {
                    //letter
                    image[row][column] = image[row][column + 1];
                    organismFound = true;
                }
            }
            //left check
            if (image[row][column - 1] != ' ') {
                if (image[row][column - 1] == '*') {
                    //asterisk
                    foundLeft = true;
                } else {
                    //letter
                    image[row][column] = image[row][column - 1];
                    organismFound = true;
                }
            }
            //up check
            if (!(column >= image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
        }

        //right wall
        if (column == (image[row].length - 1) && !checked) {
            checked = true;
            //down check
            if (!(column >= image[row + 1].length - 1)) {
                if (image[row + 1][column] != ' ') {
                    if (image[row + 1][column] == '*') {
                        //asterisk
                        foundBelow = true;
                    } else {
                        //letter
                        image[row][column] = image[row + 1][column];
                        organismFound = true;
                    }
                }
            }
            //left check
            if (image[row][column - 1] != ' ') {
                if (image[row][column - 1] == '*') {
                    //asterisk
                    foundLeft = true;
                } else {
                    //letter
                    image[row][column] = image[row][column - 1];
                    organismFound = true;
                }
            }
            //up check
            if (!(column > image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
        }

        //middle
        if (!checked) {
            //right check
                if (image[row][column + 1] != ' ') {
                    if (image[row][column + 1] == '*') {
                        //asterisk
                        foundRight = true;
                    } else {
                        //letter
                        image[row][column] = image[row][column + 1];
                        organismFound = true;
                    }
                }
            //down check
            if (!(column >= image[row + 1].length - 1)) {
                if (image[row + 1][column] != ' ') {
                    if (image[row + 1][column] == '*') {
                        //asterisk
                        foundBelow = true;
                    } else {
                        //letter
                        image[row][column] = image[row + 1][column];
                        organismFound = true;
                    }
                }
            }
            //left check
            if (image[row][column - 1] != ' ') {
                if (image[row][column - 1] == '*') {
                    //asterisk
                    foundLeft = true;
                } else {
                    //letter
                    image[row][column] = image[row][column - 1];
                    organismFound = true;
                }
            }
            //up check
            if (!(column >= image[row - 1].length - 1)) {
                if (image[row - 1][column] != ' ') {
                    if (image[row - 1][column] == '*') {
                        //asterisk
                        foundAbove = true;
                    } else {
                        //letter
                        image[row][column] = image[row - 1][column];
                        organismFound = true;
                    }
                }
            }
        }
        }
        //----------------------------checks end----------------------------\\

        //new organism
        if (!organismFound) {
            image[row][column] = (char) (numberFound + 97);
        }

        //adjust for next loop as organism was found
        if (foundAbove) {
            //run checks again adjusted for above
            image = organismFinder(image, row - 1, column, numberFound);
        }

        if (foundRight) {
            //run checks again adjusted for right
            image = organismFinder(image, row, column + 1, numberFound);
        }

        if (foundBelow) {
            //run checks again adjusted for below
            image = organismFinder(image, row + 1, column, numberFound);
        }

        if (foundLeft) {
            //run checks again adjusted for left
            image = organismFinder(image, row, column - 1, numberFound);
        }

    return image;
    }

}

package com.company;

import java.util.Scanner;

public class Pyramid1 {

    public static void main(String[] args) {
        //get input from user
        Scanner input = new Scanner(System.in);
        //prompt user
        System.out.print("Enter the number of lines: ");
        //get input
        String lineNumber = input.nextLine();

        //determine spacing for each number by longest digit
        int digitLength = lineNumber.length() + 1;

        //convert lineNumber to int
        int lineNumberInt = Integer.parseInt(lineNumber);

        //initialize variable
        //assemble format string for printing
        String format = "%" + digitLength + "d";
        String spacer = "%" + digitLength + "s";
        //create pyramid
        for (int i = 1; i < (lineNumberInt + 1); i++) {
            //generate line
            //determine amount of space before numbers
            int numberOfColumns = lineNumberInt - i;
            for (int j = 1; j < (numberOfColumns + 1); j++) {
                System.out.printf(spacer, "");
            }
            //print numbers
            for (int k = i; k > 0; k--) {
                System.out.printf(format, k);
            }
            //print last half of numbers
            for (int k = 2; k < (i + 1); k++) {
                System.out.printf(format, k);
            }

            //new line
            System.out.println();
        }
    }
}

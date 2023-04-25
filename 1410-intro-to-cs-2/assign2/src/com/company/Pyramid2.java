package com.company;

import java.util.Scanner;
import java.lang.Math;

public class Pyramid2 {

    public static void main(String[] args) {
        //get input from user
        Scanner input = new Scanner(System.in);
        //prompt user
        System.out.print("Enter the number of lines: ");
        //get input
        String lineNumber = input.nextLine();

        //convert lineNumber to int
        int lineNumberInt = Integer.parseInt(lineNumber);

        //determine spacing for each number by longest digit
        String largestDigit = Integer.toString((int) Math.pow(2, lineNumberInt));
        int digitLength = largestDigit.length() + 1;

        //initialize variable
        //assemble format string for printing
        String format = "%" + digitLength + ".0f";
        String spacer = "%" + digitLength + "s";
        //create pyramid
        for (int i = 0; i < lineNumberInt; i++) {
            //generate line
            //determine amount of space before numbers
            int numberOfColumns = lineNumberInt - i;
            for (int j = 1; j < (numberOfColumns + 1); j++) {
                System.out.printf(spacer, "");
            }
            //print numbers
            for (int k = 0; k < (i + 1); k++) {
                System.out.printf(format, java.lang.Math.pow(2, k));
            }
            //print last half of numbers
            for (int k = i - 1; k > -1; k--) {
                System.out.printf(format, java.lang.Math.pow(2, k));
            }
            //new line
            System.out.println();
        }
    }
}
package com.company;

import java.util.Scanner;

public class ISBN {

    public static void main(String[] args) {
        // set up scanner for input
        Scanner input = new Scanner(System.in);

        //get ISBN from user via scanner
        System.out.print("Enter the first 9 digits of an ISBN: ");
        int ISBNumber = input.nextInt();

        //separate values
        int d1 = ISBNumber / 100000000;
        int n1 = ISBNumber - d1 * 100000000;
        int d2 = n1 / 10000000;
        int n2 = n1 - d2 * 10000000;
        int d3 = n2 / 1000000;
        int n3 = n2 - d3 * 1000000;
        int d4 = n3 / 100000;
        int n4 = n3 - d4 * 100000;
        int d5 = n4 / 10000;
        int n5 = n4 - d5 * 10000;
        int d6 = n5 / 1000;
        int n6 = n5 - d6 * 1000;
        int d7 = n6 / 100;
        int n7 = n6 - d7 * 100;
        int d8 = n7 / 10;
        int d9 = n7 - d8 * 10;

        //do the check
        int checksum = (d1 + d2*2 + d3*3 + d4*4 + d5*5 + d6*6 + d7*7 + d8*8 + d9*9) % 11;

        //print full ISBN-10
        //print start of message
        System.out.print("The ISBN-10 number is: ");
        //check for leading zeros on all digits
        //check first digit
        if (d1 == 0) {
            //print zero to pad ISBN
            System.out.print("0");
            //check second digit
            if (d2 == 0) {
                System.out.print("0");
                //check third digit
                if (d3 == 0) {
                    System.out.print("0");
                    //check fourth digit
                    if (d4 == 0) {
                        System.out.print("0");
                        //check fifth digit
                        if (d5 == 0) {
                            System.out.print("0");
                            //check sixth digit
                            if (d6 == 0) {
                                System.out.print("0");
                                //check seventh digit
                                if (d7 == 0) {
                                    System.out.print("0");
                                    //check eighth digit
                                    if (d8 == 0) {
                                        System.out.print("0");
                                        //check ninth digit
                                        if (d9 == 0) {
                                            System.out.print("0");
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        //print ISBN-9
        System.out.print(ISBNumber);
        //add X instead of ten if checksum == 10
        if (checksum == 10)
        {
            System.out.println("X");
        } else {
            System.out.println(checksum);
        }
    }
}
package com.company;
import java.util.Scanner;
import java.lang.Math;

public class Quadratic {

    public static void main(String[] args) {
	    // initialize variables for quadratic equation
        double a;
        double b;
        double c;
        // variables for roots
        double d;
        double e;

        //assign values of a, b, c from user input
        Scanner input = new Scanner(System.in);
        //assign value for a
        System.out.print("Enter 'a': ");
        a = input.nextFloat();
        //assign value for b
        System.out.print("Enter 'b': ");
        b = input.nextFloat();
        //assign value for c
        System.out.print("Enter 'c': ");
        c = input.nextFloat();

        //do calculations
        //declare variable to simplify 'math.sqrt()'
        double v = b * b - 4 * a * c;
        d = ((-1 * b) + Math.sqrt(v)) / (2 * a);
        e = ((-1 * b) - Math.sqrt(v)) / (2 * a);

        //print results
        if (v > 0) {
            System.out.println("There are two roots for the quadratic equation with these coefficients.");
            System.out.print("r1 = ");
            System.out.println(d);
            System.out.print("r2 = ");
            System.out.println(e);
        }
        if (v == 0) {
            System.out.println("There is one root for the quadratic equation with these coefficients.");
            System.out.print("r1 = ");
            System.out.println(d);
        }
        if (v < 0) {
            System.out.println("There are no roots for the quadratic equation with these coefficients.");
        }
    }
}

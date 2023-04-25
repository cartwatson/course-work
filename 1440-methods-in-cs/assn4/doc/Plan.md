# 0.  From Problem Analysis to Data Definitions

The problem with this code is not that the program has incorrect output
but instead that the code is badly written.  Errors need to be spotted  
visually and corrected after all have been found.

A list of code smells found will be documented, and a user manual created.

Program will be updated to OOP standards, modules will become classes.

Program will be easier to expand upon later if necessary.

# 1.  System Analysis

The program gets a command line argument from the user that decides what  
fractal to print and what palette to use, if neither are specified it  
will use the default for both, if no palette is specified it will use  
default.

Output is in a TK window, it will be an image.

All formulas for image generation should be created and working at this
point.

# 2.  Functional Examples

Input will come in as command line arguments from the user.

If any incorrect command line input is given, program will describe the
problem to the user and provide a list of valid inputs.

Program will run exclusively from main.py when completed.

# 3.  Function Template

The program is given in a working condition.

# 4.  Implementation

Fractal parent class and three subclasses created.

Palette parent class and two subclasses created.

ImagePainter and main in class format.

# 5.  Testing

run src/runTests.py
Verify that fractals are generated correctly from mandelbrot and julia.
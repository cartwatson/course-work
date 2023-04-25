# CS 1440 Assignment 4.1 Instructions

## Overview

After successfully refactoring your client's program into a form which is
easier to work on and think about, you are ready to take this program to the
next level.  In this sprint you will apply the [Factory
Method](https://sourcemaking.com/design_patterns/factory_method) design pattern
to your code.  Through judicious use of this design pattern your program will
evolve from being merely maintainable to easily extensible.  A little bit of
planning and energy spent now will set the stage for many years of smooth
maintenance in the future.


## Objectives

-   Re-organize modules into Polymorphic (duck typed) classes with Inheritance
    -   Take advantage of code reuse
-   Use Factory Methods to easily make fractal & palette objects
-   Implement hard-coded default behaviors which may be overridden by user
-   Documentation (UML, manual, etc.) from previous assignment is congruent
    with final product
-   Perform integration testing


## Submission Instructions

Upon completion of Assignment 4.1 push your code to GitLab as usual.



## Requirements

0.  Define a `Fractal` abstract class and *three* concrete sub-classes
    -   The `Fractal` abstract class exists solely to provide a common
        structure to the concrete classes that inherit from it.  Your program
        will not create plain `Fractal` objects.  It will instead use classes
        derived from `Fractal` through inheritance.
    -   The `Fractal` class cannot be instantiated because its `__init__`
        method is a placeholder which raises [`NotImplementedError`](https://docs.python.org/3.9/library/exceptions.html#NotImplementedError)
        when called.  It need only consist of this line of code:
        `raise NotImplementedError("Concrete subclass of Fractal must implement __init__")`
    -   `Fractal` provides a placeholder `count()` method which raises an
        exception when called.  It consists solely of this statement:
        `raise NotImplementedError("Concrete subclass of Fractal must implement count() method")`
    -   You are allowed (but not required) to write other methods besides
        `count()`.  These methods do not need to raise `NotImplementedError`.
        These methods would then be available in all derived classes of
        `Fractal`.
    -   The `Julia` and `Mandelbrot` classes inherit their structure from the
        abstract class `Fractal`, and are obligated to provide their own
        implementations of `__init__` and `count()` such that they will not
        raise `NotImplementedError` when used.
    -   `count()` takes one complex number as input and returns an integer
        that is the number of iterations tried before the absolute value of the
        Fractal formula grew larger than `2.0`; otherwise the maximum number of
        iterations is returned.  This operation is the defining characteristic
        of a `Fractal` object.
    -   Other data used by `count()` are supplied through `self`, if needed.
    -   Define at least **one** new concrete subclass of `Fractal` following the
        pattern set forth by `Julia` and `Mandelbrot` but using different
        formulae.  You may choose from
        *   [Mandelbrot3 and Mandelbrot4](http://usefuljs.net/fractals/docs/multibrot.html)
        *   [Phoenix, BurningShip, and BurningShipJulia](http://usefuljs.net/fractals/docs/mandelvariants.html).
        You may also devise your own fractal formula.  Get creative!  If your
        new fractal class requires new configuration parameters, augment your
        `FractalFactory` class to handle then.
    -   The concrete sub-classes of `Fractal` are used _interchangeably_ in
        your program.  This is an example of polymorphism in action: objects of
        different classes which are used in the same way.  The code which uses
        a `Fractal`-derived object does not inspect the object to determine
        what kind of fractal it is; it just works because it defines the
        `count()` method.
    -   `Fractal` objects have no relation whatsoever to `Palettes` nor any
        knowledge about `Colors`.
1.  `FractalFactory` class or module
    -   Follow the [Factory Method Pattern](https://sourcemaking.com/design_patterns/factory_method)
        in your program when you need to instantiate objects embodying fractal
        algorithms.  `FractalFactory` returns a concrete fractal object based
        upon a configuration file given to it from the main program.  See below
        for details about the format of the fractal configuration file.
    -   The file defining `FractalFactory` is the only place in your entire
        program where your concrete `Fractal`-derived classes need to be
        imported.
    -   The `FractalFactory` itself doesn't have to be an object that you
        instantiate; it can be a function within a module.

        For example, this is how a `FractalFactory` object would be used:

        ```
        from FractalFactory import FractalFactory

        factory = FractalFactory()
        fractal = factory.makeFractal(sys.argv[1])
        ```

        Instead, `FractalFactory` might be a module containing the function `makeFractal()`:

        ```
        import FractalFactory

        fractal = FractalFactory.makeFractal(sys.argv[1])
        ```
    -   When no fractal configuration file is specified by the user on the
        command line, `FractalFactory` produces a "default" fractal
        configuration object that is hardcoded into your program.
    -   `FractalFactory` must do some basic error checking upon the contents of
        the fractal configuration file it uses to create a `Fractal` object.
        *   When a missing or inaccessible fractal is called for, simply let
            the `open()` function fail.
        *   When a fractal configuration file contains errors, raise
            [`RuntimeError`](https://docs.python.org/3.9/library/exceptions.html#RuntimeError).
            Possible errors are described in the section "Fractal Configuration
            File Format" below.
2.  Create a `Palette` abstract class and *two* concrete sub-classes
    -   The `Palette` abstract class exists solely to provide a common
        structure to the concrete classes that inherit from it.  Your program
        will not create plain `Palette` objects.  It will instead use classes
        derived from `Palette` through inheritance.
    -   The `Palette` class cannot be instantiated because its `__init__`
        method is a placeholder which raises [`NotImplementedError`](https://docs.python.org/3.9/library/exceptions.html#NotImplementedError)
        when called.  It need only consist of this line of code:
        `raise NotImplementedError("Concrete subclass of Palette must implement __init__")`
    -   `Palette` provides a placeholder `getColor()` method which raises an
        exception when called.  It consists solely of this statement:
        `raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")`
    -   You are allowed (but not required) to write other methods besides
        `getColor()`.  These methods do not need to raise
        `NotImplementedError`.  These methods would then be available in all
        derived classes of `Palette`.
    -   Concrete subclasses of `Palette` inherit their structure from the
        abstract class `Palette`, and are obligated to provide their own
        implementations of `__init__` and `getColor()` such that they will not
        raise `NotImplementedError` when used.
    -   `getColor(n)` takes an integer as input and returns a string which
        represents a color in this format: `"#RRGGBB"`. This operation is the
        defining characteristic of a  `Palette`  object.
    -   Other data used by `count()` are supplied through `self`, if needed.
    -   Define at least **three** concrete subclasses of `Palette` classes
        that provide alternative color palettes.  Generalize color palette
        creation so that a user-defined number of iterations may be specified
        instead of using a hard-coded array of colors.
    -   The concrete sub-classes of  `Palette`  are used _interchangeably_ in
        your program.  This is an example of polymorphism in action: objects of
        different classes which are used in the same way.  The code which uses
        a `Palette`-derived object does not inspect the object to determine
        what kind of palette it is; it just works because it defines the
        `getColor()` method.
    -   `Palette` objects have no relation to nor knowledge of `Fractal`.
3.  `PaletteFactory` class or module
    -   Follow the [Factory Method Pattern](https://sourcemaking.com/design_patterns/factory_method)
        in your program when you need to instantiate objects embodying palettes.
        `PaletteFactory` returns a concrete palette object specified by the
        user on the command line.
    -   The file defining `PaletteFactory` is the only place in your entire
        program where your concrete `Palette`-derived classes need to be
        imported.
    -   The `PaletteFactory` itself doesn't have to be an object that you
        instantiate; it can be a function within a module.
        ```
        from PaletteFactory import PaletteFactory

        factory = PaletteFactory()
        palette = factory.makePalette(paletteName)
        ```
        Instead, `PaletteFactory` might be a module containing the function `makePalette()`:
        ```
        import PaletteFactory

        palette = PaletteFactory.makePalette(paletteName)
        ```
    -   When no palette is specified by the user on the command line,
        `PaletteFactory` creates a default palette at your discretion.  Which
        type of palette is considered the default may _not_ be hard coded into
        the main driver program; the default is wholly under the purview of the
        factory.
    -   When a non-existent palette is asked for, an error is raised
        ```
        raise NotImplementedError("Invalid palette requested")
        ```
4.  The command line interface to your program must follow the format described
    below.
5.  Documentation (UML, user manual, etc.) from the previous assignment is
    congruent with final the product.  List the names of possible palettes in
    the user manual as this program will not regard absent command line
    arguments as an error and will not print a usage message.


## Command line interface

The command line interface to your program must follow this format:

```
python src/main.py [FRACTAL_FILE [PALETTE_NAME]]
```

0.  FRACTAL_FILE is the name of a fractal configuration file found in the data directory of the original repository. It is an error if this file name is misspelled, or refers to a file which your program cannot open. It is also an error when this file does not follow the format described below.
1.  PALETTE_NAME is an optional name of a palette which your `PaletteFactory` can produce.

When zero arguments are given, your factories return hard-coded default values. For example:

```
$ python src/main.py
FractalFactory: Creating default fractal
PaletteFactory: Creating default color palette
```

When only one argument is given, it is used as the name of a fractal configuration file:

```
$ python src/main.py data/fulljulia.frac
PaletteFactory: Creating default color palette
```

When two arguments are given, the first is used as the name of a fractal configuration object and the second is taken to be the name of a Palette:

```
$ python src/main.py data/funnel-down.frac ColorCube
```

When an missing, or inaccessible fractal configuration file is given, the
program may exit with the error raised by `open()`:

```
$ python src/main.py data/NOT_EXIST ColorCube
Traceback (most recent call last):
  File "src/main.py", line 26, in <module>
    fractal = FractalFactory.makeFractal(cfg)
  File "/home/fadein/cs1440-falor-erik-assn4/src/FractalFactory.py", line 30, in makeFractal
    cfg = __readFrac(cfgFile)
  File "/home/fadein/cs1440-falor-erik-assn4/src/FractalFactory.py", line 64, in __readFrac
    with open(cfgFile) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/NOT_EXIST'
```

When an invalid palette name is requested, the program exits with an error message

```
$ python src/main.py data/funnel-down.frac NOT_EXIST
Traceback (most recent call last):
  File "src/main.py", line 27, in <module>
    palette = PaletteFactory.makePalette(fractal.iterations, gtype=palette)
  File "/home/fadein/cs1440-falor-erik-assn4/src/PaletteFactory.py", line 49, in makePalette
    raise NotImplementedError("Invalid palette requested")
NotImplementedError: Invalid palette requested
```


## Fractal configuration file format

Fractal configuration files have a simple format.  Study the files in the
[../data/](../data/) directory to understand how they are written.  In summary:

*   Lines beginning with `#` are skipped
*   Blank lines are skipped
*   Configuration parameters can appear in any order
*   Names of configuration parameters are case-insensitive
*   Parameter names are separated from their values with a colon `:`
*   White space is not significant; you can strip all of it away from the input data



## Configuration fields

The meaning of the fields within configuration files are illustrated by this image:

![annotated mandelbrot image](./annotated_mandelbrot.png)



*   `type`
    *   Informs the program which fractal formula to apply.  For example, this may be `Mandelbrot`, `Julia` or `BurningShipJulia`, etc.
*   `centerX`
    *   The center point of the image along the X axis (a.k.a. the "real" axis)
*   `centerY`
    *   The center point of the image along the Y axis (a.k.a. the "imaginary" axis)
*   `axisLength`
    *   The distance along the complex plane this image covers
    *   Because the images are square, both axes are the same size
    *   Making this value smaller results in a *zoomed-in* image
    *   Making this value larger results in a *zoomed-out* image
*   `pixels`
    *   The width (and height) of the image in pixels 
    *   Increasing this parameter increases
        *   the size of the image
        *   the amount of time it takes to render the image
*   `iterations`
    *   The number of iterations the central `for` loop runs before giving up on coloring a pixel
    *   Controls the number of colors in the image
    *   Increasing this parameter increases
        *   the amount of time it takes to render the image
        *   the amount detail visible in your image, provided your color palette has enough different, contrasting colors 
*   `creal` and `cimag`
    *   The real and imaginary components of the `C` constant used by the Julia formula
    *   Experiment with different values to make your Julia set images more interesting


### Required fields 

The following fields are **required** for all types of fractals.  Your program
should consider it an error when any of these are missing:

*   `type`
*   `centerx`
*   `centery`
*   `axislength`
*   `pixels`
*   `iterations`

These fields are **required** only for Julia fractals.  Your program
should consider it an error when either of these are missing when `type ==
julia` or `burningshipjulia`:

*   `creal`
*   `cimag`

Any other fields which may appear in data files should be ignored.


### Fractal configuration objects

When your program reads data from from configuration files it needs to put that
information into some variables so that it can be used later.  You may define a
new class to represent fractal configuration, though a dictionary is perfectly
adequate.

As an example, upon reading the fractal configuration found in
`data/fullmandelbrot.frac` my implementation creates a dictionary containing
this information:

```
{
    'type': 'mandelbrot',
    'pixels': 640,
    'axislength': 4.0,
    'pixelsize': 0.00625,
    'iterations': 100,
    'min': {'x': -2.0, 'y': -2.0},
    'max': {'x': 2.0, 'y': 2.0},
    'imagename': 'fullmandelbrot.png'
}
```

Note the addition of computed values alongside parameters contained in
the configuration file.

*   The  `min`  and  `max`  values are trivially computed from (`centerX`,
    `centerY`) and `axisength`, giving the coordinates in the complex plane of
    the image pixels at the upper left and lower-right corners of the image.
*   Likewise, the length of each pixel of the image in terms of distance on the
    real and imaginary axes is given as `pixelsize`, which is easily obtained
    from  `pixels`  and  `axislength`.
*   `imagename` was added by the program for my convenience; you can do the
    same if it suits you.


Other considerations:

-   We will follow the convention that fractal configuration files have the extension .frac, but your program will not enforce this.  In other words, your program accepts *any* file *regardless* of its name.
-   Words in the configuration file are  _case-insensitive_. `Type`  ==  `TYPE` ==  `type`. Convert all text to lower case as you read it into your program.
-   Lines beginning with a '#' character are treated as comments; they are ignored by your program.
    -   Likewise, ignore lines that contain only whitespace.
-   Required parameters which are missing are treated as an error.
-   Misspelled parameter names are ignored.
-   Missing or invalid values are likewise to be treated as errors.


[../data/invalid.frac](../data/invalid.frac) is a fractal configuration file which contains errors:

```
# invalid.frac
#
# This is a purposefully broken fractal config file
# Use this to stress-test your configuation file parser


# Here be dragons!
Type: julia
centerX: in the middle
centerY:
Itertons: 23.654
PIXELS: 894.965
cImag: 0.3
```

As explained above, the capitalization of text in this file is irrelevant.  These are the errors:

-   `centerx`'s value is not a number; coordinates of the center point are regarded by the program as floats, but may occur in this file as integers
-   `centery` is missing its value
-   `iterations` was misspelled, and thus ignored; this is handled the same as if `iterations` was not specified at all
-   The value of the `pixels` must be an integer, not a float
-   The required parameter `axislength` is missing
-   The `type` of this fractal is `julia`, but the required `creal` property is missing

When these errors are encountered your program must raise a
`NotImplementedError` with a message.  The following message is the
bare-minimum that will suffice:

```
raise NotImplementedError("Invalid fractal configuration file")
```

It is better if you can provide more specific information about what's wrong, though this is not required for this assignment:

*   `raise NotImplementedError("The value of the 'centerx' parameter is not a number")`
*   `raise NotImplementedError("The value of the 'centery' parameter is missing")`
*   `raise NotImplementedError("The value of the 'pixels' parameter is not an integer")`
*   `raise NotImplementedError("The required parameter 'iterations' is missing")`
*   `raise NotImplementedError("The required parameter 'axislength' is missing")`
*   `raise NotImplementedError("This is a Julia fractal, but the 'creal' parameter was not specified")`

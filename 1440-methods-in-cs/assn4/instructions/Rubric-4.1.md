# CS 1440 Assignment 4.1 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 20 pts | Concrete fractal classes inherit from the abstract `Fractal` class<br/>The `Fractal` class cannot be instantiated. `Julia` and `Mandelbrot` fractals inherit from `Fractal`.
| 10 pts | Add a third concrete fractal class embodying an algorithm of your choice.<br/>Each fractal must be distinct from the others; simple renames are <em>not</em> allowed.<br/>The `FractalInformation` module/class handles any custom parameters needed by this fractal.
| 10 pts | `FractalFactory` returns a concrete fractal object when given a configuration object or raises `NotImplementedError`
| 20 pts | Concrete palette classes which inherit from abstract class `Palette`<br/>The `Palette` class cannot be instantiated, but defines methods which may be overridden by subclasses. Two or more concrete polymorphic palette classes are provided which inherit from `Palette`
| 10 pts | Two or more concrete polymorphic palette classes<br/>At least two new palette classes which inherit from Palette are written. These classes are polymorphic in that they each provide the same methods and may be used interchangeably
| 10 pts | `PaletteFactory` creates concrete palette objects.<br/>When no command-line argument is supplied, create a default palette object.<br/>Otherwise, produce the palette object requested on the command line or raise `NotImplementedError`.
| 10 pts | UML Class diagram describes involved classes' relationships, data members and methods accurately
| 10 pts | Class diagram adheres to UML standards as far as these were explained in class<br/>Abstract classes in UML write the class name in *italics*
| 10 pts | Users' Manual accurately describes the program's user interface

**Total points: 110**


## Penalties

*   Review the Course Rules document in the lecture notes repository to avoid general penalties which apply to all assignments.
    *   In particular, don't forget to include your *Software Development Plan* and *Sprint Signature* documents in the `doc/` directory.
    *   Pay attention to the name you give your repository on GitLab.

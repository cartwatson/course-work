# CS 1440 Assignment 4.0 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
|10 pts  | The original user interface and functionality are preserved<br/>No new features or capabilities are added to the refactored program
|15 pts  | Increase coverage of Unit Tests<br/>All tests continue to pass
|15 pts  | Code Smells are cataloged in `doc/Smells.md`<br/>Each piece of required information is included: location, code snippet, explanation and fix description.
|15 pts  | A UML class diagram describes your design<br/> All modules/classes are represented, behaviors and data members are accounted for, and relationships between modules are described.
|15 pts  | A user's manual explains in simple terms how the program is run<br/>Avoid describing details of how the program works.
|10 pts  | `main.py` is a short, simple driver program<br/>It accepts command-line arguments and calls upon other modules<br/>It imports only those modules it uses directly
|10 pts  | `FractalInformation.py` defines a data structure that contains all fractal configuration data in the program<br/>configuration data intended for the Mandelbrot function are distinctly marked from those for the Julia function
|10 pts  | `Mandelbrot.py` and `Julia.py` each define functions which, when given a coordinate in the complex plane, return the iteration count for that point<br/>The functions are isolated from the concepts of palettes and colors<br/>Function parameters may be changed as you deem necessary
|10 pts  | `Palette.py` contains an array of colors<br/>Colors are strings which may be names of colors (e.g. `Red`, `White`, `Blue`) or hex colors in the form `#RRGGBB` where `R`, `G`, `B`, are hexadecimal digits.

**Total points: 110**


## Penalties

Review the [Course Rules](https://gitlab.cs.usu.edu/erik.falor/fa20-cs1440-lecturenotes/blob/master/Course_Rules.md)
document to avoid general penalties which apply to all assignments.

In particular, don't forget to include your *Software Development Plan* and
*Sprint Signature* documents in the `doc/` directory.

Pay attention to the name you give your repository on GitLab.

Tag the last commit of Assignment 4.0 `Assn4.0` (mind the capitalization).
Push this tag to GitLab.  Detailed instructions are
[here](https://gitlab.cs.usu.edu/erik.falor/fa20-cs1440-lecturenotes/-/blob/master/Using_Git/Intermediate_Git.md#tagging-commits)

# Code Smells Report

**Issues with main.py**

Lines 18-20, unnecessarily complex
```
all_of_the_fractals = MBROTS
all_of_the_fractals.extend(JULIAS)
for i in all_of_the_fractals:
```
turned both lists into a dictionary and pulled from there

Line 23, misspelled variable name

**Issues with julia_fractal.py**

getFractalConfig is useless
```
def getFractalConfig(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                return key
```
function deleted

Unrelated and excessive comments throughout program - comments deleted.

Many functions do too many things or the wrong thing. - functions turned into methods and simplified.

Ordering of functions and variables is hard to read. - variables placed at the top of file, functions at the bottom

Use of vague variables throughout. - variables renamed to be more recognizable.

Creation and use of global variables
```
    global grad
    global win
```
```
    global win
    global grad
    global photo
```
```
global WHITE
```
Global variables replaced with class variables.

Assignment of variable unreachable
```
if abs(z) > 2:
    return grad[i]  # The sequence is unbounded
    z += z + c
```
deleted assignment

Magic number used for range
```
# Here 76 refers to the number of colors in the palette
for i in range(78):
```
replaced with class variable.

Unused return statement
```
return grad[77]         # Else this is a bounded sequence
return grad[78]
```
deleted extra return statement.

Method name excessively long
```
def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
```
name shortened, function later removed.

Function makePicture has unused parameters
```
def makePicture(f, i, e):
```
deleted unused parameters.

Excessive use of .pack()
```
canvas.pack()
canvas.create_image((256, 256), image=photo, state="normal")
canvas.pack()
canvas.pack()
canvas.pack() .pack()
canvas.create_image((256, 256), image=photo, state="normal")
canvas.pack()
canvas.pack()
canvas.pack()
```
deleted excessive calls of .pack().

Variables are created and never used in multiple locations - deleted variables

Gradient is explicit instead of created - moved to Palette.py and renamed

Code from main is reused at the end of file - removed from file.

**Issues with mbrot_fractal.py**

Imports math when it is not needed - import statement removed.

Platte is explicitly defined - moved to Palette.py and renamed.

Unnecessary global variables created - replaced with class varibales.

Redundant return
```
return palette[MAX_ITERATIONS - 1]   # Indicate a bounded sequence
return palette[MAX_ITERATIONS]
```
second return deleted.

Unused variable created
```
portion = int(512 / 64)
total_pixels = 1048576

maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
```
variables deleted.

Unused function
```
def pixelsWrittenSoFar(self, rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels
```
function deleted.

Copied functionality from main.py
```
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for i in images:
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in images:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in images:
            print(f"\t{i}")
        sys.exit(1)

    else:
        mbrot_main(sys.argv[1])
```
removed from file.
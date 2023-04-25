# Fractal Visualizer User Manual

In a command line navigate to
```
cs1440-watson-jethro-assn4
```
and run
```
python src/main.py data/<fractal name>.frac <palette name>
```
if data/<fractal name> is not given the default will be run

note that <palette name> is optional

appropriate palette names are "Palette0" and "grayscale"

A window should pop up, the program will start drawing to the window.

Afterwards a .png will be saved to the directory it is run from.

When the drawing is completed the program will output the time taken, and instructions on how to end the program.

Closing the window where the fractal is being drawn will cause the program to crash.
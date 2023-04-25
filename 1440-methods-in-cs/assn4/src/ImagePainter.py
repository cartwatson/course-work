import sys
from time import time
from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter():
    def __init__(self, fractal, palette, fractalFilePath):
        self.__window = Tk()
        self.__img = None #type PhotoImage
        self.__fractal = fractal
        self.__config = fractal.getConfig()
        self.__palette = palette
        self.__fractalFilePath = fractalFilePath

    def createWindow(self):
        # Set up the GUI so that we can display the fractal image on the screen
        start = time()
        self.__img = PhotoImage(width=self.__config["pixels"], height=self.__config["pixels"])
        self.__makePicture()
        stop = time()
        imageName = self.__fractalFilePath.split('/')[-1].replace(".frac", "")
        self.__img.write(f"{imageName}.png")
        print(f"Done in {stop - start:.3f} seconds!", file=sys.stderr)
        print("Close the image window to exit the program")
        # Call tkinter.mainloop so the GUI remains open
        mainloop()

    def __makePicture(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        Assumes the image is 512x512 pixels."""
        # Correlate the boundaries of the PhotoImage object to the complex
        # coordinates of the imaginary plane
        min = ((self.__config['centerx'] - (self.__config['axislength'] / 2.0)),
               (self.__config['centery'] - (self.__config['axislength'] / 2.0)))

        max = ((self.__config['centerx'] + (self.__config['axislength'] / 2.0)),
               (self.__config['centery'] + (self.__config['axislength'] / 2.0)))

        # Display the image on the screen
        canvas = Canvas(self.__window, width=self.__config["pixels"], height=self.__config["pixels"], bg='#ffffff')
        canvas.pack()
        canvas.create_image((self.__config["pixels"]/2, self.__config["pixels"]/2), image=self.__img, state="normal")
        # At this scale, how much length and height of the imaginary plane does one pixel cover?
        size = abs(max[0] - min[0]) / self.__config["pixels"]
        
        for row in range(self.__config["pixels"], 0, -1):
            for col in range(self.__config["pixels"]):
                x = min[0] + col * size
                y = min[1] + row * size

                count = self.__fractal.count(complex(x, y))
                color = self.__palette.getColor(count)

                self.__img.put(color, (col, self.__config["pixels"] - row))
            self.__window.update()  # display a row of pixels

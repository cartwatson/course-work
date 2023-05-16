// ------------------------------------------------------------------
// 
// This is the graphics object.  It provides a pseudo pixel rendering
// space for use in demonstrating some basic rendering techniques.
//
// ------------------------------------------------------------------
MySample.graphics = (function(pixelsX, pixelsY, showPixels) {
    'use strict';

    let canvas = document.getElementById('canvas-main');
    let context = canvas.getContext('2d', { alpha: false });

    let deltaX = canvas.width / pixelsX;
    let deltaY = canvas.height / pixelsY;

    //------------------------------------------------------------------
    //
    // Public function that allows the client code to clear the canvas.
    //
    //------------------------------------------------------------------
    function clear() {
        context.save();
        context.setTransform(1, 0, 0, 1, 0, 0);
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.restore();

        //
        // Draw a very light background to show the "pixels" for the framebuffer.
        if (showPixels) {
            context.save();
            context.lineWidth = .1;
            context.strokeStyle = 'rgb(150, 150, 150)';
            context.beginPath();
            for (let y = 0; y <= pixelsY; y++) {
                context.moveTo(1, y * deltaY);
                context.lineTo(canvas.width, y * deltaY);
            }
            for (let x = 0; x <= pixelsX; x++) {
                context.moveTo(x * deltaX, 1);
                context.lineTo(x * deltaX, canvas.width);
            }
            context.stroke();
            context.restore();
        }
    }

    //------------------------------------------------------------------
    //
    // Public function that renders a "pixel" on the framebuffer.
    //
    //------------------------------------------------------------------
    function drawPixel(x, y, color) {
        context.fillStyle = color;
        context.fillRect(Math.floor(x * deltaX), Math.floor(y * deltaY), Math.ceil(deltaX), Math.ceil(deltaY));
    }

    //------------------------------------------------------------------
    //
    // Bresenham line drawing algorithm.
    //
    //------------------------------------------------------------------
    function drawLine(x1, y1, x2, y2, color) {
        let dX = Math.abs(x2 - x1);
        let dY = Math.abs(y2 - y1);
        let Pk = 2 * dY - dX;
        let currP = { x: x1, y: y1 }
        let dirX = 1;
        let dirY = 1;

        // determine octant
        //   \ 7 | 0 /
        //  6 \  |  / 1
        // ------------
        //  5 /  |  \ 2
        //   / 4 | 3 \

        if (x2 - x1 < 0) {
            // left half // octants: 4, 5, 6, 7
            if (y2 - y1 < 0) {
                // top half // octants: 6, 7
                if (y2 > x2) {
                    console.log("OCTANT 7"); // DEBUG
                    // octant 7

                } else {
                    console.log("OCTANT 6"); // DEBUG
                    // octant 6
                    dirX = -1;
                }
            } else {
                // bottom half // octants: 4, 5
                if (y2 > x2) {
                    console.log("OCTANT 5"); // DEBUG
                    // octant 5
                    dirX = -1;
                    dirY = -1;
                } else {
                    console.log("OCTANT 4"); // DEBUG
                    // octant 4

                }
            }
        } else {
            console.log("right half") // DEBUG
            // right half // octants: 0, 1, 2, 3
            if (y2 - y1 < 0) {
                console.log("top right corner") // DEBUG
                // top right corner // octants: 0, 1
                if (y2 > x2) {
                    console.log("OCTANT 0"); // DEBUG
                    // octant 0
                    
                } else {
                    console.log("OCTANT 1"); // DEBUG
                    // octant 1
                    // default dirX and dirY
                }
            } else {
                console.log("bottom right corner") // DEBUG
                // bottom right corner // octants: 2, 3
                if (y2 > x2) {
                    console.log("OCTANT 3"); // DEBUG
                    // octant 3

                } else {
                    console.log("OCTANT 2"); // DEBUG
                    // octant 2
                    dirY = -1;
                }
            }
        }


        // draw line
        let notFinished = true;
        while (notFinished)
        {
            // draw pixel
            drawPixel(currP.x, currP.y, color)

            // get point
            currP.x += dirX; // TODO: change to dirX
            if (Pk >= 0) {
                currP.y -= dirY; // TODO: change to dirY
                Pk = Pk + 2 * dY - 2 * dX;
            } else {
                Pk = Pk + 2 * dY;
            }

            // end if we just drew the last pixel
            if (currP.x == x2 && currP.y == y2) { notFinished = false; }
        }
    }

    let api = {
        clear: clear,
        drawPixel: drawPixel,
        drawLine: drawLine,
        get sizeX() { return pixelsX; },
        get sizeY() { return pixelsY; }
    };

    return api;
}(150, 150, true));

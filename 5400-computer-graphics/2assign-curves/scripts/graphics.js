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
        x = Math.trunc(x);
        y = Math.trunc(y);

        context.fillStyle = color;
        context.fillRect(x * deltaX, y * deltaY, deltaX, deltaY);
    }

    //------------------------------------------------------------------
    //
    // Helper function used to draw an X centered at a point.
    //
    //------------------------------------------------------------------
    function drawPoint(x, y, ptColor) {
        drawPixel(x - 1, y - 1, ptColor);
        drawPixel(x + 1, y - 1, ptColor);
        drawPixel(x, y, ptColor);
        drawPixel(x + 1, y + 1, ptColor);
        drawPixel(x - 1, y + 1, ptColor);
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
        let dir = "horiz";

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
                if (dY > dX) {
                    // octant 7
                    dir = "vert";
                    dirX = -1;
                } else {
                    // octant 6
                    dirX = -1;
                }
            } else {
                // bottom half // octants: 4, 5
                if (dY > dX) {
                    // octant 4
                    dir = "vert";
                    dirY = -1;
                    dirX = -1;
                } else {
                    // octant 5
                    dirX = -1;
                    dirY = -1;
                }
            }
        } else {
            // right half // octants: 0, 1, 2, 3
            if (y2 - y1 < 0) {
                // top right corner // octants: 0, 1
                if (dY > dX) {
                    // octant 0
                    // default dirX and dirY
                    dir = "vert";
                } else {
                    // octant 1
                    // default dirX and dirY
                }
            } else {
                // bottom right corner // octants: 2, 3
                if (y2 > x2) {
                    // octant 3
                    dir = "vert";
                    dirY = -1;
                } else {
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
            if (dir == "vert") {
                currP.y -= dirY;
                if (Pk >= 0) {
                    currP.x += dirX;
                    Pk = Pk + 2 * dX - 2 * dY;
                } else {
                    Pk = Pk + 2 * dX;
                }
            } else {
                currP.x += dirX;
                if (Pk >= 0) {
                    currP.y -= dirY;
                    Pk = Pk + 2 * dY - 2 * dX;
                } else {
                    Pk = Pk + 2 * dY;
                }
            }

            // end if we just drew the last pixel
            if (currP.x == x2 || currP.y == y2) { notFinished = false; }
        }
    }

    //------------------------------------------------------------------
    //
    // Renders an Hermite curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveHermite(controls, segments, showPoints, showLine, showControl, lineColor) {
        
    }

    //------------------------------------------------------------------
    //
    // Renders a Cardinal curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveCardinal(controls, segments, showPoints, showLine, showControl, lineColor) {

    }

    //------------------------------------------------------------------
    //
    // Renders a Bezier curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveBezier(controls, segments, showPoints, showLine, showControl, lineColor) {

    }

    //------------------------------------------------------------------
    //
    // Renders a Bezier curve based on the input parameters; using the matrix form.
    // This follows the Mathematics for Game Programmers form.
    //
    //------------------------------------------------------------------
    function drawCurveBezierMatrix(controls, segments, showPoints, showLine, showControl, lineColor) {

    }

    //------------------------------------------------------------------
    //
    // Entry point for rendering the different types of curves.
    // I know a different (functional) JavaScript pattern could be used
    // here.  My goal was to keep it looking C++'ish to keep it familiar
    // to those not expert in JavaScript.
    //
    //------------------------------------------------------------------
    function drawCurve(type, controls, segments, showPoints, showLine, showControl, lineColor) {
        switch (type) {
            case api.Curve.Hermite:
                drawCurveHermite(controls, segments, showPoints, showLine, showControl, lineColor);
                break;
            case api.Curve.Cardinal:
                drawCurveCardinal(controls, segments, showPoints, showLine, showControl, lineColor);
                break;
            case api.Curve.Bezier:
                drawCurveBezier(controls, segments, showPoints, showLine, showControl, lineColor);
                break;
            case api.Curve.BezierMatrix:
                drawCurveBezierMatrix(controls, segments, showPoints, showLine, showControl, lineColor);
                break;
        }
    }

    //
    // This is what we'll export as the rendering API
    const api = {
        clear: clear,
        drawPixel: drawPixel,
        drawLine: drawLine,
        drawCurve: drawCurve
    };

    Object.defineProperty(api, 'sizeX', {
        value: pixelsX,
        writable: false
    });
    Object.defineProperty(api, 'sizeY', {
        value: pixelsY,
        writable: false
    });
    Object.defineProperty(api, 'Curve', {
        value: Object.freeze({
            Hermite: 0,
            Cardinal: 1,
            Bezier: 2,
            BezierMatrix: 3
        }),
        writable: false
    });

    return api;
}(1000, 1000, true));

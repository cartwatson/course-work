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
    // Handles boolean logic for curve drawing
    //
    //------------------------------------------------------------------
    function drawPointsLineControl(startPt, endPt, points, showPoints, showLine, showControl, lineColor) {
        // print line
        if (showLine) {
            for (let i = 0; i < points.length - 1; i++) {
                // grab point and next point
                let start = { x: points[i].x, y: points[i].y }
                let end   = { x: points[i+1].x, y: points[i+1].y }
                
                console.log(start.x, start.y, end.x, end.y) // DEBUG
                // drawLine(start.x, start.y, end.x, end.y, lineColor) // TODO: FIX
            }
        }

        // print points
        if (showPoints) {
            for (let i = 0; i < points.length; i++) { drawPoint(points[i].x, points[i].y, lineColor) }
        // print control points
        } else if (showControl) {
            drawPoint(startPt.x, startPt.y, lineColor)
            drawPoint(endPt.x, endPt.y, lineColor)
        }
    }

    
    //------------------------------------------------------------------
    //
    // Renders an Hermite curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveHermite(controls, segments, showPoints, showLine, showControl, lineColor) {
        // parse controls & init
        let startPt    = { x: controls[0].x, y: controls[0].y }
        let tanStartPt = { x: controls[1].x, y: controls[1].y }
        let tanEndPt   = { x: controls[2].x, y: controls[2].y }
        let endPt      = { x: controls[3].x, y: controls[3].y }
        let points = []

        // divide curve into segments
        for (let t = 0; t <= 1; t += 1 / segments) {
            // calc t^2 and t^3
            let t2 = t  * t
            let t3 = t2 * t

            // calculate basis functions
            let h1 =  2 * t3 - 3 * t2 + 1
            let h2 = -2 * t3 + 3 * t2
            let h3 =      t3 - 2 * t2 + t
            let h4 =      t3 -     t2

            // calc x and y & store point
            points.push({
                x: h1 * startPt.x + h2 * endPt.x + h3 * tanStartPt.x + h4 * tanEndPt.x,
                y: h1 * startPt.y + h2 * endPt.y + h3 * tanStartPt.y + h4 * tanEndPt.y,
            })
        }

        drawPointsLineControl(startPt, endPt, points, showPoints, showLine, showControl, lineColor)
    }

    //------------------------------------------------------------------
    //
    // Renders a Cardinal curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveCardinal(controls, segments, showPoints, showLine, showControl, lineColor) {
        let points = []
        let startPt = controls[0]
        let endPt   = controls.slice(-1)
        let tension = 0.5 //TODO: TEST

        // calculate points
        for (let i = 0; i < controls.length - 4; i++) {
            let p0 = controls[i+0]
            let p1 = controls[i+1]
            let p2 = controls[i+2]
            let p3 = controls[i+3]

            // divide curve into segments
            for (let t = 0; t <= 1; t += 1 / segments) {
                // calc t^2 and t^3
                let t2 = t  * t
                let t3 = t2 * t

                // calculate basis functions
                let h1 =  2 * t3 - 3 * t2 + 1
                let h2 = -2 * t3 + 3 * t2
                let h3 =      t3 - 2 * t2 + t
                let h4 =      t3 -     t2

                // calc x and y & store point
                points.push({
                    x: h1 * p1.x + h2 * p2.x + h3 * (p2.x - p0.x) * tension + h4 * (p3.x - p1.x) * tension,
                    y: h1 * p1.y + h2 * p2.y + h3 * (p2.y - p0.y) * tension + h4 * (p3.y - p1.y) * tension,
                })
            }
        }

        // boolean logic here
        drawPointsLineControl(startPt, endPt, points, showPoints, showLine, showControl, lineColor)
    }

    //------------------------------------------------------------------
    //
    // Renders a Bezier curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveBezier(controls, segments, showPoints, showLine, showControl, lineColor) {
        let points  = []
        let startPt = controls[0]
        let endPt   = controls.slice(-1)

        let len = controls.length - 1
        for (let t = 0; t <= 1; t += 1 / segments) {
            for (let i = 0; i < len; i++) {
                coefficient = binomialCoefficient(len, i) * (1 - t)**(len - i) * t**i
                points.push({
                    x: coefficient * controlPoints[i].x,
                    y: coefficient * controlPoints[i].y
                })
            }
        }

        // boolean logic here
        drawPointsLineControl(startPt, endPt, points, showPoints, showLine, showControl, lineColor)
    }

    // Helper function to calculate the binomial coefficient of two numbers
    // adjusted from https://www.w3resource.com/javascript-exercises/javascript-math-exercise-20.php
    function binomialCoefficient(n, k) {
        let coeff = 1;
        for (let x = n-k+1; x <= n; x++) { coeff *= x }
        for (x = 1; x <= k; x++) { coeff /= x }
        return coeff;
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

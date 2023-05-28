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

    let lineColorDEBUG    = "red"
    let pointColorDEBUG   = "aqua"
    let controlColorDEBUG = "lightpink"

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

        // check if totally vertical line
        // not sure why this is necessary but it makes it work
        if (x1 - x2 === 0) { Pk = -1 }

        // draw line
        let notFinished = true;
        while (notFinished)
        {
            // draw pixel
            drawPixel(currP.x, currP.y, color)
            // console.log("drew a pixel")//DEBUG
            // console.log(currP.x, currP.y)//DEBUG
            // console.log(Pk)//DEBUG

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

            // console.log(currP.x, currP.y)//DEBUG

            // end if we just drew the last pixel
            if (currP.x == x2 && currP.y == y2 || currP.x == x1 && currP.y == y1) {
                drawPixel(currP.x, currP.y, color)
                notFinished = false;
            }
        }
    }

    //------------------------------------------------------------------
    //
    // Draw lines inbetween set of given points
    //
    //------------------------------------------------------------------
    function drawLines(points, lineColor) {
        for (let i = 0; i < points.length - 1; i++) {
            // console.log(points[i].x, points[i].y, points[i+1].x, points[i+1].y)//DEBUG
            drawLine(points[i].x, points[i].y, points[i+1].x, points[i+1].y, lineColor)
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
        for (let u = 0; u <= 1; u += 1 / segments) {
            // calc t^2 and t^3
            let u2 = u  * u
            let u3 = u2 * u

            // calculate basis functions
            let h1 =  2 * u3 - 3 * u2 + 1
            let h2 = -2 * u3 + 3 * u2
            let h3 =      u3 - 2 * u2 + u
            let h4 =      u3 -     u2

            // calc x and y & store point
            points.push({
                x: Math.round(h1 * startPt.x + h2 * endPt.x + h3 * tanStartPt.x + h4 * tanEndPt.x),
                y: Math.round(h1 * startPt.y + h2 * endPt.y + h3 * tanStartPt.y + h4 * tanEndPt.y),
            })
        }

        // draw curve
        drawLines(points, lineColor)

        // handle boolean debug info
        // print line
        if (showLine) {
            drawLine(startPt.x, startPt.y, tanStartPt.x, tanStartPt.y, lineColorDEBUG)
            drawLine(endPt.x, endPt.y, tanEndPt.x, tanEndPt.y, lineColorDEBUG)
        }

        // print calculated points
        if (showPoints) {
            for (let i = 0; i < points.length; i++) {
                drawPoint(points[i].x, points[i].y, pointColorDEBUG)
            }
        }
        
        // print control points
        if (showControl) {
            drawPoint(controls[0].x, controls[0].y, controlColorDEBUG)
            drawPoint(tanStartPt.x,  tanStartPt.y,  controlColorDEBUG)
            drawPoint(tanEndPt.x,    tanEndPt.y,    controlColorDEBUG)
            drawPoint(controls[3].x, controls[3].y, controlColorDEBUG)
        }
    }

    //------------------------------------------------------------------
    //
    // Renders a Cardinal curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveCardinal(controls, segments, showPoints, showLine, showControl, lineColor) {
        let points = []
        let tension = controls[4] //TODO: TEST

        // calculate points
        let p0 = controls[0]
        let p1 = controls[1]
        let p2 = controls[2]
        let p3 = controls[3]

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
                x: Math.round(h1 * p1.x + h2 * p2.x + h3 * (p2.x - p0.x) * tension + h4 * (p3.x - p1.x) * tension),
                y: Math.round(h1 * p1.y + h2 * p2.y + h3 * (p2.y - p0.y) * tension + h4 * (p3.y - p1.y) * tension),
            })
        }

        // draw curve
        drawLines(points, lineColor)

        // handle boolean debug info
        // print line
        if (showLine) {
            drawLine(p0.x, p0.y, p1.x, p1.y, lineColorDEBUG)
            drawLine(p3.x, p3.y, p2.x, p2.y, lineColorDEBUG)
        }

        // print calculated points
        if (showPoints) {
            for (let i = 0; i < points.length; i++) {
                drawPoint(points[i].x, points[i].y, pointColorDEBUG)
            }
        }
        
        // print control points
        if (showControl) {
            for (let i = 0; i < controls.length; i++) {
                drawPoint(controls[i].x, controls[i].y, controlColorDEBUG)
            }
        }
    }

    //------------------------------------------------------------------
    //
    // Renders a Bezier curve based on the input parameters.
    //
    //------------------------------------------------------------------
    function drawCurveBezier(controls, segments, showPoints, showLine, showControl, lineColor) {
        let points  = []

        let n = controls.length - 1
        // for (let u = 0; u <= 1; u += 1 / segments) {
        for(let i = 0; i <= segments; i++) {
            const u = i / segments;
            
            let point = {x: 0, y: 0}
            for (let k = 0; k < controls.length; k++) {
                let coefficient = binomialCoefficient(n, k) * (1 - u)**(n - k) * u**k
                point.x += coefficient * controls[k].x
                point.y += coefficient * controls[k].y
            }

            points.push({ x: Math.round(point.x), y: Math.round(point.y) })
        }

        // draw curve
        drawLines(points, lineColor)

        // handle boolean debug info
        // print line between related control points
        if (showLine) {
            // drawLines(controls, lineColorDEBUG)
            for (let i = 0; i < controls.length -1; i++) {
                drawLine(controls[i].x, controls[i].y, controls[i+1].x, controls[i+1].y, lineColorDEBUG)
            }
        }

        // print calculated points
        if (showPoints) {
            for (let i = 0; i < points.length; i++) {
                drawPoint(points[i].x, points[i].y, pointColorDEBUG)
            }
        }
        
        // print control points
        if (showControl) {
            for (let i = 0; i < controls.length; i++) {
                drawPoint(controls[i].x, controls[i].y, controlColorDEBUG)
            }
        }
    }

    // Helper function to calculate the binomial coefficient of two numbers
    // adjusted from https://www.w3resource.com/javascript-exercises/javascript-math-exercise-20.php
    function binomialCoefficient (n, k) {
        let numerator = 1;
        let denominator = 1;
        for (let i = 0; i < k; i++) {
            numerator *= (n - i);
            denominator *= (i + 1);
        }
        return numerator / denominator;
    }

    //------------------------------------------------------------------
    //
    // Renders a Bezier curve based on the input parameters; using the matrix form.
    // This follows the Mathematics for Game Programmers form.
    //
    //------------------------------------------------------------------
    function drawCurveBezierMatrix(controls, segments, showPoints, showLine, showControl, lineColor) {
        // Create an array to store the computed points
        let points = [];

        // calculate points
        let p0 = controls[0] // start
        let p1 = controls[1] 
        let p2 = controls[2]
        let p3 = controls[3] // end

        // divide curve into segments
        for (let u = 0; u <= 1; u += 1 / segments) {
            // calc t^2 and t^3
            let u2 = u  * u
            let u3 = u2 * u

            // calculate basis functions
            let h1 =      u3
            let h2 = -3 * u3 + 3 * u2
            let h3 =  3 * u3 - 6 * u2 + 3 * u
            let h4 = -1 * u3 - 3 * u2 - 3 * u + 1

            // calc x and y & store point
            points.push({
                x: Math.round(h1 * p0.x + h2 * p1.x + h3 * p2.x + h4 * p3.x),
                y: Math.round(h1 * p0.y + h2 * p1.y + h3 * p2.y + h4 * p3.y),
            })
        }

        console.log(points)

        // draw curve
        drawLines(points, lineColor)

        // handle boolean debug info
        // print line between related control points
        if (showLine) {
            // drawLines(controls, lineColorDEBUG)
            for (let i = 0; i < controls.length -1; i++) {
                drawLine(controls[i].x, controls[i].y, controls[i+1].x, controls[i+1].y, lineColorDEBUG)
            }
        }

        // print calculated points
        if (showPoints) {
            for (let i = 0; i < points.length; i++) {
                drawPoint(points[i].x, points[i].y, pointColorDEBUG)
            }
        }
        
        // print control points
        if (showControl) {
            for (let i = 0; i < controls.length; i++) {
                drawPoint(controls[i].x, controls[i].y, controlColorDEBUG)
            }
        }
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

// --ASSIGN 3-----------------------------------------------------------

    //------------------------------------------------------------------
    //
    // Renders a primitive of the form: {
    //    verts: [ {x, y}, ...],    // Must have at least 2 verts
    //    center: { x, y }
    // }
    // 
    // connect: If true, the last vertex and first vertex have a line drawn between them.
    //
    // color: The color to use when drawing the lines
    //
    //------------------------------------------------------------------
    function drawPrimitive(primitive, connect, color) {
        // return if not enough vertices
        if (primitive.verts.length < 2) {
            console.log("NOT ENOUGH VERTS")
            return
        }

        // get points in world coords
        let pointsInWorldCoords = []
        for (let i = 0; i < primitive.verts.length; i++) {
            // console.log(points[i].x + center.x)
            // console.log(points[i].y + center.y)
            pointsInWorldCoords.push({
                x: primitive.verts[i].x + primitive.center.x,
                y: primitive.verts[i].y + primitive.center.y
            })
        }
        
        // draw prim
        drawLines(pointsInWorldCoords, color)

        if (connect) {
            drawLine(pointsInWorldCoords[primitive.verts.length - 1].x, pointsInWorldCoords[primitive.verts.length - 1].y, pointsInWorldCoords[0].x, pointsInWorldCoords[0].y, color)
        }
    }

    //------------------------------------------------------------------
    //
    // Translates a primitive of the form: {
    //    verts: [],    // Must have at least 2 verts
    //    center: { x, y }
    // }
    //
    // distance: { x, y }
    //
    //------------------------------------------------------------------
    function translatePrimitive(primitive, distance) {
        // return if not enough vertices
        if (primitive.verts.length < 2) {
            console.log("NOT ENOUGH VERTS")
            return
        }

        // keep it functional
        return {verts: primitive.verts, center: {
            x: primitive.center.x + distance.x,
            y: primitive.center.y + distance.y, // should be subtract but that breaks it
        }}
    }

// --ASSIGN 3 END-------------------------------------------------------

    //
    // This is what we'll export as the rendering API
    const api = {
        clear: clear,
        drawPixel: drawPixel,
        drawLine: drawLine,
        drawCurve: drawCurve,
        drawPrimitive: drawPrimitive,
        translatePrimitive: translatePrimitive,
        // scalePrimitive: scalePrimitive,
        // rotatePrimitive: rotatePrimitive,
        // translateCurve: translateCurve,
        // scaleCurve: scaleCurve,
        // rotateCurve: rotateCurve
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


MySample.main = (function(graphics) {
    'use strict';

    let previousTime = performance.now();

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    //
    //------------------------------------------------------------------
    function update(elapsedTime) {

    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        graphics.clear();

    }

    function debugRenderCurves() {
        // cardinal - type: 0
        // graphics.drawCurve(0, [{x: 100, y: 500}, {x: 200, y: 600}, {x: 700, y: 700}, {x: 900, y: 500}, 1], 10, true, true, true, "aqua")
        // bezier - type: 1
        let bezierControls = [{x: 100, y: 500}, {x: 300, y: 300}, {x: 500, y: 700}, {x: 900, y: 300}]
        let translatedBezier = graphics.translateCurve(1, bezierControls, {x: 100, y: 100})
        let scaledBezier = graphics.scaleCurve(1, bezierControls, {x: 0.5, y: 0.5})
        let rotatedBezier = graphics.rotateCurve(1, bezierControls, 45)
        console.log(scaledBezier)
        graphics.drawCurve(1, bezierControls, 1000, false, false, false, "aqua")
        // graphics.drawCurve(1, translatedBezier, 1000, false, false, false, "aqua")
        graphics.drawCurve(1, scaledBezier, 1000, false, false, false, "aqua")
        graphics.drawCurve(1, rotatedBezier, 1000, false, false, false, "aqua")
    }

    function debugRender() {
        let square1 = {verts: [{x: -100, y: -100}, {x: -100, y: 100}, {x: 100, y: 100}, {x: 100, y: -100}, ], center: {x: 250, y: 250}}
        graphics.drawPrimitive(square1, true, "aqua")
        let square2 = graphics.translatePrimitive(square1, {x: -100, y: -100})
        graphics.drawPrimitive(square2, true, "red")
        let square3 = graphics.translatePrimitive(square1, {x: -200, y: 100})
        graphics.drawPrimitive(square3, true, "gold")
        let square4 = graphics.scalePrimitive(square1, {x: 0.66, y: 0.66})
        graphics.drawPrimitive(square4, true, "orange")
        let square5 = graphics.scalePrimitive(square4, {x: 0.75, y: 0.75})
        graphics.drawPrimitive(square5, true, "pink")
        let square6 = graphics.scalePrimitive(square1, {x: 0.5, y: 0.5})
        graphics.drawPrimitive(square6, true, "aqua")
        let square7 = graphics.rotatePrimitive(square1, 45)
        graphics.drawPrimitive(square7, true, "pink")
    }

    //------------------------------------------------------------------
    //
    // This is the animation loop.
    //
    //------------------------------------------------------------------
    function animationLoop(time) {

        let elapsedTime = time - previousTime;
        previousTime = time;
        update(elapsedTime);
        render();

        requestAnimationFrame(animationLoop);
    }

    console.log('initializing...');
    debugRender()
    debugRenderCurves()
    // requestAnimationFrame(animationLoop);

}(MySample.graphics));


MySample.main = (function(graphics) {
    'use strict';

    let previousTime = performance.now();
    let startTime = performance.now();
    let totalTime = 0;

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    //
    //------------------------------------------------------------------
    function update(elapsedTime) {
        let delta = 0.0005 * elapsedTime

        // oscillate the scale value of the violet square
        scale = oscillateValue(totalTime, 0, 1, 5000)
        // translate the value 
        if (square2.center.x < 100 || square2.center.x > 900) { shrinkingX = !shrinkingX }
        if (shrinkingX) { square2 = graphics.translatePrimitive(square2, {x: 1, y: 0}) }
        else { square2 = graphics.translatePrimitive(square2, {x: -1, y: 0}) }
    
        if (square3.center.y < 100 || square3.center.y > 900) { shrinkingY = !shrinkingY }
        if (shrinkingY) { square3 = graphics.translatePrimitive(square3, {x: 0, y: 1}) }
        else { square3 = graphics.translatePrimitive(square3, {x: 0, y: -1}) }

        bezierControls = graphics.rotateCurve(1, bezierControls, delta)
        square1 = graphics.scalePrimitive(square, { x: scale, y: scale})
        triangle = graphics.rotatePrimitive(triangle, delta)
    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        graphics.clear();
        graphics.drawCurve(1, bezierControls, 1000, false, false, false, "lightgreen")
        graphics.drawPrimitive(square1, true, "violet")
        graphics.drawPrimitive(triangle, true, "yellow")
        graphics.drawPrimitive(square2, true, "lightblue")
        graphics.drawPrimitive(square3, true, "white")
    }

    function debugRenderCurves() {
        // cardinal - type: 0
        // graphics.drawCurve(0, [{x: 100, y: 500}, {x: 200, y: 600}, {x: 700, y: 700}, {x: 900, y: 500}, 1], 10, true, true, true, "aqua")
        // bezier - type: 1
        let translatedBezier = graphics.translateCurve(1, bezierControls, {x: 100, y: 100})
        let scaledBezier = graphics.scaleCurve(1, bezierControls, {x: 0.5, y: 0.5})
        let rotatedBezier = graphics.rotateCurve(1, bezierControls, 45)
        // console.log(scaledBezier)
        graphics.drawCurve(1, bezierControls, 1000, false, false, false, "aqua")
        // graphics.drawCurve(1, translatedBezier, 1000, false, false, false, "aqua")
        graphics.drawCurve(1, scaledBezier, 1000, false, false, false, "aqua")
        graphics.drawCurve(1, rotatedBezier, 1000, false, false, false, "aqua")
    }

    function debugRender() {
        let square1 = square
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
        totalTime = Math.round(totalTime + elapsedTime);
        update(elapsedTime);
        render();

        requestAnimationFrame(animationLoop);
    }


    // init var for update and animation loop
    // curve
    let bezierControls = [{x: 100, y: 500}, {x: 300, y: 300}, {x: 500, y: 700}, {x: 900, y: 300}]
    let square = {verts: [{x: -100, y: -100}, {x: -100, y: 100}, {x: 100, y: 100}, {x: 100, y: -100}, ], center: {x: 250, y: 250}}
    let square1 = square
    let square2 = square
    let square3 = square
    let shrinkingX = false
    let shrinkingY = false
    let scale = 1
    let triangle =  {verts: [{x: -200, y: 0}, {x: 200, y: 0}, {x: 0, y: -300}, ], center: { x: 700, y: 500}}



    console.log('initializing...');
    debugRender()
    debugRenderCurves()
    console.log('running...');
    requestAnimationFrame(animationLoop);


    // GPT Generated Functions - helping for animation
    function oscillateValue(time, minValue, maxValue, duration) {
        let range = maxValue - minValue;
        let normalizedTime = (time % duration) / duration; // Normalize time between 0 and 1
        let scaledValue = range * Math.sin(2 * Math.PI * normalizedTime); // Scale the sine wave to the desired range
        let oscillatedValue = scaledValue + (maxValue + minValue) / 2; // Translate the value to the desired range center
        return oscillatedValue;
      }

}(MySample.graphics));


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
        // hermite
        // graphics.drawCurve(0, [{x: 100, y: 500},  {x: 100, y: 100}, {x: 900, y: 900}, {x: 900, y: 500}], 1000, true, true, true, "aqua")
        // cardinal
        // graphics.drawCurve(1, [{x: 100, y: 500}, {x: 200, y: 600}, {x: 700, y: 700}, {x: 900, y: 500}, 1], 1000, true, true, true, "aqua")
        // bezier
        // graphics.drawCurve(2, [{x: 100, y: 500}, {x: 300, y: 300}, {x: 500, y: 700}, {x: 900, y: 300}], 1000, true, true, true, "aqua")
        // matrix bezier
        // graphics.drawCurve(3, [{x: 100, y: 500}, {x: 300, y: 300}, {x: 500, y: 700}, {x: 900, y: 300}], 1000, true, true, true, "aqua")
    }

    function debugRender() {
        // graphics.drawLine(100, 100, 300, 100, "red")
        // graphics.drawLine(100, 100, 100, 300, "purple")
        let primitive1 = {verts: [{x: -100, y: -100}, {x: -100, y: 100}, {x: 100, y: 100}, {x: 100, y: -100}, ], center: {x: 250, y: 250}}
        graphics.drawPrimitive(primitive1, true, "aqua")
        let primitive2 = graphics.translatePrimitive(primitive1, {x: 100, y: 100})
        graphics.drawPrimitive(primitive2, true, "red")
        // let primitive3 = graphics.translatePrimitive(primitive2, {x: 100, y: 100})
        // graphics.drawPrimitive(primitive3, true, "gold")
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
    // requestAnimationFrame(animationLoop);

}(MySample.graphics));

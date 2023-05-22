
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
    // requestAnimationFrame(animationLoop);
    // DEBUG
    graphics.drawCurve(0, [{x: 100, y: 500}, {x: 900, y: 500}, {x: 200, y: 0}, {x: -200, y: 0}], 100, true, true, false, "aqua")
    graphics.drawCurve(0, [{x: 100, y: 500}, {x: 900, y: 500}, {x: 200, y: 500}, {x: -200, y: -500}], 100, true, false, false, "lightpink")
    graphics.drawCurve(1, [
        {x:   0, y: 500}, {x: 100, y: 300}, {x: 200, y: 700}, {x: 300, y: 200}, {x: 400, y: 800},
        {x: 500, y: 400}, {x: 600, y: 600}, {x: 700, y: 500}, {x: 800, y: 500}, {x: 900, y: 700}
    ], 10, true, false, false, "white")
    // END DEBUG

}(MySample.graphics));

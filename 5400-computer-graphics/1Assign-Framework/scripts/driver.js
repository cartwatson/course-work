
MySample.main = (function(graphics) {
    'use strict';

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    //
    //------------------------------------------------------------------
    function update(elapsedTime) {
        const rotationRate = 0.0005;

        ptEnd = {
            x: (ptEnd.x - ptCenter.x) * Math.cos(rotationRate *  elapsedTime) - (ptEnd.y - ptCenter.y) * Math.sin(rotationRate *  elapsedTime) + ptCenter.x,
            y: (ptEnd.y - ptCenter.y) * Math.cos(rotationRate *  elapsedTime) + (ptEnd.x - ptCenter.x) * Math.sin(rotationRate *  elapsedTime) + ptCenter.y
        }
    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        graphics.clear();

        graphics.drawLine(ptCenter.x, ptCenter.y, Math.trunc(ptEnd.x), Math.trunc(ptEnd.y));
    }

    //------------------------------------------------------------------
    //
    // This is the animation loop.
    //
    //------------------------------------------------------------------
    function animationLoop(time) {

        update(); // strictly logical
        render(); // move framebuffers

        requestAnimationFrame(animationLoop); // kinda like gameloop/step
    }

    console.log('initializing...');
    
    // get center
    let ptCenter = {
        x: graphics.sizeX / 2,
        y: graphics.sizeY / 2
    }

    // DEBUG
    // console.log("OCTANT 0"); graphics.drawLine(ptCenter.x, ptCenter.y, 80, 80, "white") // octant 0
    console.log("OCTANT 1"); graphics.drawLine(ptCenter.x, ptCenter.y, 100, 50, "green") // octant 1
    console.log("OCTANT 2"); graphics.drawLine(ptCenter.x, ptCenter.y, 100, 100, "blue") // octant 2
    // console.log("OCTANT 3"); graphics.drawLine(ptCenter.x, ptCenter.y, 100, 135, "aqua") // octant 3
    console.log("OCTANT 5"); graphics.drawLine(ptCenter.x, ptCenter.y, 50, 100, "pink") // octant 5
    console.log("OCTANT 6"); graphics.drawLine(ptCenter.x, ptCenter.y, 50, 50, "red") // octant 6

    // DEBUG

    // requestAnimationFrame(animationLoop); 

}(MySample.graphics));


MySample.main = (function(graphics) {
    'use strict';

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    //
    //------------------------------------------------------------------
    function update() {
        let rotationRate = 0.0005;
        let elapsedTime = (startTime - performance.now()) / 100;

        ptEnd = {
            x: (ptEnd.x - ptCenter.x) * Math.cos(rotationRate *  elapsedTime) - (ptEnd.y - ptCenter.y) * Math.sin(rotationRate * elapsedTime) + ptCenter.x,
            y: (ptEnd.y - ptCenter.y) * Math.cos(rotationRate *  elapsedTime) + (ptEnd.x - ptCenter.x) * Math.sin(rotationRate * elapsedTime) + ptCenter.y
        }

        ptEnd2 = {
            x: (ptEnd.y - ptCenter.y) * Math.cos(rotationRate *  elapsedTime) + (ptEnd.x - ptCenter.x) * Math.sin(rotationRate * elapsedTime) + ptCenter.y,
            y: (ptEnd.x - ptCenter.x) * Math.cos(rotationRate *  elapsedTime) - (ptEnd.y - ptCenter.y) * Math.sin(rotationRate * elapsedTime) + ptCenter.x
        }
    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        graphics.clear();

        graphics.drawLine(ptCenter.x, ptCenter.y, Math.trunc(ptEnd.x), Math.trunc(ptEnd.y), "aqua");
        graphics.drawLine(ptCenter.x, ptCenter.y, Math.trunc(ptEnd2.x), Math.trunc(ptEnd2.y), "pink");
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

    let ptEnd  = { x: 0, y: 0 }
    let ptEnd2 = { x: 0, y: 0 }
    let startTime = performance.now();

    // DEBUG {
    // graphics.drawLine(ptCenter.x, ptCenter.y, 100, 30, "white") // octant 0
    // graphics.drawLine(ptCenter.x, ptCenter.y, 100, 60, "green") // octant 1
    // graphics.drawLine(ptCenter.x, ptCenter.y, 100, 90, "blue") // octant 2
    // graphics.drawLine(ptCenter.x, ptCenter.y, 100, 135, "aqua") // octant 3
    // graphics.drawLine(ptCenter.x, ptCenter.y, 60, 135, "purple") // octant 4
    // graphics.drawLine(ptCenter.x, ptCenter.y, 50, 90, "pink") // octant 5
    // graphics.drawLine(ptCenter.x, ptCenter.y, 50, 50, "red") // octant 6
    // graphics.drawLine(ptCenter.x, ptCenter.y, 60, 30, "orange") // octant 7
    // } DEBUG


    requestAnimationFrame(animationLoop); 

}(MySample.graphics));

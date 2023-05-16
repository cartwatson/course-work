
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
    // graphics.drawPixel(ptCenter.x, ptCenter.y, "pink")
    // graphics.drawLine(ptCenter.x, ptCenter.y, 100, 75, "pink")
    // graphics.drawLine(ptCenter.x, ptCenter.y, 100, 74, "pink")
    graphics.drawLine(ptCenter.x, ptCenter.y, 100, 75, "blue")
    graphics.drawLine(ptCenter.x, ptCenter.y, 100, 100, "green")
    // graphics.drawLine(50, 50, 100, 50, "blue")
    // graphics.drawLine(50, 50, 100, 80, "green")

    // graphics.drawPixel(75, 75, "red")
    // graphics.drawPixel(100, 75, "red")
    // DEBUG

    // requestAnimationFrame(animationLoop); 

}(MySample.graphics));

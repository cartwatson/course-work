
MySample.main = (function() {
    'use strict';

    // Step 1 : Define an HTML <canvas> Element
    let canvas = document.getElementById('canvas-main');
    // Step 2 : Obtain the WebGL Context
    let gl = canvas.getContext('webgl2');
    // Step 3 : Prepare Raw Data
    // create buffer objects
    let vertices = new Float32Array([
        0.0, 0.5, 0.0,
        0.5, 0.0, 0.0,
        -0.5, 0.0, 0.0
    ]);
    let vertexColors = new Float32Array([
        .0, 0.0, 0.0,
        1.0, 1.0, 1.0,
        0.0, 0.0, 1.0
    ]);
    let indices = new Uint16Array([ 0, 2, 1 ]);

    // Step 4 : Prepare Buffer Objects
    // vertex buffer
    let vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);

    // color buffer
    let vertexColorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexColorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertexColors, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);

    // index buffer
    let indexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);
    
    // Step 5 : Prepare Shaders
    // Vertex Shader
    // let vertexShaderSource = loadFileFromServer('../shaders/simple.vert') // TODO: make this work later
    let vertexShaderSource = `#version 300 es\nin vec4 aPosition; in vec4 aColor; out vec4 vColor; void main() { gl_Position = aPosition; vColor = aColor; }`
    let vertexShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertexShader, vertexShaderSource);
    gl.compileShader(vertexShader);
    console.log(gl.getShaderInfoLog(vertexShader)); // for debugging

    // Fragment Shader
    // let fragmentShaderSource = loadFileFromServer('../shaders/simple.frag') // TODO: make this work later
    let fragmentShaderSource = `#version 300 es\nprecision lowp float; in vec4 vColor; out vec4 outColor; void main() { outColor = vColor; }`
    let fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragmentShader, fragmentShaderSource);
    gl.compileShader(fragmentShader);

    // Create the Shader Program
    let shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader);
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);
    gl.useProgram(shaderProgram);

    // STEP 6 : Specify Shader & Buffer Object Attributes
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    let position = gl.getAttribLocation(shaderProgram, 'aPosition');
    gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 3, gl.FLOAT, false, vertices.BYTES_PER_ELEMENT * 3, 0);

    gl.bindBuffer(gl.ARRAY_BUFFER, vertexColorBuffer);
    let color = gl.getAttribLocation(shaderProgram, 'aColor');
    gl.enableVertexAttribArray(color);
    gl.vertexAttribPointer(color, 3, gl.FLOAT, false, vertexColors.BYTES_PER_ELEMENT * 3, 0);

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    //
    //------------------------------------------------------------------
    function update() {

    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        // Step 8 : Reset Framebuffer & Depth Buffer
        gl.clearColor(
            0.3921568627450980392156862745098,
            0.58431372549019607843137254901961,
            0.92941176470588235294117647058824,
            1.0
        );
        gl.clearDepth(1.0);
        gl.depthFunc(gl.LEQUAL);
        gl.enable(gl.DEPTH_TEST);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        // Step 9 : Draw the Primitives
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
        gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0);
    }

    //------------------------------------------------------------------
    //
    // This is the animation loop.
    //
    //------------------------------------------------------------------
    function animationLoop(time) {

        update();
        render();

        requestAnimationFrame(animationLoop);
    }

    console.log('initializing...');
    // Step 7 : Request Animation Frame
    requestAnimationFrame(animationLoop);
}());

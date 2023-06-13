
MySample.main = (function() {
    'use strict';

    // Step 1 : Define an HTML <canvas> Element
    let canvas = document.getElementById('canvas-main');
    // Step 2 : Obtain the WebGL Context
    let gl = canvas.getContext('webgl2');
    // Step 3 : Prepare Raw Data
    // create buffer objects
    // tetrahedron 0-3
    // cube        4-11
    // octahedron  12-17
    let vertices = new Float32Array([
        // tetrahedron
        0.0, 0.25, -0.125,
        0.25, 0.0, -0.125,
        -0.25, 0.0, -0.125,
        0.0, 0.15, 0.125,
        // cube
        0.75, 0.75, -0.25,
        0.75, 0.25, -0.25,
        0.25, 0.25, -0.25,
        0.25, 0.75, -0.25,
        0.75, 0.75,  0.25,
        0.75, 0.25,  0.25,
        0.25, 0.25,  0.25,
        0.25, 0.75,  0.25,
       // octahedron
       -0.25, -0.5, -0.25, // back right
       -0.75, -0.5, -0.25, // back left
       -0.25, -0.5,  0.25, // front right
       -0.75, -0.5,  0.25, // front left
       -0.5,  -0.25, 0.0, // top
       -0.5, -0.75, 0.0,  // bottom
    ]);
    let vertexColors = new Float32Array([
        // tetrahedron
        0.0, 0.0, 0.0,
        1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0,
        // cube
        0.0, 0.0, 0.0, // black
        1.0, 0.0, 0.0, // red
        0.0, 1.0, 0.0, // blue
        0.0, 0.0, 1.0, // green
        1.0, 1.0, 1.0, // white
        1.0, 1.0, 0.0, // purple
        0.0, 1.0, 1.0, // cyan
        1.0, 0.0, 1.0, // fuschia
        // octahedron
        1.0, 0.0, 0.0, // red
        0.0, 1.0, 0.0, // blue
        0.0, 0.0, 1.0, // green
        1.0, 1.0, 0.0, // purple
        0.0, 1.0, 1.0, // cyan
        1.0, 0.0, 1.0, // fuschia
    ]);
    let indices = new Uint16Array([
        // tetrahedron
        0, 1, 2,
        0, 2, 3,
        0, 3, 1,
        1, 3, 2,
        // cube
        4,  6,  5,
        4,  7,  6,
        4,  8,  5,
        8,  5,  9,
        8,  9,  11,
        11, 9,  10,
        7,  10, 6,
        11, 10, 7,
        7,  4,  8,
        7,  8,  11,
        10, 5,  6,
        10, 9,  5,
        // octahedron
        12, 16, 14,
        14, 16, 15,
        15, 16, 13,
        13, 16, 12,
        14, 17, 12,
        12, 17, 13,
        13, 17, 15,
        15, 17, 14,
    ]);

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
    // let vertexShaderSource = loadFileFromServer('../shaders/simple.vert') // TODO: make this work using promise chaining
    let vertexShaderSource = `#version 300 es\nuniform mat4 uProjection; uniform mat4 uThing; in vec4 aPosition; in vec4 aColor; out vec4 vColor; void main() { gl_Position = uThing * aPosition; vColor = aColor; }`
    let vertexShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertexShader, vertexShaderSource);
    gl.compileShader(vertexShader);

    // Fragment Shader
    // let fragmentShaderSource = loadFileFromServer('../shaders/simple.frag') // TODO: make this work using promise chaining
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
    let scale = 0.5;
    let t = 0;
    let theta = 0;

    function update() {
        theta += 0.01;
        t += 0.0005;
        if (t > 1) { t = 0; }

        let uTS = [
            scale, 0, 0, 0,
            0, scale, 0, 0,
            0, 0, scale, 0,
            t, t, t, 1,
        ];

        let uR_Y = [
            Math.cos(theta), 0, Math.sin(theta), 0,
            0, 1, 0, 0,
            -Math.sin(theta), 0, Math.cos(theta), 0,
            0, 0, 0, 1,
        ];

        let uR_X = [
            1, 0, 0, 0,
            0, Math.cos(theta), -Math.sin(theta), 0,
            0, Math.sin(theta), Math.cos(theta), 0,
            0, 0, 0, 1,
        ];

        let uRotation = multiplyMatrix4x4(uR_Y, uR_X);

        let location = gl.getUniformLocation(shaderProgram, 'uThing');
        let uTSR = multiplyMatrix4x4(uTS, uRotation);
        gl.uniformMatrix4fv(location, false, uTSR);
    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        // Step 8 : Reset Framebuffer & Depth Buffer
        gl.clearColor(
            0.392156862740980392156862745098,
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

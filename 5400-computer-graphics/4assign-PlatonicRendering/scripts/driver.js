
MySample.main = (function() {
    'use strict';

    // Step 1 : Define an HTML <canvas> Element
    let canvas = document.getElementById('canvas-main');
    // Step 2 : Obtain the WebGL Context
    let gl = canvas.getContext('webgl2');
    // Step 3 : Prepare Raw Data
    // create buffer objects
    // TETRAHEDRON
    let tetrahedronVertices = new Float32Array([
        0.0, 0.5, 0.0,
        0.5, 0.0, 0.0,
        -0.5, 0.0, 0.0,
        0.0, 0.25, 0.0
    ]);
    let tetrahedronVertexColors = new Float32Array([
        0.0, 0.0, 0.0,
        1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0,
    ]);
    let tetrahedronIndices = new Uint16Array([
        0, 1, 2,
        0, 2, 3,
        0, 3, 1,
        1, 3, 2,
    ]);

    // CUBE
    let cubeVertices = new Float32Array([
         0.25,  0.25, -0.25,
         0.25, -0.25, -0.25,
        -0.25, -0.25, -0.25,
        -0.25,  0.25, -0.25,
         0.25,  0.25,  0.25,
         0.25, -0.25,  0.25,
        -0.25, -0.25,  0.25,
        -0.25,  0.25,  0.25,
    ]);
    let cubeVertexColors = new Float32Array([
        0.0, 0.0, 0.0, // black
        1.0, 0.0, 0.0, // red
        0.0, 1.0, 0.0, // blue
        0.0, 0.0, 1.0, // green
        1.0, 1.0, 1.0, // white
        1.0, 1.0, 0.0, // purple
        0.0, 1.0, 1.0, // cyan
        1.0, 0.0, 1.0, // fuschia
    ]);
    let cubeIndices = new Uint16Array([
        // back
        0, 2, 1,
        0, 3, 2,
        // right
        0, 1, 4,
        4, 1, 5,
        // front
        4, 5, 7,
        7, 5, 6,
        // left
        3, 6, 2,
        7, 6, 3,
        // top
        3, 0, 4,
        3, 4, 7,
        // bottom
        6, 1, 2,
        6, 5, 1,
    ]);

    // OCTAHEDRON
    let octahedronVertices = new Float32Array([
         0.25, 0.0, -0.25, // back right
        -0.25, 0.0, -0.25, // back left
         0.25, 0.0,  0.25, // front right
        -0.25, 0.0,  0.25, // front left
         0.0,  0.25, 0.0, // top
         0.0, -0.25, 0.0,  // bottom
    ]);
    let octahedronVertexColors = new Float32Array([
        1.0, 0.0, 0.0, // red
        0.0, 1.0, 0.0, // blue
        0.0, 0.0, 1.0, // green
        1.0, 1.0, 0.0, // purple
        0.0, 1.0, 1.0, // cyan
        1.0, 0.0, 1.0, // fuschia
    ]);
    let octahedronIndices = new Uint16Array([
        0, 4, 2,
        2, 4, 3,
        3, 4, 1,
        1, 4, 0,
        2, 5, 0,
        0, 5, 1,
        1, 5, 3,
        3, 5, 2,
    ]);

    // Step 4 : Prepare Buffer Objects
    // TETRAHEDRON BUFFER OBJECTS
    // vertex buffer
    let tetrahedronVertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, tetrahedronVertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, tetrahedronVertices, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);
    // color buffer
    let tetrahedronVertexColorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, tetrahedronVertexColorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, tetrahedronVertexColors, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);
    // index buffer
    let tetrahedronIndexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, tetrahedronIndexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, tetrahedronIndices, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);

    // // CUBE BUFFER OBJECTS
    // // vertex buffer
    // let cubeVertexBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ARRAY_BUFFER, cubeVertexBuffer);
    // gl.bufferData(gl.ARRAY_BUFFER, cubeVertices, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ARRAY_BUFFER, null);
    // // color buffer
    // let cubeVertexColorBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ARRAY_BUFFER, cubeVertexColorBuffer);
    // gl.bufferData(gl.ARRAY_BUFFER, cubeVertexColors, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ARRAY_BUFFER, null);
    // // index buffer
    // let cubeIndexBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, cubeIndexBuffer);
    // gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, cubeIndices, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);

    // // OCTOHEDRON BUFFER OBJECTS
    // // vertex buffer
    // let octahedronVertexBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ARRAY_BUFFER, octahedronVertexBuffer);
    // gl.bufferData(gl.ARRAY_BUFFER, octahedronVertices, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ARRAY_BUFFER, null);
    // // color buffer
    // let octahedronVertexColorBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ARRAY_BUFFER, octahedronVertexColorBuffer);
    // gl.bufferData(gl.ARRAY_BUFFER, octahedronVertexColors, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ARRAY_BUFFER, null);
    // // index buffer
    // let octahedronIndexBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, octahedronIndexBuffer);
    // gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, octahedronIndices, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);
    
    // Step 5 : Prepare Shaders
    // TETRAHEDRON
    // Vertex Shader
    // let vertexShaderSource = loadFileFromServer('../shaders/simple.vert') // TODO: make this work using promise chaining
    let vertexShaderSource = `#version 300 es\nuniform mat4 uProjection; uniform mat4 uThing; in vec4 aPosition; in vec4 aColor; out vec4 vColor; void main() { gl_Position = uProjection * uThing * aPosition; vColor = aColor; }`
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

    // // CUBE
    // // Vertex Shader
    // // let vertexShaderSource = loadFileFromServer('../shaders/simple.vert') // TODO: make this work using promise chaining
    // let cubeVertexShaderSource = `#version 300 es\nuniform mat4 uProjection; uniform mat4 uThing; in vec4 aPosition; in vec4 aColor; out vec4 vColor; void main() { gl_Position = uProjection * uThing * aPosition; vColor = aColor; }`
    // let cubeVertexShader = gl.createShader(gl.VERTEX_SHADER);
    // gl.shaderSource(cubeVertexShader, cubeVertexShaderSource);
    // gl.compileShader(cubeVertexShader);

    // // Fragment Shader
    // // let fragmentShaderSource = loadFileFromServer('../shaders/simple.frag') // TODO: make this work using promise chaining
    // let cubeFragmentShaderSource = `#version 300 es\nprecision lowp float; in vec4 vColor; out vec4 outColor; void main() { outColor = vColor; }`
    // let cubeFragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    // gl.shaderSource(cubeFragmentShader, cubeFragmentShaderSource);
    // gl.compileShader(cubeFragmentShader);

    // // Create the Shader Program
    // let cubeShaderProgram = gl.createProgram();
    // gl.attachShader(cubeShaderProgram, cubeVertexShader);
    // gl.attachShader(cubeShaderProgram, cubeFragmentShader);
    // gl.linkProgram(cubeShaderProgram);
    // gl.useProgram(cubeShaderProgram);

    // // OCTAHEDRON
    // // Vertex Shader
    // // let vertexShaderSource = loadFileFromServer('../shaders/simple.vert') // TODO: make this work using promise chaining
    // let octahedronVertexShaderSource = `#version 300 es\nuniform mat4 uProjection; uniform mat4 uThing; in vec4 aPosition; in vec4 aColor; out vec4 vColor; void main() { gl_Position = uProjection * uThing * aPosition; vColor = aColor; }`
    // let octahedronVertexShader = gl.createShader(gl.VERTEX_SHADER);
    // gl.shaderSource(octahedronVertexShader, octahedronVertexShaderSource);
    // gl.compileShader(octahedronVertexShader);

    // // Fragment Shader
    // // let fragmentShaderSource = loadFileFromServer('../shaders/simple.frag') // TODO: make this work using promise chaining
    // let octahedronFragmentShaderSource = `#version 300 es\nprecision lowp float; in vec4 vColor; out vec4 outColor; void main() { outColor = vColor; }`
    // let octahedronFragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    // gl.shaderSource(octahedronFragmentShader, octahedronFragmentShaderSource);
    // gl.compileShader(octahedronFragmentShader);

    // // Create the Shader Program
    // let octahedronShaderProgram = gl.createProgram();
    // gl.attachShader(octahedronShaderProgram, octahedronVertexShader);
    // gl.attachShader(octahedronShaderProgram, octahedronFragmentShader);
    // gl.linkProgram(octahedronShaderProgram);
    // gl.useProgram(octahedronShaderProgram);

    // STEP 6 : Specify Shader & Buffer Object Attributes
    // TETRAHEDRON
    gl.bindBuffer(gl.ARRAY_BUFFER, tetrahedronVertexBuffer);
    let tetrahedronPosition = gl.getAttribLocation(shaderProgram, 'aPosition');
    gl.enableVertexAttribArray(tetrahedronPosition);
    gl.vertexAttribPointer(tetrahedronPosition, 3, gl.FLOAT, false, tetrahedronVertices.BYTES_PER_ELEMENT * 3, 0);

    gl.bindBuffer(gl.ARRAY_BUFFER, tetrahedronVertexColorBuffer);
    let tetrahedronColor = gl.getAttribLocation(shaderProgram, 'aColor');
    gl.enableVertexAttribArray(tetrahedronColor);
    gl.vertexAttribPointer(tetrahedronColor, 3, gl.FLOAT, false, tetrahedronVertexColors.BYTES_PER_ELEMENT * 3, 0);

    // // CUBE
    // gl.bindBuffer(gl.ARRAY_BUFFER, cubeVertexBuffer);
    // let cubePosition = gl.getAttribLocation(cubeShaderProgram, 'aPosition');
    // gl.enableVertexAttribArray(cubePosition);
    // gl.vertexAttribPointer(cubePosition, 3, gl.FLOAT, false, cubeVertices.BYTES_PER_ELEMENT * 3, 0);

    // gl.bindBuffer(gl.ARRAY_BUFFER, cubeVertexColorBuffer);
    // let cubeColor = gl.getAttribLocation(cubeShaderProgram, 'aColor');
    // gl.enableVertexAttribArray(cubeColor);
    // gl.vertexAttribPointer(cubeColor, 3, gl.FLOAT, false, cubeVertexColors.BYTES_PER_ELEMENT * 3, 0);

    // // OCTOHEDRON
    // gl.bindBuffer(gl.ARRAY_BUFFER, octahedronVertexBuffer);
    // let octahedronPosition = gl.getAttribLocation(octahedronShaderProgram, 'aPosition');
    // gl.enableVertexAttribArray(octahedronPosition);
    // gl.vertexAttribPointer(octahedronPosition, 3, gl.FLOAT, false, cubeVertices.BYTES_PER_ELEMENT * 3, 0);

    // gl.bindBuffer(gl.ARRAY_BUFFER, octahedronVertexColorBuffer);
    // let octahedronColor = gl.getAttribLocation(octahedronShaderProgram, 'aColor');
    // gl.enableVertexAttribArray(octahedronColor);
    // gl.vertexAttribPointer(octahedronColor, 3, gl.FLOAT, false, cubeVertexColors.BYTES_PER_ELEMENT * 3, 0);

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    //
    //------------------------------------------------------------------
    let scale = 1;
    let tX = 0;
    let tY = 0;
    let tZ = 0;

    function update() {
        let uTS = [
            scale, 0, 0, 0,
            0, scale, 0, 0,
            0, 0, scale, 0,
            tX, tY, tZ, 1,
        ];

        let uRotation = [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ];

        let location = gl.getUniformLocation(shaderProgram, 'uThing');
        gl.uniformMatrix4fv(location, false, multiplyMatrix4x4(uTS, uRotation));

        // let cubeLocation = gl.getUniformLocation(cubeShaderProgram, 'uThing');
        // gl.uniformMatrix4fv(cubeLocation, false, multiplyMatrix4x4(uTS, uRotation));

        // let octahedronLocation = gl.getUniformLocation(octahedronShaderProgram, 'uThing');
        // gl.uniformMatrix4fv(octahedronLocation, false, multiplyMatrix4x4(uTS, uRotation));
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
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, tetrahedronIndexBuffer);
        gl.drawElements(gl.TRIANGLES, tetrahedronIndices.length, gl.UNSIGNED_SHORT, 0);

        // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, cubeIndexBuffer);
        // gl.drawElements(gl.TRIANGLES, cubeIndices.length, gl.UNSIGNED_SHORT, 0);

        // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, octahedronIndexBuffer);
        // gl.drawElements(gl.TRIANGLES, octahedronIndices.length, gl.UNSIGNED_SHORT, 0);
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

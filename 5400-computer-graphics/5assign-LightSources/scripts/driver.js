MySample.main = (function() {
    'use strict';

    // Step 1 : Define an HTML <canvas> Element
    let canvas = document.getElementById('canvas-main');
    // Step 2 : Obtain the WebGL Context
    let gl = canvas.getContext('webgl2');

    // file paths
    const bunnyFilePath = '../models/bun_zipper.ply'
    const dragonFilePath = '../models/dragon_vrip.ply'
    // const armadilloFilePath = '../models/armadillo.ply'
    const vertexShaderFilePath = '../shaders/simple.vert'
    const fragmentShaderFilePath = '../shaders/simple.frag'

    // testings
    let colors = new Float32Array([1.0, 0.0, 0.0]);

    // shaders
    let vertexShader = null;
    let fragmentShader = null;
    let shaderProgram = null;
    
    // models
    let dragon = null;
    let bunny = null;
    
    // buffers
    let indexBuffer = gl.createBuffer();
    let vertexBuffer = gl.createBuffer();
    let normalBuffer = gl.createBuffer();
    
    loadFileFromServer(bunnyFilePath)
    .then(data => {
        // Step 3 : Prepare Raw Data
        bunny = parsePly(data);

        // Step 4 : Prepare Buffer Objects
        // vertex buffer
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, bunny.vertices, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, null);
        // index buffer
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, bunny.indices, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null)
        // normals buffer
        gl.bindBuffer(gl.ARRAY_BUFFER, normalBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, bunny.normals, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, null);

        // Step 5 : Prepare Shaders
        // vertex shader
        return loadFileFromServer(vertexShaderFilePath);
    }).then(source => {
        vertexShader = gl.createShader(gl.VERTEX_SHADER);
        gl.shaderSource(vertexShader, source);
        gl.compileShader(vertexShader);

        // fragment shader
        return loadFileFromServer(fragmentShaderFilePath)
    }).then(source => {
        fragmentShader = gl.createShader(gl.FRAGMENT_SHADER)
        gl.shaderSource(fragmentShader, source);
        gl.compileShader(fragmentShader);

        // shader program
    }).then(() => {
        shaderProgram = gl.createProgram()
        gl.attachShader(shaderProgram, vertexShader);
        gl.attachShader(shaderProgram, fragmentShader);
        gl.linkProgram(shaderProgram);
        gl.useProgram(shaderProgram);
        
        // Step 7 : Request Animation Frame
    }).then(() => {
        requestAnimationFrame(animationLoop);
    });

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    // Variables used:
    let theta = 0;
    let t = 0; // to function as a time variable, changes model and lighting
    let model = bunny;
    //
    //------------------------------------------------------------------
    function update() {
        // change model

        // change lights

        t += 1;
        if (t > 500) { t = 0; }


        theta += 0.01;

        let uR_Y = [
            Math.cos(theta), 0, Math.sin(theta), 0,
            0, 1, 0, 0,
            -Math.sin(theta), 0, Math.cos(theta), 0,
            0, 0, 0, 1,
        ];

        // let uR_X = [
        //     1, 0, 0, 0,
        //     0, Math.cos(theta), -Math.sin(theta), 0,
        //     0, Math.sin(theta), Math.cos(theta), 0,
        //     0, 0, 0, 1,
        // ];

        // let uR_Z = [
        //     Math.cos(theta), -Math.sin(theta), 0, 0,
        //     Math.sin(theta), Math.cos(theta), 0, 0,
        //     0, 0, 1, 0,
        //     0, 0, 0, 1,
        // ];

        let uRotation = uR_Y;//multiplyMatrix4x4(multiplyMatrix4x4(uR_Y, uR_X), uR_Z);
        // let uRotation = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]; // IDENTITY MATRIX, just for testing

        let location = gl.getUniformLocation(shaderProgram, 'uThing');
        gl.uniformMatrix4fv(location, false, uRotation);
    }

    //------------------------------------------------------------------
    //
    // Rendering code goes here
    //
    //------------------------------------------------------------------
    function render() {
        // STEP 6 : Specify Shader & Buffer Object Attributes
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
        let position = gl.getAttribLocation(shaderProgram, 'aPosition');
        gl.enableVertexAttribArray(position);
        gl.vertexAttribPointer(position, 3, gl.FLOAT, false, bunny.vertices.BYTES_PER_ELEMENT * 3, 0);

        gl.bindBuffer(gl.ARRAY_BUFFER, normalBuffer);
        let normal = gl.getAttribLocation(shaderProgram, 'aNormal');
        gl.enableVertexAttribArray(normal);
        gl.vertexAttribPointer(normal, 3, gl.FLOAT, false, bunny.normals.BYTES_PER_ELEMENT * 3, 0);

        // Step 8 : Reset Framebuffer & Depth Buffer
        gl.clearColor(0.392156862740980392156862745098, 0.58431372549019607843137254901961, 0.92941176470588235294117647058824, 1.0);
        gl.clearDepth(1.0);
        gl.depthFunc(gl.LEQUAL);
        gl.enable(gl.DEPTH_TEST);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        // Step 9 : Render the models
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
        gl.drawElements(gl.TRIANGLES, bunny.indices.length, gl.UNSIGNED_INT, 0);
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

}());

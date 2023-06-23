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

        return loadFileFromServer(dragonFilePath)
    }).then(data => {
        // Step 3 : Prepare Raw Data
        dragon = parsePly(data);

        // Step 5 : Prepare Shaders & Shader Program
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
        changeModel(bunny);
        requestAnimationFrame(animationLoop);
    });

    //------------------------------------------------------------------
    //
    // Scene updates go here.
    // Variables used:
    // iteration control
    let theta = 0;
    let time = 0; // changes model and lighting
    //
    // uTRS
    let scale = 4;
    let transform = {dx: 0, dy: -0.3, dz: 0}
    //
    // model currently being rendered
    let model = null;
    //
    // // lights
    // let light1 = [1, 0, 0]; // default values: [1, 0, 0];
    // let light2 = [0, 0, 0]; // default values: [0, 1, 0];
    // let light3 = [0, 0, 0]; // default values: [0, 0, 1];
    //
    // Update lights and specular parameters
    let lightDirection = [0.5, 0.5, 1.0];       // Example light direction
    let lightColor = [1.0, 0.0, 0.0];           // Example light color
    let specularColor = [1.0, 0.0, 0.0];        // Example specular color
    let shininess = 4.0;                       // Example shininess factor
    //
    //------------------------------------------------------------------
    function update() {
        // ---update model and lights based on time---------------------
        if (time < 25) {
            // all of these values are set with an init or reset
        } else if (time < 50) {
            // green
            specularColor = [0.0, 1.0, 0.0];
            lightColor = [0.0, 1.0, 0.0];
        } else if (time < 75) {
            // blue
            specularColor = [0.0, 0.0, 1.0];
            lightColor = [0.0, 0.0, 1.0];
        } else if (time < 100) {
            // white
            specularColor = [1.0, 1.0, 1.0];
            lightColor = [1.0, 1.0, 1.0];
        } else { // reset
            time = 0;
            // switch model
            if (model.vertices.length == 107841) { changeModel(dragon); }
            else { changeModel(bunny) }
            // red
            specularColor = [0.0, 0.0, 1.0];
            lightColor = [0.0, 0.0, 1.0];
        }

        // increment loop values
        time += 0.05;
        theta += 0.01;

        // ---matrices for Translation, Scale, and Rotation-------------
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

        let uR_Z = [
            Math.cos(theta), -Math.sin(theta), 0, 0,
            Math.sin(theta), Math.cos(theta), 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ];

        let uTS = [
            scale, 0, 0, 0,
            0, scale, 0, 0,
            0, 0, scale, 0,
            transform.dx, transform.dy, transform.dz, 1,
        ]

        // calculate uTSR (uTranslateScaleRotation)
        // let uRotation = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]; // TESTING: i matrix
        let uRotation = uR_Y;//multiplyMatrix4x4(multiplyMatrix4x4(uR_Y, uR_X), uR_Z);//uR_Y;
        let uTSR = multiplyMatrix4x4(uRotation, uTS);

        //variables for projection
        let n = 0;
        let t = 0;
        let f = 0;

        // matrix for perspective projection
        let projection = [
            // n/r, 0, 0, 0,
            // 0, n/t, 0, 0,
            // 0, 0, (-(f + n))/(f - n), (-2 * f * n)/(f - n),
            // 0, 0, -1, 0,
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        ];

        // ---update values in shader-----------------------------------
        let shaderLightDirection = gl.getUniformLocation(shaderProgram, 'lightDirection');
        let shaderLightColor = gl.getUniformLocation(shaderProgram, 'lightColor');
        let shaderSpecularColor = gl.getUniformLocation(shaderProgram, 'specularColor');
        let shaderShininess = gl.getUniformLocation(shaderProgram, 'shininess');
        gl.uniform3fv(shaderLightDirection, lightDirection);
        gl.uniform3fv(shaderLightColor, lightColor);
        gl.uniform3fv(shaderSpecularColor, specularColor);
        gl.uniform1f(shaderShininess, shininess);

        // // update lights
        // let shaderLight1 = gl.getUniformLocation(shaderProgram, 'L1_d');
        // let shaderLight2 = gl.getUniformLocation(shaderProgram, 'L2_d');
        // let shaderLight3 = gl.getUniformLocation(shaderProgram, 'L3_d');
        // gl.uniform3fv(shaderLight1, light1);
        // gl.uniform3fv(shaderLight2, light2);
        // gl.uniform3fv(shaderLight3, light3);

        // update location
        let location = gl.getUniformLocation(shaderProgram, 'uThing');
        gl.uniformMatrix4fv(location, false, uTSR);

        // update with projection perspective
        let perspective = gl.getUniformLocation(shaderProgram, 'uProjection');
        gl.uniformMatrix4fv(perspective, false, projection);
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
        gl.vertexAttribPointer(position, 3, gl.FLOAT, false, model.vertices.BYTES_PER_ELEMENT * 3, 0);

        gl.bindBuffer(gl.ARRAY_BUFFER, normalBuffer);
        let normal = gl.getAttribLocation(shaderProgram, 'aNormal');
        gl.enableVertexAttribArray(normal);
        gl.vertexAttribPointer(normal, 3, gl.FLOAT, false, model.normals.BYTES_PER_ELEMENT * 3, 0);

        // Step 8 : Reset Framebuffer & Depth Buffer
        gl.clearColor(0.392156862740980392156862745098, 0.58431372549019607843137254901961, 0.92941176470588235294117647058824, 1.0);
        gl.clearDepth(1.0);
        gl.depthFunc(gl.LEQUAL);
        gl.enable(gl.DEPTH_TEST);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        // Step 9 : Render the models
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
        gl.drawElements(gl.TRIANGLES, model.indices.length, gl.UNSIGNED_INT, 0);
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

    //------------------------------------------------------------------
    //
    // Helper function to set model, vertex, index, and normal buffers
    //
    //------------------------------------------------------------------
    function changeModel(newModel) {
        model = newModel;
        // Step 4 : Prepare Buffer Objects
        // vertex buffer
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, model.vertices, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, null);
        // index buffer
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, model.indices, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null)
        // normals buffer
        gl.bindBuffer(gl.ARRAY_BUFFER, normalBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, model.normals, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, null);
    }
}());

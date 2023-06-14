//------------------------------------------------------------------
//
// Helper function used to load a file from the server
//
//------------------------------------------------------------------
function loadFileFromServer(filename) {
    return fetch(filename)
        .then(res => res.text());
}

//------------------------------------------------------------------
//
// Helper function to parse .ply files with the format ascii
//
//------------------------------------------------------------------
function parsePly(lines) {
    let dataIndex = 0;
    
    let vertexCount = null;
    let faceCount = null;
    // get face and vertex count
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].startsWith('element vertex')) {
            vertexCount = parseInt(lines[i].split(' ')[2]);
        } else if (lines[i].startsWith('element face')) {
            faceCount = parseInt(lines[i].split(' ')[2]);
        } else if (lines[i].startsWith('end_header')) {
            dataIndex = i + 1;
            break;
        }
    }
    
    let v =[];
    // get vertices
    for (let i = dataIndex; i < dataIndex + vertexCount; i++) {
        const vertexData = lines[i].split(' ');
        v.push({
            x: parseFloat(vertexData[0]),
            y: parseFloat(vertexData[1]),
            z: parseFloat(vertexData[2])
        });
    }
    let vertices = new Float32Array(v);
    
    let I = [];
    // get indices
    for (let i = dataIndex + vertexCount; i < dataIndex + vertexCount + faceCount; i++) {
        const faceData = lines[i].split(' ');
        const faceIndices = faceData.slice(1).map(index => parseInt(index));
        faceIndices.pop();
        I.push(faceIndices);
    }
    let indices = new Uint32Array(I);

    // compute normals
    let normals = computeNormals(vertices, indices);

    return {vertices, indices, normals}
}

//------------------------------------------------------------------
//
// Helper function to compute normals
//
//------------------------------------------------------------------
function computeNormals(verticies, indices) {
    let normals = new Float32Array([]);

    // TODO: IMPLEMENT - actually compute normals

    return normals
}

//------------------------------------------------------------------
//
// Helper function to multiply two 4x4 matrices.
//
//------------------------------------------------------------------
function multiplyMatrix4x4(m1, m2) {
    let r = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0];

    // Iterative multiplication
    // for (let i = 0; i < 4; i++) {
    //     for (let j = 0; j < 4; j++) {
    //         for (let k = 0; k < 4; k++) {
    //             r[i * 4 + j] += m1[i * 4 + k] * m2[k * 4 + j];
    //         }
    //     }
    // }

    // "Optimized" manual multiplication
    r[0] = m1[0] * m2[0] + m1[1] * m2[4] + m1[2] * m2[8] + m1[3] * m2[12];
    r[1] = m1[0] * m2[1] + m1[1] * m2[5] + m1[2] * m2[9] + m1[3] * m2[13];
    r[2] = m1[0] * m2[2] + m1[1] * m2[6] + m1[2] * m2[10] + m1[3] * m2[14];
    r[3] = m1[0] * m2[3] + m1[1] * m2[7] + m1[2] * m2[11] + m1[3] * m2[15];

    r[4] = m1[4] * m2[0] + m1[5] * m2[4] + m1[6] * m2[8] + m1[7] * m2[12];
    r[5] = m1[4] * m2[1] + m1[5] * m2[5] + m1[6] * m2[9] + m1[7] * m2[13];
    r[6] = m1[4] * m2[2] + m1[5] * m2[6] + m1[6] * m2[10] + m1[7] * m2[14];
    r[7] = m1[4] * m2[3] + m1[5] * m2[7] + m1[6] * m2[11] + m1[7] * m2[15];

    r[8] = m1[8] * m2[0] + m1[9] * m2[4] + m1[10] * m2[8] + m1[11] * m2[12];
    r[9] = m1[8] * m2[1] + m1[9] * m2[5] + m1[10] * m2[9] + m1[11] * m2[13];
    r[10] = m1[8] * m2[2] + m1[9] * m2[6] + m1[10] * m2[10] + m1[11] * m2[14];
    r[11] = m1[8] * m2[3] + m1[9] * m2[7] + m1[10] * m2[11] + m1[11] * m2[15];

    r[12] = m1[12] * m2[0] + m1[13] * m2[4] + m1[14] * m2[8] + m1[15] * m2[12];
    r[13] = m1[12] * m2[1] + m1[13] * m2[5] + m1[14] * m2[9] + m1[15] * m2[13];
    r[14] = m1[12] * m2[2] + m1[13] * m2[6] + m1[14] * m2[10] + m1[15] * m2[14];
    r[15] = m1[12] * m2[3] + m1[13] * m2[7] + m1[14] * m2[11] + m1[15] * m2[15];

    return r;
}

//------------------------------------------------------------------
//
// Transpose a matrix.
// Reference: https://jsperf.com/transpose-2d-array
//
//------------------------------------------------------------------
function transposeMatrix4x4(m) {
    let t = [
        m[0], m[4], m[8], m[12],
        m[1], m[5], m[9], m[13],
        m[2], m[6], m[10], m[14],
        m[3], m[7], m[11], m[15]
    ];

    return t;
}

//------------------------------------------------------------------
//
// Helper function to multiply two 4x4 matrices.
//
//------------------------------------------------------------------
function multiplyMatrix_4x4_4x1(m4x1, m4x4) {
    let r = [
        0,
        0,
        0,
        0,
    ];

    // Iterative multiplication
    // for (let i = 0; i < 4; i++) {
    //     for (let j = 0; j < 4; j++) {
    //         for (let k = 0; k < 4; k++) {
    //             r[i * 4 + j] += m1[i * 4 + k] * m2[k * 4 + j];
    //         }
    //     }
    // }

    // "Optimized" manual multiplication
    r[0] = m4x1[0] * m4x4[0]  + m4x1[1] * m4x4[1]  + m4x1[2] * m4x4[2]  + m4x1[3] * m4x4[3];
    r[1] = m4x1[0] * m4x4[4]  + m4x1[1] * m4x4[5]  + m4x1[2] * m4x4[6]  + m4x1[3] * m4x4[7];
    r[2] = m4x1[0] * m4x4[8]  + m4x1[1] * m4x4[9]  + m4x1[2] * m4x4[10] + m4x1[3] * m4x4[11];
    r[3] = m4x1[0] * m4x4[12] + m4x1[1] * m4x4[13] + m4x1[2] * m4x4[14] + m4x1[3] * m4x4[15];

    return r;
}

//------------------------------------------------------------------
//
// function to multiply matrix4x4 by -1
//
//------------------------------------------------------------------
function negateMatrix4x4(m) {
    return [
        -1 * m[0],  -1 * m[1],   -1 * m[2],  -1 * m[3],
        -1 * m[4],  -1 * m[5],   -1 * m[6],  -1 * m[7],
        -1 * m[8],  -1 * m[9],   -1 * m[10], -1 * m[11],
        -1 * m[12], -1 * m[13],  -1 * m[14], -1 * m[15],
    ];
}

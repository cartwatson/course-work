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
function parsePly(data) {
    const lines = data.split('\n');
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
    
    let v = []; // [x, y, z]
    // get vertices
    for (let i = dataIndex; i < dataIndex + vertexCount; i++) {
        const vertexData = lines[i].split(' ');
        v.push([
            parseFloat(vertexData[0]),
            parseFloat(vertexData[1]),
            parseFloat(vertexData[2])
        ]);
    }
    
    let I = [];
    // get indices
    for (let i = dataIndex + vertexCount; i < dataIndex + vertexCount + faceCount; i++) {
        const faceData = lines[i].split(' ');
        const faceIndices = faceData.slice(1).map(index => parseInt(index));
        faceIndices.pop();
        I.push(faceIndices);
    }

    // compute normals
    let n = computeNormals(v, I);

    // get in usable form // flatten arrays
    let vertices = new Float32Array(flattenArray(v));
    let indices = new Uint32Array(flattenArray(I));
    let normals = new Float32Array(flattenArray(n));
    
    return {vertices, indices, normals}
}

//------------------------------------------------------------------
//
// Helper function to compute normals
//
//------------------------------------------------------------------
function computeNormals(vertices, indices) {
    // compute face normal
    let faceNormals = [];
    for (let i = 0; i < indices.length; i += 1) {
        const v1 = vertices[indices[i][0]];
        const v2 = vertices[indices[i][1]];
        const v3 = vertices[indices[i][2]];

        const edge1 = [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]]
        const edge2 = [v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]]

        faceNormals.push(normalize(crossProduct(edge1, edge2)));
    }

    // compute vertex normal
    // init final and helper array, fill with zeros
    const vertexNormals = new Array(vertices.length);
    for (let i = 0; i < vertexNormals.length; i++) { vertexNormals[i] = [0, 0, 0]; } // using .fill([0,0,0]) results in each index having the same ref
    const vertexCount = new Array(vertices.length).fill(0);

    // Accumulate face normals to vertex normals
    for (let i = 0; i < indices.length; i++) {
        const vertexIndex1 = indices[i][0];
        const vertexIndex2 = indices[i][1];
        const vertexIndex3 = indices[i][2];
        
        const faceNormal = faceNormals[i];

        // increment count to use for averaging later
        vertexCount[vertexIndex1] += 1;
        vertexCount[vertexIndex2] += 1;
        vertexCount[vertexIndex3] += 1;

        // increment value of normal to be averaged and normalized later
        vertexNormals[vertexIndex1][0] += faceNormal[0];
        vertexNormals[vertexIndex1][1] += faceNormal[1];
        vertexNormals[vertexIndex1][2] += faceNormal[2];

        vertexNormals[vertexIndex2][0] += faceNormal[0];
        vertexNormals[vertexIndex2][1] += faceNormal[1];
        vertexNormals[vertexIndex2][2] += faceNormal[2];
        
        vertexNormals[vertexIndex3][0] += faceNormal[0];
        vertexNormals[vertexIndex3][1] += faceNormal[1];
        vertexNormals[vertexIndex3][2] += faceNormal[2];
    }
    
    // average vertex normals
    for (let i = 0; i < vertexCount.length; i++) {
        if (vertexCount[i] === 0) { continue; }
        vertexNormals[i][0] = vertexNormals[i][0] / vertexCount[i];
        vertexNormals[i][1] = vertexNormals[i][1] / vertexCount[i];
        vertexNormals[i][2] = vertexNormals[i][2] / vertexCount[i];
    }
  
    // Normalize vertex normals
    for (let i = 0; i < vertexNormals.length; i++) { vertexNormals[i] = normalize(vertexNormals[i]); }

    // return vertex normal
    return vertexNormals;
}

//------------------------------------------------------------------
//
// Helper function to do cross product
//
//------------------------------------------------------------------
function crossProduct(v1, v2) {
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
      ];
}

//------------------------------------------------------------------
//
// Helper function to do normalize vector
//
//------------------------------------------------------------------
function normalize(v) {
    const length = Math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
    
    v[0] /= length;
    v[1] /= length;
    v[2] /= length;

    return v;
}

//------------------------------------------------------------------
//
// Helper function to make a 2D array 1D
//
//------------------------------------------------------------------
function flattenArray(array2D) {
    let flattened = [];

    for (let i = 0; i < array2D.length; i++) {
        for (let j = 0; j < array2D[i].length; j++) {
            flattened.push(array2D[i][j]);
        }
    }

    return flattened;
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

// //------------------------------------------------------------------
// //
// // function to transpose model matrix
// // param  - modelMatrix: [int] len=4
// // param  - transpose: [int] len=3
// //          form: [x, y, z]
// // return - modelMatrix`: [int] len=4
// //
// //------------------------------------------------------------------
// function transpose(modelMatrix, tranpose) {
//     // convert transpose to 4x4
//     let T = [
//         1, 0, 0, tranpose[0],
//         0, 1, 0, tranpose[1],
//         0, 0, 1, tranpose[2],
//         0, 0, 0, 1,
//     ];

//     return multiplyMatrix_4x4_4x1(T, modelMatrix)
// }

// //------------------------------------------------------------------
// //
// // function to sca;e model matrix
// // param  - modelMatrix: [int] len=4
// // param  - scale: [int] len=3
// //          form: [x, y, z]
// // return - modelMatrix`: [int] len=4
// //
// //------------------------------------------------------------------
// function scale(modelMatrix, scale) {
//     // convert transpose to 4x4
//     let S = [
//         scale[0], 0,        0,        0,
//         0,        scale[1], 0,        0,
//         0,        0,        scale[2], 0,
//         0,        0,        0,        1,
//     ];

//     return multiplyMatrix_4x4_4x1(S, modelMatrix)
// }

// //------------------------------------------------------------------
// //
// // function to rotate model matrix
// // param  - modelMatrix: [int] len=4
// // param  - r: int
// // param  - theta: int
// // return - modelMatrix`: [int] len=4
// //
// //------------------------------------------------------------------
// function rotate(modelMatrix, r, theta) {
//     // find T
//     let T = [
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//     ];

//     // find R_A
//     let R_A = [
//         Math.cos(theta),      0, Math.sin(theta), 0, 
//         0,                    1, 0,               0, 
//         -1 * Math.sin(theta), 0, Math.cos(theta), 0, 
//         0,                    0, 0,               1, 
//     ];

//     // find R_B
//     let R_B = [
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//     ];

//     // find R_Theta
//     let R_Theta = [
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//         0, 0, 0, 0, 
//     ];
    
//     // return (-1)T * R_-A * R_-B * R_Theta * R_B * R_A * T * P
//     return multiplyMatrix_4x4_4x1(negateMatrix4x4(T),
//         multiplyMatrix_4x4_4x1(negateMatrix4x4(R_A),
//             multiplyMatrix_4x4_4x1(negateMatrix4x4(R_B),
//                 multiplyMatrix_4x4_4x1(R_Theta,
//                     multiplyMatrix_4x4_4x1(R_B,
//                         multiplyMatrix_4x4_4x1(R_A,
//                             multiplyMatrix_4x4_4x1(T, modelMatrix)
//                         )
//                     )
//                 )
//             )
//         )
//     )
// }



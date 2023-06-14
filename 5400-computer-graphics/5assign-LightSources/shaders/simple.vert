#version 300 es

//uniform mat4 uProjection;
uniform mat4 uThing;
in vec4 aPosition;
in vec4 aColor;
out vec4 vColor;

void main()
{
    //gl_Position = uProjection * uThing * aPosition;
    gl_Position = uThing * aPosition;
    vColor = aColor;
}

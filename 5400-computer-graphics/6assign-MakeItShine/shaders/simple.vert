#version 300 es

uniform mat4 uProjection;
uniform mat4 uThing;
in vec4 aPosition;
in vec4 aNormal;
in vec4 aColor;
out vec4 vColor;
out vec4 vNormal;

void main()
{
    // position calcs
    gl_Position = uProjection * uThing * aPosition;

    vNormal = aNormal;
    vColor = aColor;
}

#version 300 es

uniform mat4 uProjection;
uniform mat4 uThing;
in vec4 aPosition;
in vec4 aNormal;
out vec4 vColor;

// light intensity = light color RGB
uniform vec3 L1_d;
uniform vec3 L2_d;
uniform vec3 L3_d;

// constants
vec3 K_d = vec3(0.5, 0.5, 0.5);
vec3 LightPos1 = vec3(1, 1, 1);
vec3 LightPos2 = vec3(1, 1, 1);
vec3 LightPos3 = vec3(1, 1, 1);

// ambient light
vec3 K_a = vec3(1, 1, 1);
vec3 La_d = vec3(0.25, 0.25, 0.25);

void main()
{
    // position calcs
    gl_Position = uProjection * uThing * aPosition;

    // lighting calcs
    vec3 Light1 = K_d * L1_d * dot(aNormal.xyz, LightPos1 - aPosition.xyz);
    vec3 Light2 = K_d * L2_d * dot(aNormal.xyz, LightPos2 - aPosition.xyz);
    vec3 Light3 = K_d * L3_d * dot(aNormal.xyz, LightPos3 - aPosition.xyz);
    vec3 ambient = K_a * La_d;
    vec3 intensity = clamp(Light1 + Light2 + Light3 + ambient, vec3(0, 0, 0), vec3(1, 1, 1));
    vColor = vec4(intensity, 1);
}

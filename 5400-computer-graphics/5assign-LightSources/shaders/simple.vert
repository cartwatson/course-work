#version 300 es

//uniform mat4 uProjection;
uniform mat4 uThing;
in vec4 aPosition;
in vec4 aNormal;
out vec4 vColor;

// light intensity = light color RGB
// TODO: take this in as a uniform later
vec3 L1_d = vec3(1, 0, 0);
vec3 L2_d = vec3(0, 1, 0);
vec3 L3_d = vec3(0, 0, 1);

// constants
vec3 K_d = vec3(1, 0, 0);
vec3 LightPos1 = vec3(1, 1, 1);
vec3 LightPos2 = vec3(-1, -1, -1);
vec3 LightPos3 = vec3(1, -1, -1);

// ambient light
vec3 K_a = vec3(0.25, 0, 0);
// vec3 La_d = vec3(1, 1, 1);
vec3 La_d = vec3(0.25, 0.25, 0.25);

void main()
{
    //gl_Position = uProjection * uThing * aPosition;
    gl_Position = uThing * aPosition;
    vec3 Light1 = K_d * L1_d * dot(aPosition.xyz, LightPos1 - aPosition.xyz);
    vec3 Light2 = K_d * L2_d * dot(aPosition.xyz, LightPos2 - aPosition.xyz);
    vec3 Light3 = K_d * L3_d * dot(aPosition.xyz, LightPos3 - aPosition.xyz);
    vec3 ambient = K_a * La_d;
    vec3 intensity = clamp(Light1 + Light2 + Light3 + ambient, vec3(0, 0, 0), vec3(1, 1, 1));
    vColor = vec4(intensity, 1);
    // vColor = vec4(1, 0, 0, 1); // TESTING ONLY
}

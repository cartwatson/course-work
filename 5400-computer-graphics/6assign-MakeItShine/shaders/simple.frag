#version 300 es

precision lowp float;
in vec4 vNormal;
out vec4 fragColor;

uniform vec3 lightDirection;     // Direction of the light source
uniform vec3 lightColor;         // Color of the light source
uniform vec3 specularColor;      // Color of the specular highlight
uniform float shininess;         // Shininess factor for controlling the size of the specular highlight

// // light intensity = light color RGB
// uniform vec3 L1_d;
// uniform vec3 L2_d;
// uniform vec3 L3_d;

// // constants
// vec3 K_d = vec3(0.5, 0.5, 0.5);
// vec3 LightPos1 = vec3(1, 1, 1);
// vec3 LightPos2 = vec3(1, 1, 1);
// vec3 LightPos3 = vec3(1, 1, 1);

// // ambient light
// vec3 K_a = vec3(1, 1, 1);
// vec3 La_d = vec3(0.25, 0.25, 0.25);

void main()
{
    // Normalize the interpolated normal
    vec3 normal = normalize(vNormal.xyz);

    // Calculate the diffuse lighting contribution
    vec3 diffuse = max(dot(normal, -lightDirection), 0.0) * lightColor;

    // Calculate the specular lighting contribution
    vec3 viewDirection = normalize(-gl_FragCoord.xyz);
    vec3 reflectionDirection = reflect(lightDirection, normal);
    float specularFactor = pow(max(dot(viewDirection, reflectionDirection), 0.0), shininess);
    vec3 specular = specularColor * specularFactor;

    // Combine the diffuse and specular lighting
    vec3 lighting = diffuse + specular;

    // Output the final color
    fragColor = vec4(lighting, 1.0);

    // vec3 normal = normalize(vNormal.xyz);

    // // lighting calcs
    // vec3 Light1 = K_d * L1_d * dot(normal, LightPos1 - gl_FragCoord.xyz);
    // vec3 Light2 = K_d * L2_d * dot(normal, LightPos2 - gl_FragCoord.xyz);
    // vec3 Light3 = K_d * L3_d * dot(normal, LightPos3 - gl_FragCoord.xyz);
    // vec3 ambient = K_a * La_d;
    // vec3 intensity = clamp(Light1 + Light2 + Light3 + ambient, vec3(0, 0, 0), vec3(1, 1, 1));
    // fragColor = vec4(intensity, 1);
}

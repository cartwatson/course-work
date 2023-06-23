#version 300 es

precision lowp float;
in vec4 vNormal;
out vec4 fragColor;

uniform vec3 lightDirection;
uniform vec3 lightColor;
uniform vec3 specularColor;
uniform float shininess;

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
}

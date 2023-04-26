using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR;

public class movement : MonoBehaviour
{
    private float speed = 20.0f;
    private float accel = 2.0f;

    private float rotSens = 3.0f;

    // Update is called once per frame
    void Update()
    {
        // Handle rotation with mouse input
        float yaw = transform.eulerAngles.y + Input.GetAxis("Mouse X") * rotSens;
        float pitch = transform.eulerAngles.x - Input.GetAxis("Mouse Y") * rotSens;
        transform.eulerAngles = new Vector3(pitch, yaw, 0.0f);

        // Handle movement with keyboard input
        Vector3 direction = new Vector3();

        // Move relative to device's facing direction
        InputDevice device = InputDevices.GetDeviceAtXRNode(XRNode.Head);
        if (device.isValid)
        {
            Quaternion deviceRotation;
            if (device.TryGetFeatureValue(CommonUsages.deviceRotation, out deviceRotation))
            {
                Vector3 forward = deviceRotation * Vector3.forward;
                Vector3 right = deviceRotation * Vector3.right;
                Vector3 up = deviceRotation * Vector3.up;

                if (Input.GetKey(KeyCode.W))
                {
                    direction += forward;
                }
                if (Input.GetKey(KeyCode.A))
                {
                    direction -= right;
                }
                if (Input.GetKey(KeyCode.S))
                {
                    direction -= forward;
                }
                if (Input.GetKey(KeyCode.D))
                {
                    direction += right;
                }
                if (Input.GetKey(KeyCode.Q))
                {
                    direction -= up;
                }
                if (Input.GetKey(KeyCode.E))
                {
                    direction += up;
                }
            }
        }

        // Apply speed and move the object
        float currentSpeed = speed;
        if (Input.GetKey(KeyCode.LeftShift))
        {
            currentSpeed *= accel;
        }
        direction = direction.normalized * currentSpeed * Time.deltaTime;
        transform.position += direction;

        // Reset speed if left shift is released
        if (Input.GetKeyUp(KeyCode.LeftShift))
        {
            currentSpeed /= accel;
        }
    }
}
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraManipulator : MonoBehaviour
{
    private float speed = 20.0f;
    private float accel = 2.0f;

    private float yaw = 0.0f;
    private float pitch = 0.0f;

    private float rotSens = 3.0f;

    // Update is called once per frame
    void Update()
    {
        yaw += Input.GetAxis("Mouse X") * rotSens;
        pitch -= Input.GetAxis("Mouse Y") * rotSens;
        transform.eulerAngles = new Vector3(pitch, yaw, 0.0f);

        // 1: move to center of room 1
        // 2: move to center of room 2
        if (Input.GetKeyDown(KeyCode.Alpha1) || Input.GetKeyDown(KeyCode.Alpha2))
        {
            if (Input.GetKeyDown("1"))
            {
                // move to center of room 1
                transform.position = new Vector3(0, 15, 0);
            }
            else 
            {
                // move to center of room 2
                transform.position = new Vector3(0, 15, -60);
            }
        }
        else
        {
            Vector3 v = new Vector3();
            // get direction
            if (Input.GetKey(KeyCode.W))
            {
                v += Vector3.forward;
            }
            if (Input.GetKey(KeyCode.A))
            {
                v += Vector3.left;
            }
            if (Input.GetKey(KeyCode.S))
            {
                v += Vector3.back;
            }
            if (Input.GetKey(KeyCode.D))
            {
                v += Vector3.right;
            }
            if (Input.GetKey(KeyCode.Q))
            {
                v += Vector3.down;
            }
            if (Input.GetKey(KeyCode.E))
            {
                v += Vector3.up;
            }

            // get speed
            if (Input.GetKey(KeyCode.LeftShift))
            {
                speed *= accel;
            }

            v = v * speed * Time.deltaTime;
            transform.Translate(v);

            // reset speed
            if (Input.GetKey(KeyCode.LeftShift))
            {
                speed /= accel;
            }
        }
    }
}

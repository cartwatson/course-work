using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR;
using Unity.XR.CoreUtils;

public class navigation : MonoBehaviour
{
    public XRNode rightHand;
    public XRNode leftHand;
    private XROrigin rig;
    private Vector2 inputAxis;
    private CharacterController character;
    private float scale = 6f; // the scale of my rooms and such is very off, this is to help mitigate that problem
    public float speed = 10f;
    private float gravity = -9.81f;
    private Vector3 velocity = new Vector3(0f, 0f, 0f);
    // jump, speed up, turn around  
    private bool jump = false; // button
    private bool isJumping = false; //bool
    private float jumpHeight = 2f;
    // accelerate
    private bool accel = false;
    private float accelMultiplier = 0f;
    // turn around
    private bool turn = false;
    private bool haventTurned = true;
    private Quaternion currentRotation;
    // door
    private bool doorChange = false;
    private bool doorOpen = false; // false == closed
    private GameObject door;
    private bool doorTransitioning = false;

    // Start is called before the first frame update
    void Start()
    {
        character = GetComponent<CharacterController>();
        rig = GetComponent<XROrigin>();
        currentRotation = rig.transform.rotation;
        door = GameObject.Find("Door");
    }

    // Update is called once per frame
    void Update()
    {
        UnityEngine.XR.InputDevice left = InputDevices.GetDeviceAtXRNode(leftHand);
        UnityEngine.XR.InputDevice right = InputDevices.GetDeviceAtXRNode(rightHand);
        // movement - left stick
        left.TryGetFeatureValue(CommonUsages.primary2DAxis, out inputAxis);
        // jumping - A
        right.TryGetFeatureValue(CommonUsages.primaryButton, out jump);
        // accel - left trigger
        left.TryGetFeatureValue(CommonUsages.triggerButton, out accel);
        // turn around - left Stick Press
        left.TryGetFeatureValue(CommonUsages.primary2DAxisClick, out turn);
        // open door - X
        left.TryGetFeatureValue(CommonUsages.primaryButton, out doorChange);
    }

    private void FixedUpdate()
    {
        // accelerate
        if (accel) { accelMultiplier = 2f; }
        // apply movement relative to direction facing
        Quaternion headYaw = Quaternion.Euler(0, rig.Camera.transform.eulerAngles.y, 0);
        Vector3 direction = headYaw * new Vector3(inputAxis.x, 0, inputAxis.y);
        character.Move(direction * Time.fixedDeltaTime * speed * accelMultiplier * scale);
        // jump
        if (jump && character.isGrounded && !isJumping) {
            isJumping = true;
            velocity.y += Mathf.Sqrt(jumpHeight * -3.0f * gravity);
        } else if (isJumping && character.isGrounded) {
            isJumping = false;
            velocity.y = 0f;
        }
        // turn around
        if (turn && haventTurned)
        {
            currentRotation *= Quaternion.Euler(0f, 180f, 0f);
            rig.transform.rotation = currentRotation;
            haventTurned = false;
        }
        // reset ability to turn
        if (!turn && !haventTurned) { haventTurned = true; }
        
        // apply gravity
        velocity.y += gravity * Time.fixedDeltaTime;
        character.Move(velocity * Time.fixedDeltaTime * scale);

        // alternate door
        if (doorChange && !doorTransitioning)
        {
            if (doorOpen)
            {
                // close door
                door.transform.position = new Vector3(-42.5f, 15f, 125f);
            }
            else
            {
                // open door
                door.transform.position = new Vector3(-57.5f, 15f, 125f);
            }
            // change the state of the door
            doorOpen = !doorOpen;
            doorTransitioning = true;
        }
        
        if (!doorChange && doorTransitioning) { doorTransitioning = false; }

        // reset accel
        accelMultiplier = 1f;
    }
}

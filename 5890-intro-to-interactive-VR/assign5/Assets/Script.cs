using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR;
using Unity.XR.CoreUtils;

public class Script : MonoBehaviour
{
    // animation
    public Animator mainCharacterAnimator;
    public Animator sideCharacterAnimator;
    // objects
    public XRNode rightHand;
    public XRNode leftHand;
    private XROrigin rig;
    private Vector2 inputAxis;
    private CharacterController character;
    // values
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
    // animation
    // side
    private bool anim = false;
    private float range = 10f;
    private float distance;
    private GameObject sideChar;

    // Start is called before the first frame update
    void Start()
    {
        character = GetComponent<CharacterController>();
        rig = GetComponent<XROrigin>();
        currentRotation = rig.transform.rotation;
        sideChar = GameObject.Find("YBot");
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
        // animation button - X
        left.TryGetFeatureValue(CommonUsages.primaryButton, out anim);
    }

    private void FixedUpdate()
    {
        // accelerate
        if (accel) {
            accelMultiplier = 2f;
            mainCharacterAnimator.SetBool("IsRunning", true);
        } else {
            mainCharacterAnimator.SetBool("IsRunning", false);
        }

        // apply movement relative to direction facing
        Quaternion headYaw = Quaternion.Euler(0, rig.Camera.transform.eulerAngles.y, 0);
        Vector3 direction = headYaw * new Vector3(inputAxis.x, 0, inputAxis.y);
        character.Move(direction * Time.fixedDeltaTime * speed * accelMultiplier * scale);

        // animation control
        if (direction != Vector3.zero) {
            mainCharacterAnimator.SetBool("IsWalking", true);
        } else {
            mainCharacterAnimator.SetBool("IsWalking", false);
        }

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

        // reset accel
        accelMultiplier = 1f;

        // side character animations
        // get updated distance between player and side character
        distance = Vector3.Distance(sideChar.transform.position, this.transform.position);
        // toggle animations
        if (distance < range) {
            // if pressing button
            if (anim) {
                sideCharacterAnimator.SetBool("InRange+Button", true); // activate button animation
            } else {
                sideCharacterAnimator.SetBool("InRange+Button", false); // deactivate button animation
            }
            sideCharacterAnimator.SetBool("InRange", true); // reactivate in range animation
        } else {
            // deactivate both animations
            sideCharacterAnimator.SetBool("InRange", false);
            sideCharacterAnimator.SetBool("InRange+Button", false);
        }
    }
}

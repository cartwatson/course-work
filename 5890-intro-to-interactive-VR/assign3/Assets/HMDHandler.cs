using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR;

public class HMDHandler : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Is device active: " + XRSettings.isDeviceActive);

        if (!XRSettings.isDeviceActive) {
            Debug.Log("No HMD");
        }
        else if (XRSettings.isDeviceActive &&
                (XRSettings.loadedDeviceName == "Mock HMD" ||
                 XRSettings.loadedDeviceName == "MockHMD Display")) {
            Debug.Log("Using Mock HMD");
        }
        else {
            Debug.Log("Headset Name: " + XRSettings.loadedDeviceName);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

# Unit 1
## Intro
* early history
* application areas
* components in system
  * input
  * CPU
  * RAM
  * GPU 
    * memory
      * framebuffer
  * output
* Pixels and Framebuffer
  * modern systems, raster based
    * array (raster) of pixels
    * referred to as framebuffer
  * resolution
    * num of pixels in framebuffer
  * depth/precision
    * num of bits per pixel
    * full color has >24 bits per pixel; 8 for RGB each; 0-255
    * high dynamic range >30 bits per pixel
  * dynamic range
    * ratio between max and min intensity in display
    * 12bits per color is 4096:1
    * human eye can perceive 10,000:1 (ballpark figure)
  * Coordinate representation
    * (Device & Screen) or (Image & Pixel)
      * upper left 0, 0
    * World
      * center 0, 0
      * bottom left -1.0, -1.0
      * top right 1.0, 1.0
      * conversions in slides
        * world to device
        * device to world
    * Graphics APIs
      * OpenGL
        * Khronos Group
        * depricated
      * OpenGL Embedded Systems
        * Khronos Group again
        * up to date with OpenGL
      * WebGL
        * Khronos Group again
        * based on OpenGL ES
      * Others
        * DirectX - Microsoft
        * Vulkan - Khronos Group
        * Metal - Apple

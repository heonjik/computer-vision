# computer-vision

1. Generate and save promising markers
2. Decode the markers using a reliable method (OpenCV modules, apriltag library, our own algorithm, etc.)
3. Find minimum pixel per bit required for detection by resizing the image
4. Find maximum viewing angle feasible for detection by applying perspective transformation
5. Use the previous values to find a relation between camera's attributes (resolution and FOV), altitude and marker size
6. Compare the results for different types of markers
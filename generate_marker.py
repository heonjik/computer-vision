import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#from apriltag import apriltag

def generate_markers():
    dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
    # 250 markers and a marker size of 6x6 bits

    # Generate a marker
    marker_id = 1  # marker 1 of the dictionary
    marker_size = 200   # size in pixels
    marker_image = cv.aruco.generateImageMarker(dictionary, marker_id, marker_size)

    cv.imwrite("marker1.png", marker_image)
    plt.imshow(marker_image, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.title(f'ArUco Marker {marker_id}')
    plt.show()

def detect_markers():
    detectorParams = cv.aruco.DetectorParameters()

def main():
    detect_markers()

if __name__=='__main__':
    main()
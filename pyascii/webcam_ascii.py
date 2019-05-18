import cv2
import numpy as np
from PIL import Image

from AsciiArt import AsciiArt

ascii_art = AsciiArt()
cap = cv2.VideoCapture(0)

while(True):

    _, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pillow_image = Image.fromarray(image)

    ascii_image = ascii_art.convert_to_ascii(pillow_image, 0.1)

    # TODO: Print ASCII image in terminal

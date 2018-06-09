#! /usr/bin/env python3
# coding: utf-8
from PIL import Image

class AsciiArt():
    def __init__(self, img_path):
        self.path = img_path
        self.gray_scale = r' .:-=+*#%@'
        self.size = ()
    
    def select_ascii_char(self, pixel):
        unit = 256 / len(self.gray_scale)
        return self.gray_scale[int(pixel/unit)]

    def convert_to_ascii(self, scaling_ratio):
        img = Image.open(self.path).convert('L')
        width, height = img.size
        img = img.resize((int(width*scaling_ratio), int(height*scaling_ratio)), Image.LANCZOS)  # Image.NEAREST Image.BILINEAR Image.BICUBIC Image.LANCZOS
        self.size = width_new, height_new = img.size
        ascii = ''
        for row in range(height_new):
            for col in range(width_new):
                pixel = img.getpixel((col, row))
                ascii += self.select_ascii_char(pixel)
            ascii += '\n'
        return ascii
    
    def save_as_txt_file(self, scaling_ratio=0.5):
        ascii = self.convert_to_ascii(scaling_ratio)
        with open('imgtoascii.txt', 'w') as f:
            f.write(ascii)


if __name__ == '__main__':
    AsciiArt('avatar.png').save_as_txt_file(0.1)

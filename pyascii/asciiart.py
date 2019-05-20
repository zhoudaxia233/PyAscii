# coding: utf-8
import os
import time
import platform
import cv2


class AsciiArt:
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.gray_scale = r'@%#*+=-:. '
        self.num_of_color_levels = len(self.gray_scale)

    def convert(self, target_format, scaling_ratio, font_size=None, line_height=None):
        image = cv2.imread(self.filepath)
        filename = self.filepath.split('.')[0]

        ascii_data = self.img_to_ascii(image, scaling_ratio)

        if target_format == "txt":
            self.save_as_txt_file(ascii_data, filename)
        elif target_format == "html":
            self.save_as_html_file(ascii_data, font_size, line_height, filename)
        else:
            print(f'{target_format} is not supported.')

    def play_video(self, scaling_ratio):
        cap = cv2.VideoCapture(self.filepath)
        try:
            while True:
                get_frame, frame = cap.read()
                if not get_frame:
                    break
                ascii_data = self.img_to_ascii(frame, scaling_ratio)

                if platform.system() == 'Windows':
                    os.system('cls')
                else:
                    os.system('clear')

                print(ascii_data)
                time.sleep(0.01)
        except KeyboardInterrupt:
            pass

    def show_webcam(self, scaling_ratio):
        cap = cv2.VideoCapture(0)
        try:
            while True:
                _, frame = cap.read()
                frame = cv2.flip(frame, 1)  # mirror
                ascii_data = self.img_to_ascii(frame, scaling_ratio)

                if platform.system() == 'Windows':
                    os.system('cls')
                else:
                    os.system('clear')

                print(ascii_data)
                time.sleep(0.01)
        except KeyboardInterrupt:
            pass

    def select_ascii_char(self, pixel):
        unit = 256 / self.num_of_color_levels
        return self.gray_scale[int(pixel / unit)]

    def img_to_ascii(self, image, scaling_ratio):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width = image.shape
        image_ = cv2.resize(image, (int(width * scaling_ratio), int(height * scaling_ratio)),
                            interpolation=cv2.INTER_LANCZOS4)

        height_, width_ = image_.shape
        ascii_data = ''
        for row in range(height_):
            for col in range(width_):
                pixel = image_[row, col]
                ascii_data += self.select_ascii_char(pixel)
            ascii_data += '\n'
        return ascii_data

    @staticmethod
    def save_as_txt_file(ascii_data, output_filename):
        with open(f'{output_filename}.txt', 'w') as f:
            f.write(ascii_data)

    @staticmethod
    def save_as_html_file(ascii_data, font_size, line_height, output_filename):
        html = '''<!DOCTYPE HTML>
                <html>
                <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                <style type="text/css">
                    pre {
                    word-wrap: break-word;      /* IE 5.5-7 */
                    white-space: -moz-pre-wrap; /* Firefox 1.0-2.0 */
                    white-space: pre-wrap;      /* Modern browsers */
                    font-family: 'Monaco', 'Consolas', monospace;
                    line-height: %.2f;
                    font-size: %dpx;
                    }
                </style>
                </head>
                <body>
                <pre>%s</pre>
                </body>
                </html>
                '''
        html = html % (line_height, font_size, ascii_data)
        with open(f'{output_filename}.html', 'w') as f:
            f.write(html)

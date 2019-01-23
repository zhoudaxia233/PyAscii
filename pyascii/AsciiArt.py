#! /usr/bin/env python3
# coding: utf-8
from PIL import Image


class AsciiArt():
    def __init__(self):
        self.gray_scale = r'@%#*+=-:. '

    def __select_ascii_char(self, pixel):
        unit = 256 / len(self.gray_scale)
        return self.gray_scale[int(pixel/unit)]

    def convert_file(self, input_image_path, output_filename, conversion_format="txt",
                     scaling_ratio=0.5,
                     font_size=5, line_height=0.65):
        """Convert a image file to ASCII

        Arguments:
            input_image_path {string} -- Input image path

        Keyword Arguments:
            output_filename {string} -- Output file path
            conversion_format {str} -- Output file format (default: {"txt"})
            scaling_ratio {float} -- Image rescaling ratio (default: {0.5})
            font_size {int} -- Font size for HTML styling (default: {5})
            line_height {float} -- Line height for HTML styling (default: {0.65})
        """
        image = Image.open(input_image_path)

        ascii_data = self.convert_to_ascii(image, scaling_ratio)

        if conversion_format == "txt":
            self.save_as_txt_file(ascii_data, output_filename)
        if conversion_format == "html":
            self.save_as_html_file(ascii_data, font_size, line_height, output_filename)

    def convert_to_ascii(self, image, scaling_ratio=0.5):
        """Convert image file to ASCII

        Arguments:
            image {ndarray} -- OpenCV image array
            scaling_ratio {float} -- Image rescaling ratio

        Returns:
            ndarray -- Image data as ASCII
        """
        image = image.convert('L')
        width, height = image.size
        image = image.resize((int(width*scaling_ratio), int(height*scaling_ratio)), Image.LANCZOS)

        width_new, height_new = image.size
        ascii_data = ''
        for row in range(height_new):
            for col in range(width_new):
                pixel = image.getpixel((col, row))
                ascii_data += self.__select_ascii_char(pixel)
            ascii_data += '\n'
        return ascii_data

    def save_as_txt_file(self, ascii_data, output_filename):
        """Saves image as ASCII text file

        Arguments:
            ascii_data {ndarray} -- OpenCV image array
            output_filename {string} -- Output HTML file path
        """
        with open(f'{output_filename}.txt', 'w') as f:
            f.write(ascii_data)

    def save_as_html_file(self, ascii_data, font_size, line_height, output_filename):
        """Save image as HTML file

        Arguments:
            ascii_data {ndarray} -- OpenCV image array
            font_size {float} -- Font size for HTML styling
            line_height {float} -- Line height for HTML styling
            output_filename {string} -- Output HTML file path
        """
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

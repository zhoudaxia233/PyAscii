# coding: utf-8
from PIL import Image


class AsciiArt:
    def __init__(self):
        self.gray_scale = r'@%#*+=-:. '
        self.num_of_color_levels = len(self.gray_scale)

    def convert(self, filepath, target_format, scaling_ratio, font_size=None, line_height=None):
        image = Image.open(filepath)
        filename = filepath.split('.')[0]

        ascii_data = self.__img_to_ascii(image, scaling_ratio)

        if target_format == "txt":
            self.save_as_txt_file(ascii_data, filename)
        elif target_format == "html":
            self.save_as_html_file(ascii_data, font_size, line_height, filename)
        else:
            print(f'{target_format} is not supported.')

    def __select_ascii_char(self, pixel):
        unit = 256 / self.num_of_color_levels
        return self.gray_scale[int(pixel/unit)]

    def __img_to_ascii(self, image, scaling_ratio):
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

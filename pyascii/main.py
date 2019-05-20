# coding: utf-8
import argparse
from .asciiart import AsciiArt


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-s', '--scaling_ratio', help="set scaling ratio", type=float, default=0.5)
    parser.add_argument('-o', '--output_format', help="set output format", type=int, default=1)
    parser.add_argument('-fs', '--font_size', help="set font size", type=int, default=5)
    parser.add_argument('-lh', '--line_height', help="set line height", type=float, default=0.65)

    args = parser.parse_args()
    return args.input, args.scaling_ratio, args.output_format, args.font_size, args.line_height


def is_image(filepath):
    img_formats = ['jpg', 'jpeg', 'png', 'bmp', 'dib', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'tiff', 'tif']
    file_format = filepath.split('.')[-1]
    if file_format in img_formats:
        return True
    return False


def main():
    input_, scaling_ratio, output_format, font_size, line_height = init()
    asciiart = AsciiArt(input_)

    if input_ == "webcam":
        asciiart.show_webcam(scaling_ratio)

    elif is_image(input_):
        if output_format == 0:
            asciiart.convert(target_format="txt", scaling_ratio=scaling_ratio)
        elif output_format == 1:
            asciiart.convert(target_format="html",
                             scaling_ratio=scaling_ratio,
                             font_size=font_size,
                             line_height=line_height)
        elif output_format == 2:
            asciiart.convert(target_format="txt", scaling_ratio=scaling_ratio)
            asciiart.convert(target_format="html",
                             scaling_ratio=scaling_ratio,
                             font_size=font_size,
                             line_height=line_height)
        else:
            raise ValueError('Possible values are 0, 1 and 2.')

    else:
        asciiart.play_video(scaling_ratio)

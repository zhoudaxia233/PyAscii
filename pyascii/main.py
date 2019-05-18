# coding: utf-8
import argparse
from .asciiart import AsciiArt


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-s', '--scaling_ratio', help="set scaling ratio", type=float, default=0.5)
    parser.add_argument('-o', '--output_format', help="set output format", type=int, default=1)
    parser.add_argument('-fs', '--font_size', help="set font size", type=int, default=5)
    parser.add_argument('-lh', '--line_height', help="set line height", type=float, default=0.65)

    args = parser.parse_args()
    return args.file, args.scaling_ratio, args.output_format, args.font_size, args.line_height


def main():
    img_path, scaling_ratio, output_format, font_size, line_height = init()
    asciiart = AsciiArt()
    if output_format == 0:
        asciiart.convert(filepath=img_path,
                         target_format="txt",
                         scaling_ratio=scaling_ratio)
    elif output_format == 1:
        asciiart.convert(filepath=img_path,
                         target_format="html",
                         scaling_ratio=scaling_ratio,
                         font_size=font_size,
                         line_height=line_height)
    elif output_format == 2:
        asciiart.convert(filepath=img_path,
                         target_format="txt",
                         scaling_ratio=scaling_ratio)
        asciiart.convert(filepath=img_path,
                         target_format="html",
                         scaling_ratio=scaling_ratio,
                         font_size=font_size,
                         line_height=line_height)
    else:
        raise ValueError('Possible values are 0, 1 and 2.')


if __name__ == '__main__':
    main()

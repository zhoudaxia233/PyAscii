#! /usr/bin/env python3
# coding: utf-8
from AsciiArt import AsciiArt
import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--scaling_ratio', type=float, default=0.5)
    parser.add_argument('--output_format', type=int, default=2)
    parser.add_argument('--font_size', type=int, default=5)
    parser.add_argument('--line_height', type=float, default=0.80)

    args = parser.parse_args()
    return (args.file, args.scaling_ratio, args.output_format, args.font_size, args.line_height)

def main():
    img_path, scaling_ratio, output_format, font_size, line_height = init()
    filename = img_path.split('.')[0]
    asciiart = AsciiArt(img_path)
    if output_format == 0:
        asciiart.save_as_txt_file(scaling_ratio, filename)
    elif output_format == 1:
        asciiart.save_as_html_file(scaling_ratio, filename, font_size, line_height)
    elif output_format == 2:
        asciiart.save_as_txt_file(scaling_ratio, filename)
        asciiart.save_as_html_file(scaling_ratio, filename, font_size, line_height)
    else:
        raise ValueError('Possible values are 0, 1 and 2.')


if __name__ == '__main__':
    main()

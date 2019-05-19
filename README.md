# PyAscii

## Some Amazing examples
[1. A Beautiful Girl drawed by me](http://zhoudaxia.eu/PyAscii/examples/test1.html)  
[2. Famous Yaoming's Face](http://zhoudaxia.eu/PyAscii/examples/yaoming.html)  
[3. My Avatar](http://zhoudaxia.eu/PyAscii/examples/avatar.html)

---
## To do list
- [x] Asciify an image into `txt` & `html`
- [x] Asciify a video
- [x] Improve ascii video quality (by thresholding???)
- [ ] Asciify webcam feed

---
## Requirements
1. `Python >= 3.6`
2. `opencv-python >= 4.0.0` (It will automatically be installed when you install `pyascii`)

---
## Installation
Install `pyascii`:

```bash
pip install pyascii
```

---

## Usage
##### 1. Asciify an image
```bash
pyascii avatar.png
```
You can use `-s` or `--scaling_ratio` to specify the scaling ratio of the output with respect to the input image. The default value is `0.5`.  
```bash
pyascii avatar.png -s 0.1
```

You can use `-o` or `--output_format` to specify the format of the output file.  
>`0` represents for `.txt` format  
`1` represents for `.html` format  
`2` represents for both `.txt` format & `.html` format

The default value is `1`.
```bash
pyascii avatar.png -o 0
```

You can use `-lh` or `--line_height` to specify the height of each line of ascii characters in the output file. The default value is `0.65`.
> Note: It only works for `html` format output.
```bash
pyascii avatar.png -lh 0.65
```

You can use `-fs` or `--font_size` to specify the font size of ascii characters in the output file. The default value is `5`.
> Note: It only works for `html` format output.
```bash
pyascii avatar.png -fs 8
```

##### 2. Asciify a video
```bash
pyascii demo.mp4
```
You can use `-s` or `--scaling_ratio` to specify the scaling ratio of the output with respect to the input image. The default value is `0.5`.  
```bash
pyascii demo.mp4 -s 0.1
```

# AsciiArt

<img src="https://raw.githubusercontent.com/zhoudaxia233/AsciiArt/develop/cover.png" width="256">

- [x] Asciify an image into `txt` & `html` (naive algorithm)
- [ ] Asciify an image into `txt` & `html` (advanced algorithm)
- [ ] Asciify many images parallelly
- [ ] Asciify a GIF
- [ ] Asciify a video

---
## Requirements
1. `Python3`
2. `Pillow-5.1.0` (Only this version has been tested, other versions may also work)

---

## Usage
```
./main.py avatar.png
```
You can use `--scaling_ratio` to specify the scaling ratio of the output with respect to the input image. The default value is `0.5`.  
```
./main.py avatar.png --scaling_ratio 0.1
```

You can use `--output_format` to specify the format of the output file.  
>`0` represents for `.txt` format  
`1` represents for `.html` format  
`2` represents for both `.txt` format & `.html` format

The default value is `2`.
```
./main.py avatar.png --output_format 1
```

You can use `--line_height` to specify the height of each line of ascii characters in the output file. The default value is `0.80`.
```
./main.py avatar.png --line_height 0.90
```

You can use `--font_size` to specify the font size of ascii characters in the output file. The default value is `5`.
```
./main.py avatar.png --font_size 8
```

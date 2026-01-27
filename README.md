# BMP Encoder
A small tool written in Python3 to write a pixel map to a .bmp file with 24 bits per pixel.  
  
## Usage  
```
import Main as bmp_w
name = 'readme_demo'
width = 2
height = 3
pixels = [['#000000', '#000000'],
          ['#000000', '#000000'],
          ['#000000', '#000000']]
bmp_w.write_bmp('name', width, height, pixels)
```

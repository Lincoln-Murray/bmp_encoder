import Main as bmp_w

width = 960
height = 540
start = (0, 0, 255)
end = (255, 0, 0)
pixels = []
for y in range(0, height):
    pixels.append([])
    for x in range(0, width):
        pixels[y].append([])
        percent_x = x/width
        percent_y = y/width
        percent = percent_x*percent_y
        pixels[y][x] = '#%02x%02x%02x' % (int(percent_x*255), int(0.5*(1-percent)*255), int(percent_y*255))
bmp_w.write_bmp('demo', width, height, pixels)
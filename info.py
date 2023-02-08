from PIL import Image, ImageFont, ImageDraw

def print_logo():
    ShowText = 'D N P'
# font = ImageFont.truetype(font=None, size=15) #load the font
# size = font.getsize(ShowText)  #calc the size of text in pixels
    size = (35, 12)
    image = Image.new('1', size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
# draw.text((0, 0), ShowText, font=font) #render the text to the bitmap
    draw.text((0, 0), ShowText)

    for row_num in range(size[1]):
    # scan the bitmap:
    # print ' ' for black pixel and
    # print '#' for white one
        line = []
        for col_num in range(size[0]):
            if image.getpixel((col_num, row_num)):
                line.append(' '),
            else:
                line.append('#'),
        print(''.join(line))

import epd1in54
import time
from PIL import Image, ImageDraw, ImageFont


def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)

    image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('anonymouspro.ttf', 24)
    draw.rectangle((0, 10, 200, 34), fill = 0)
    draw.text((8, 12), 'Hello world!', font = font, fill = 255)
    draw.text((8, 36), 'e-Paper Demo', font = font, fill = 0)
    draw.line((16, 60, 56, 60), fill = 0)
    draw.line((56, 60, 56, 110), fill = 0)
    draw.line((16, 110, 56, 110), fill = 0)
    draw.line((16, 110, 16, 60), fill = 0)
    draw.line((16, 60, 56, 110), fill = 0)
    draw.line((56, 60, 16, 110), fill = 0)
    draw.arc((90, 60, 150, 120), 0, 360, fill = 0)
    draw.rectangle((16, 130, 56, 180), fill = 0)
    draw.chord((90, 130, 150, 190), 0, 360, fill = 0)
    
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()

    epd.delay_ms(2000)

    epd.init(epd.lut_partial_update)
    image = Image.open('monocolor.bmp')
    image = image.resize(((epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT)), Image.ANTIALIAS)

    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()


if __name__ == '__main__':
    main()

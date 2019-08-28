import epd1in54
import time
from PIL import Image, ImageDraw, ImageFont


def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)

    image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('fonts/Comfortaa-Regular.ttf', 11)

    draw.text((14, 24), 'ABCČĆDĐEFGHIJKLMNOPQR', font= font, fill= 0)
    draw.text((14, 36), 'SŠTUVWXYZŽabcčćdđefghijk', font= font, fill= 0)
    draw.text((14, 48), 'lmnopqrsštuvwxyzžАБВГҐДЂ', font= font, fill= 0)
    draw.text((14, 60), 'ЕГҐДЂЕЁЄЖЗЅИІЇЙЈКЛЉМН', font= font, fill= 0)
    draw.text((14, 72), 'ЊОПРСТЋУЎФХЦЧЏШЩЪЫ', font= font, fill= 0)
    draw.text((14, 84), 'ЬЭЮЯабвгґдђеёєжзѕиіїйјклљ', font= font, fill= 0)
    draw.text((14, 96), 'мнњопрстћуўфхцчџшщъыьэ', font= font, fill= 0)
    draw.text((14, 108), 'эюяΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤ', font= font, fill= 0)
    draw.text((14, 120), 'ΥΦΧΨΩαβγδεζηθικλμνξοπρστυ', font= font, fill= 0)
    draw.text((14, 132), 'φψωĂÂÊÔƠƯăâêôơư12345678', font= font, fill= 0)
    draw.text((14, 144), '9χ0‘?’“!”(%)[#]{@}/&\<-+÷×=>®©$', font= font, fill= 0)
    draw.text((14, 156), '€£¥¢:;,.*', font= font, fill= 0)
    
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

import epd1in54
import time
from PIL import Image, ImageDraw, ImageFont
import qr


def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)

    image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('../fonts/Comfortaa-Light.ttf', 12)

    text = ['ABCČĆDĐEFGHIJKLMNOPQR',
            'SŠTUVWXYZŽabcčćdđefghijk',
            'lmnopqrsštuvwxyzžАБВГҐДЂ',
            'ЕГҐДЂЕЁЄЖЗЅИІЇЙЈКЛЉМН',
            'ЊОПРСТЋУЎФХЦЧЏШЩЪЫ',
            'ЬЭЮЯабвгґдђеёєжзѕиіїйјклљ',
            'мнњопрстћуўфхцчџшщъыьэ',
            'эюяΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤ',
            'ΥΦΧΨΩαβγδεζηθικλμνξοπρστυ',
            'φψωĂÂÊÔƠƯăâêôơư12345678',
            '9χ0‘?’“!”(%)[#]{@}/&\<-+÷×=>®©',
            '$€£¥¢:;,.*']

    for i in range(len(text)):
        draw.text((8, 12 + 15*i), text[i], font= font, fill= 0)
    
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

    epd.delay_ms(2000)

    epd.init(epd.lut_full_update)
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    
    qr = qrcode.QRCode(box_size=6, version=1, border=0)
    qr.add_data('cokR7rKb3BT1BhGqiF35iCVFr5uJQ6AZ7Q')
    qr.make()
    qr_img = qr.make_image()

    qr_x = int((EPD_WIDTH - qr_img.size[0])/2)
    qr_y = int((EPD_HEIGHT - qr_img.size[1])/2)

    image.paste(qr_img, (qr_x, qr_y))

    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()


if __name__ == '__main__':
    main()

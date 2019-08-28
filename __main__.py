import epd1in54
import time
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import urlencode, quote
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
    
    qr = qrcode.QRCode(box_size=1, version=1, border=2)

    URI = {'label' : "La tiendita de la Chauchita",
        'message' : "1x Chocolito",
        'address' : "1NbfaaU4TM39uWJ5nh3Raze4LAAncEV8E2",
        'amount' : 0.153
        }
        
    URI = urlencode(URI,quote_via=quote)
    print(URI)
    qr.add_data(URI)
    qr.make()
    qr_img = qr.make_image().resize(((EPD_WIDTH, EPD_HEIGHT)), Image.ANTIALIAS)

    image.paste(qr_img, (0,0))

    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()


if __name__ == '__main__':
    main()

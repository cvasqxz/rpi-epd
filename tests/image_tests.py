import time
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import urlencode, quote
import qrcode


EPD_HEIGHT = EPD_WIDTH = 200

def main():
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
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

    image.show()
    
    time.sleep(0.2)

    image = Image.open('../monocolor.bmp')
    image = image.resize(((EPD_WIDTH, EPD_HEIGHT)), Image.ANTIALIAS)
    image.show()

    time.sleep(0.2)

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
    image.show()



if __name__ == '__main__':
    main()

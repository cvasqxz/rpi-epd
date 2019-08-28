import time
from PIL import Image, ImageDraw, ImageFont
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
    
    qr = qrcode.QRCode(box_size=5, version=2, border=0)
    qr.add_data('cokR7rKb3BT1BhGqiF35iCVFr5uJQ6AZ7Q')
    qr.make()
    qr_img = qr.make_image()

    qr_x = int((EPD_WIDTH - qr_img.size[0])/2)

    image.paste(qr_img, (qr_x, 18))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('../fonts/Share-TechMono.ttf', 22)
    price = "90.12345678"

    text_x = int((EPD_WIDTH - draw.textsize(price, font=font)[0])/2)
    draw.text((text_x, 168), price, font= font, fill= 0)

    image.show()



if __name__ == '__main__':
    main()

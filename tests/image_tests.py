import time
from PIL import Image, ImageDraw, ImageFont


EPD_HEIGHT = EPD_WIDTH = 200

def main():
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('../fonts/Comfortaa-Regular.ttf', 11)

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
    image.show()
    
    time.sleep(0.2)

    image = Image.open('../monocolor.bmp')
    image = image.resize(((EPD_WIDTH, EPD_HEIGHT)), Image.ANTIALIAS)
    #image.show()


if __name__ == '__main__':
    main()

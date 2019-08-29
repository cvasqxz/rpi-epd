import spidev
import RPi.GPIO as GPIO
import time
import yaml


with open("config.yml", 'r') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

# Pin definition
RST_PIN = cfg['pinout']['RST_PIN']
DC_PIN = cfg['pinout']['DC_PIN']
CS_PIN = cfg['pinout']['CS_PIN']
BUSY_PIN = cfg['pinout']['BUSY_PIN']

# SPI device, bus = 0, device = 0
SPI = spidev.SpiDev(0, 0)

def epd_digital_write(pin, value):
    GPIO.output(pin, value)

def epd_digital_read(pin):
    return GPIO.input(BUSY_PIN)

def epd_delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_transfer(data):
    SPI.writebytes(data)

def epd_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RST_PIN, GPIO.OUT)
    GPIO.setup(DC_PIN, GPIO.OUT)
    GPIO.setup(CS_PIN, GPIO.OUT)
    GPIO.setup(BUSY_PIN, GPIO.IN)
    SPI.max_speed_hz = 2000000
    SPI.mode = 0b00
    return 0;

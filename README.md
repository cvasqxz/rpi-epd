# rpi-epd
Raspberry Pi E-Paper Display library

## Instalación

### Drivers BCM2835
```
cd bcm2835-1.60
./configure
make
sudo make install
```

### Librerías de Python
```
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip3 install spidev pillow
```

## Ejecución
```
cd rpi-epd
python3 main.py
```

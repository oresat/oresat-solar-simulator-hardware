import board
import busio
import adafruit_mcp4728
from Adafruit_BBIO.SPI import SPI
from numpy import linspace, int16
from time import sleep

# I2C
# Red LED - DAC Channel A
# Red LED - DAC Channel B
# Red LED - DAC Channel C
# Red LED - DAC Channel D

# SPI
# 8 bit address 0-2 & 6-7 are DC
# Therm1  - ADC IN0 - 000 - 0
# Therm2  - ADC IN1 - 001 - 8
# Therm3  - ADC IN2 - 010 - 16
# PhotoD  - ADC IN3 - 011 - 24

running = True
max_voltage = 65535
i2c = busio.I2C(board.SCL, board.SDA)
mcp4728 = adafruit_mcp4728.MCP4728(i2c)
spi = SPI(0, 0)	 # /dev/spidev1.0
steps = linspace(0, max_voltage, num=100, dtype=int16)
direction = 1
i = 0
while running:
    # Red LED
    mcp4728.channel_a.value = max_voltage

    # Green LED
    mcp4728.channel_b.value = max_voltage

    # Blue LED
    mcp4728.channel_c.value = max_voltage

    # UV LED
    mcp4728.channel_d.value = max_voltage

    # SPI Read every 5th set
    if i % 5 == 0:
        spi.writebytes(0)
        print(f"Therm1: {spi.readbytes(8)}")
        spi.writebytes(8)
        print(f"Therm2: {spi.readbytes(8)}")
        spi.writebytes(16)
        print(f"Therm3: {spi.readbytes(8)}")
        spi.writebytes(24)
        print(f"Photo: {spi.readbytes(8)}")
    print(i)
    i += direction
    sleep(0.1)
    if i >= 100 or i <= 0:
        direction *= -1

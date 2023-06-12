import board
import busio
import adafruit_mcp4728
from Adafruit_BBIO.SPI import SPI
from numpy import linspace, uint16
from time import sleep
from Adafruit_I2C import Adafruit_I2C

# I2C
# Red LED - DAC Channel A
# Grn LED - DAC Channel B
# Blu LED - DAC Channel C
# UV  LED - DAC Channel D

# SPI
# 8 bit address 0-2 & 6-7 are DC
# Therm1  - ADC IN0 - 000 - 0
# Therm2  - ADC IN1 - 001 - 1
# Therm3  - ADC IN2 - 010 - 2
# PhotoD  - ADC IN3 - 011 - 3

running = True
max_voltage = 65535
i2c = busio.I2C(board.SCL, board.SDA)
# i2c = Adafruit_I2C(0x60)
mcp4728 = adafruit_mcp4728.MCP4728(i2c)
spi = SPI(0, 0)	 # /dev/spidev1.0
steps = linspace(0, max_voltage, num=100, dtype=uint16)
print(steps)
direction = 1
i = 1
while running:
    # Red LED
    mcp4728.channel_a.value = steps[i]
    # i2c.writeList()

    # Green LED
    mcp4728.channel_b.value = steps[i]

    # Blue LED
    mcp4728.channel_c.value = steps[i]

    # UV LED
    mcp4728.channel_d.value = steps[i]

    # SPI Read every 5th set
    if i % 5 == 0:
        spi.writebytes([0])
        print(f"Therm1: {spi.readbytes(2)}")
        spi.writebytes([1])
        print(f"Therm2: {spi.readbytes(2)}")
        spi.writebytes([2])
        print(f"Therm3: {spi.readbytes(2)}")
        spi.writebytes([3])
        print(f"Photo: {spi.readbytes(2)}")
    print(f'{i}: {steps[i]}')
    i += direction
    sleep(0.1)
    if i >= 99 or i <= 1:
        direction *= -1

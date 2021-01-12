import time
import Adafruit_SSD1306
import Adafruit_LSM303
import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303() # accelerometer setup
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) # dislay setup
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) # gets drwaing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0) # clears screen

# variables to help drawing
padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()

x_Changer = 0

while True:

	#this moves the x value of the point printed along the screen
	x_Value = x + x_Changer


	accel, mag = accelerometer.read() # gets accelerometer data
	accel_x, accel_y, accel_z = accel #sets the acceleration values
	mag_x, mag_y, mag_z = mag #although I don't use this, the .read() taken 6 points of data, so you need to give places for all 6 data points

	#change this to change the data you want plotted	
	#this works best for graphing the Z acceleration
	#dataValue = abs(accel_z)/50

	dataValue = accel_x/10
	print(dataValue)



	draw.text((x, top), "Accelerometer Data:", font=font, fill=255) # draws header
	draw.text((x_Value, top + dataValue),"-", font=font, fill=255) 


	#actually writes to the display
	disp.image(image) # displays x, y, z, and header
	disp.display()

	x_Changer = x_Changer + 1

	time.sleep(.1)

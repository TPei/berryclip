#!/usr/bin/python
# Based on work by Matt Hawkins and Graham Taylor

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid
import time

# Import for BerryClip
import RPi.GPIO as GPIO

# Delay between button presses
button_delay = 0.1
# Duration of flash of pin
flash_duration = 0.2

# Define a function to 'flash' a pin, whether it be LED or Buzzer
def flashPin(pin):
	print "Flashing pin {}".format(pin)
	GPIO.output(pin, True)
	time.sleep(flash_duration)
	GPIO.output(pin, False)

# Initialise the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

# Set up constants for each pin on the BerryClip
print "Initialising BerryClip"
LED_RED_1 = 4
LED_RED_2 = 17
LED_ORA_1 = 22
LED_ORA_2 = 10
LED_GRN_1 = 9
LED_GRN_2 = 11
BUZZER = 8
PIN_LIST = [LED_RED_1,LED_RED_2,LED_ORA_1,LED_ORA_2,LED_GRN_1,LED_GRN_2,BUZZER]

# Set 'em up and turn 'em off
for pin in PIN_LIST:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.setup(pin, False)

print "Testing LEDs and Buzzer"
for pin in PIN_LIST:
	flashPin(pin)

print "Wiimote Pairing..."
print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'

wii.rpt_mode = cwiid.RPT_BTN
wii.rumble = 1
time.sleep(0.5)
wii.rumble = 0
 
print 'Press HOME button or the button on the BerryClip to exit.\n'


while True:
  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  #if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
  #  print '\nClosing connection ...'
  #  exit(wii)  
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    flashPin(LED_RED_1)
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    flashPin(LED_RED_2)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'        
    flashPin(LED_ORA_1)
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'      
    flashPin(LED_ORA_2)
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    flashPin(LED_GRN_1)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    flashPin(LED_GRN_2)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    flashPin(BUZZER)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    exit(wii)
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)

GPIO.cleanup()

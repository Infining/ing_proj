import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # use board layout pin numbering
GPIO.setup(12, GPIO.OUT) # set pin 12 as the ouput pin

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
# will need to do some testing on frequency range
# use p.ChangeFrequency(freq) to change frequency in mid run
p.start(50) # start the pwm with 50% duty cycle
# use p.changeDutyCycle(dc) to change duty cycle in mid run
raw_input("Press Enter to continue...") # pause for user input before cleaning up
p.stop()
GPIO.cleanup()

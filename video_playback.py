import RPi.GPIO as GPIO
import os
import sys
import time
import subprocess
from subprocess import Popen

os.environ['DISPLAY'] = ":0"

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

movie = ("/home/pi/Videos/movie1.mp4")

last_state1 = True
input_state1 = True

quit_video = True

quit_prog = False
display_on = False
player = False

while not quit_prog:
    #Read states of inputs
    input_state1 = GPIO.input(17)
    quit_video = GPIO.input(24)
    #If GPIO(17) is shorted to Ground
    if input_state1 != last_state1:
	if not display_on:
            subprocess.call('xset dpms force on', shell = True) #turn on display before playback
            print '\n', "***Button state changed***"
            display_on = True
            if (player and not input_state1):
                os.system('killall omxplayer.bin')
                omxc = Popen(['omxplayer', '-b', movie])
                player = True
		print '\n', "***Display turned on while player was running***"
	    elif (not player and not input_state1):
		omxc = Popen(['omxplayer', '-b', movie])
		player = True
		print '\n', "***Display turned on while player wasnt running***"
	else:
            print '\n', "**Display turned off***"
            display_on = False
            
    #If omxplayer is running and GIOP(17) are not shorted to Ground
    elif (player and input_state1):
        os.system('killall omxplayer.bin')
	player = False
	display_on = False
	print '\n', "***No button but player is running***"
    else:
        print '\n',"somehow"
        subprocess.call('xset dpms force off', shell = True) #turn off display

    #GPIO(24) to close omxplayer manually - used during debug
    if quit_video == False:         
        os.system('killall omxplayer.bin')
        subprocess.call('xset dpms force on', shell = True) #turn on display 
        player = False
        quit_prog = True
        display_on = False
        print '\n', "***End of program***"


    #Set last_input states
    last_state1 = input_state1
        



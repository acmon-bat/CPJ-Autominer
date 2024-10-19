#!/usr/bin/env python
import pynput.keyboard as kb
import time
import random

keyboard = kb.Controller()

def dance():
    dance_time = random.randint(10, 15)  # Random dance duration between 10 and 15 seconds
    keyboard.press('d')
    keyboard.release('d')
    print('Dancing for {} seconds'.format(dance_time))
    time.sleep(dance_time)

# Start the infinite loop for dancing
while True:
    dance()
    print('Waiting for 2 minutes before the next dance...')
    time.sleep(120)  # Wait for 2 minutes (120 seconds)

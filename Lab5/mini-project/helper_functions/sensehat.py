from sense_hat import SenseHat
import time

# This function returns a SenseHat instance
def get_sensehat():
    sense = SenseHat()
    sense.clear()
    return sense


# This function takes in a SenseHat instance and the flash_time
# The display on the SenseHat flashes red (1 second on, 1 second off) for the duration of flash_time. At the end of the flash_time the SenseHat display should be off.
def alarm(sense,flash_time):
    red = (255, 0, 0)
    off = (0, 0, 0)
    
    start = time.time()
    
    while time.time() - start < flash_time:
        sense.clear(red)
        time.sleep(1)
        sense.clear(off)
        time.sleep(1)
        
    sense.clear()

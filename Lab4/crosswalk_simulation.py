from time import sleep
from gpiozero import Button
from traffic_lights import TrafficLights

PIN_R = 13
PIN_Y = 26
PIN_G = 6
PIN_BUTTON = 19

lights = TrafficLights(PIN_R, PIN_Y, PIN_G) #TrafficLights object
button = Button(PIN_BUTTON)

print("Starting crosswalk simulation...")

while True:
    
    lights.red()
    print("RED")
    sleep(5)

    lights.green()
    print("GREEN - waiting for crosswalk or timeout")

    
    pressed = button.wait_for_press(timeout=5) # Wait up to 5 seconds for a button press

    if pressed:
        print("Crosswalk requested!")
        sleep(0.5)   # small delay before changing

   
    lights.yellow()
    print("YELLOW")
    sleep(2)
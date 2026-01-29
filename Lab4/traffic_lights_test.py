from gpiozero import LED
from traffic_lights import TrafficLights
from time import sleep


PIN_R = 13 
PIN_Y = 26 
PIN_G = 6 

lights = TrafficLights(PIN_R, PIN_Y, PIN_G) #TrafficLights object

lights.red() #testing red light
sleep(0.5)


assert lights.red_led.value == 1, "Red light should be ON"
assert lights.yellow_led.value == 0, "Yellow light should be OFF"
assert lights.green_led.value == 0, "Green light should be OFF"

print("Red test passed")


lights.yellow() #testing yellow light
sleep(0.5)


assert lights.red_led.value == 0, "Red light should be OFF"
assert lights.yellow_led.value == 1, "Yellow light should be ON"
assert lights.green_led.value == 0, "Green light should be OFF"

print("Yellow test passed")

lights.green() #testing green light
sleep(0.5)


assert lights.red_led.value == 0, "Red light should be OFF"
assert lights.yellow_led.value == 0, "Yellow light should be OFF"
assert lights.green_led.value == 1, "Green light should be ON"

print("Green test passed")
print("\nAll TrafficLights tests passed")



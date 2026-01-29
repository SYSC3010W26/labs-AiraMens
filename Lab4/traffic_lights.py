from gpiozero import LED


class TrafficLights:
    def __init__(self, pin_r, pin_y, pin_g):
        self.red_led = LED(pin_r)
        self.yellow_led = LED(pin_y)
        self.green_led = LED(pin_g)
        
        self.all_off()
        
        
    def all_off(self):
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.off()
        
        
    def red(self):
        self.all_off()
        self.red_led.on()
        
        
    def yellow(self):
        self.all_off()
        self.yellow_led.on()
        
        
    def green(self):
        self.all_off()
        self.green_led.on()
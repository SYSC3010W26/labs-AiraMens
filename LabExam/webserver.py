#imports flask, render_template, socketIO, send, emit, from flask_socketio, json

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json
from sense_hat import SenseHat #import sensehat

sense = SenseHat() #creating sensehat object

colors = [[10,10,10] for i in range(64)] #list to hold the RGB values for all 64 LEDs
app = Flask(__name__) #Flask application instance
app.config['SECRET_KEY'] = 'secret!' #required secret key

socketio = SocketIO(app) #attach the server to the Flask app

# Converts a RGB color expressed in HEX to RGB. HEX comes 
# from the server, and RGB array used by SenseHAT.
def hex_to_rgb_color(color: str):
    color = color.strip('#')
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    return rgb

# Button ids on html are integers. 
# This function maps the led index to x and y.
def map_index_to_xy(led_index: int):
    return int(led_index%8), int(led_index/8)

@app.route('/') #Flask route for root page
def index():
    return render_template('Lab3-Colour-Picker.html') #send HTML file to browser

# When users connect to the server using a webbrowser, a websocket is opened 
# and this function is called to send the current LED colors
@socketio.on('connect')
def send_led_colors():
    print (f"sending colors.. {json.dumps(dict(colors=colors))}")
    emit('current_colors', json.dumps(dict(colors=colors)))

# When user clicks on a <div> in the webpage, the javascript sends a 
# message encoded as update_led, where data contains the id of the <div>
# and the color of set in the <colorpicker>.
# Once the color is set, the server sends a broadcast message to all 
# connected clients, which updates the LED color at each webbrowser screen. 
@socketio.on('update_led')
def update_led_color(data):
    data = json.loads(data) #convert JSON string to py dictionary
    color_rgb = hex_to_rgb_color(data['color'])
    colors[int(data['id'])] = color_rgb #store new RGB color in colors array
    x, y = map_index_to_xy(int(data['id'])) #convert LED index to SenseHAT coordinates
    sense.set_pixel(x, y, color_rgb) #update physical LED
    # Sends broadcast message to connected users.     
    emit('update_led', 
         json.dumps(dict(
            id=data['id'],
            color=data['color'])), #send LED id and color back to clients
         broadcast=True) #ensure every client receives the update
    
@socketio.on('clear_leds') # Register handler for clear LED button presses
def clear_leds():          #Function that runs when clear_leds event received
    #for i in range(64):     #loop through every LED index
        #colors[i] = [0, 0, 0] # Reset color array to black
    #sense.clear()       #Turn off all LEDs on SenseHAT
    for y in range(4, 8):
        for x in range(8):
            sense.set_pixel(x, y, 255, 0, 0) 
    emit('clear_leds', broadcast=True) # Broadcast clear command to all clients

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True) #start Flask and websocket serer

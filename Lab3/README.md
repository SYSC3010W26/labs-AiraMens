# SYSC3010 Lab3 Deliverables

# Lab3: IoT and Inter-computer Communication

##  Script Deliverables' overview

### Student name and ID: Ayra Mensah, 101221911


**1. [lab3-firebase.py](https://github.com/SYSC3010W26/labs-AiraMens/blob/main/Lab3/lab3-firebase.py)**

This script creates a firebase database, grabs environment data from SenseHat, populates the master database for the team, and retrieves the latest inputs in teammates' databases.

**2.  [myflaskwebserver.py](https://github.com/SYSC3010W26/labs-AiraMens/blob/main/Lab3/myflaskwebserver.py)**

This script starts a basic Flask server, renders a '[hello.html](https://github.com/SYSC3010W26/labs-AiraMens/blob/main/Lab3/templates/hello.html)' template using Jinja2.

**3. [webserver.py](https://github.com/SYSC3010W26/labs-AiraMens/blob/main/Lab3/myflaskwebserver.py)**

This script uses flask-socketio to control
the colors of the LEDs for a SenseHAT display.

**4. [hello_html](https://github.com/SYSC3010W26/labs-AiraMens/blob/main/Lab3/templates/hello.html)**

This is a simple html script that prints 'Hello' + 'myname' ie. whatever name it is passed from the [myflaskwebserver.py](https://github.com/SYSC3010W26/labs-AiraMens/blob/main/Lab3/myflaskwebserver.py) script.

from helper_functions import camera, computer_vision, sensehat
import time
### TO-DO: You may require more imports

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)


def main():
    camera_i = camera.get_camera() #DO NOT MODIFY, function call must work as is 
    sense = sensehat.get_sensehat() #DO NOT MODIFY, function call must work as is 
    
    already_background_image = input("Enter '1' if a background image is saved in 'data/images/background.jpg': \n")
    #take_background_image = True #TO-DO: Should be a user input
    take_background_image = input("Enter '2' to take the background image: \n")  

    if take_background_image:
        ### TO-DO: Countdown image capture of background
        print("Get out of the scene")
        print("Background image will be taken in 10 seconds... ")
        countdown(10)
        
        preview = False
        cd_time=0
        camera.capture_image(camera_i,"data/images/background.jpg", countdown_time=cd_time, preview=preview) #DO NOT MODIFY, function call must work as is 
    
    #arm_system = True #TO-DO: Should be a user input
    arm_system = input("Would you like to arm the system? y/n: \n").lower() == "y"

    if arm_system:
        #interval = 10 #TO-DO: Should be a user input
        #t1 = 480000000 #TO-DO: Should be a user input
        
        interval = int(input("Enter the interval between test images in seconds: \n"))
        t1 = int(input("Enter the threshold t1 : \n"))
        print("Monitoring will begin in 10 seconds... ")
       
       ### TO-DO: Countdown to monitoring
        countdown(10)

        count = 0
        while True: #DO NOT MODIFY, function call must work as is 
            camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval) #DO NOT MODIFY, function call must work as is 
            person_detected = computer_vision.person_detected("data/images/background.jpg","data/images/image%s.jpg" % count, t1)  #DO NOT MODIFY, function call must work as is 
            if person_detected: #DO NOT MODIFY, function call must work as is 
                print("Person Detected") #DO NOT MODIFY, function call must work as is 
                sensehat.alarm(sense,interval)  #DO NOT MODIFY, function call must work as is 
            else:
                print("No Person Detected") #DO NOT MODIFY, function call must work as is 
            count += 1


if __name__ == "__main__":
    main()
from PIL import Image
import numpy as np


#Takes in image1 and image2 locations and t1
#returns a Boolean indicating if a "person” is in the image based on t1
def person_detected(image1_file,image2_file, t1):
    img1 = Image.open(image1_file).convert("RGB")
    img2 = Image.open(image2_file).convert("RGB")
    
    array1 = np.array(img1)    
    array2 = np.array(img2)
    
    array_subtract = np.subtract(array1, array2)
    array_diff = np.abs(array_subtract)
    
    total_diff = np.sum(array_diff)
    
    print("Difference value:", total_diff)
    
    return total_diff > t1

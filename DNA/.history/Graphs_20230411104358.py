import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'256':0.0159, '512':0.004, '1024':0.005}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Image Size")
plt.ylabel("Execution time in s")
plt.title("LSB decoding Steganography")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'256':2.88, '512':2.55, '1024':2.44}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Image Size")
plt.ylabel("Execution time in s")
plt.title("LS")
plt.show()
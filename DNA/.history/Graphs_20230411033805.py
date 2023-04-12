import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'256':0.55, '512':2.69, '1024':19.22}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("Execution time in ")
plt.title("Students enrolled in different courses")
plt.show()
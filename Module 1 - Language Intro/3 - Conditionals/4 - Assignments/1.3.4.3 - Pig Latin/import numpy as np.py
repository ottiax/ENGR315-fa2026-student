import numpy as np

new_array = np.array([[11, 22, 33],[44, 55, 66],[77, 88, 99]])

print(new_array)

print(new_array[1, 1]) 

print(new_array[2, 2])  

print(new_array[2,2]) # # Accessing the element in the third row, third column
print(new_array[1:3, :2]) # Accessing the element in the first row, second column
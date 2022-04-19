## 2. Introduction to Ndarrays ##

import numpy as np
data_ndarray = np.array([10,20,30])

## 4. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))
    
# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment

taxi = np.array(converted_taxi_list)

## 5. Array Shapes ##

taxi_shape =(taxi.shape)
print(taxi_shape)

## 6. Selecting and Slicing Rows and Items from Ndarrays ##

row_0 = taxi[0]
rows_391_to_500 = taxi[391:501]
row_21_column_5 = taxi[21][5]
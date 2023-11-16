#Head and Tail Functions in Series
#head()
#head() will show the first 5 rows. 
#You can pass it a number to see more or less.
import pandas as pd
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10,])
data1 = pd.Series(array1)
print("Using head funtion to print first 5 rows of a series")
print(data1.head())
print("To access first 3 rows we can call \"\n\"series_name.head(3)\"")
print(data1.head(3))
print("To print more that 5 row you can pass number")
print(data1.head(7))#it will print first 7 rows of the series


#tail()
#tail() function used to access the last 5 row of the Series
#tail() will show the first 5 rows
#You can pass it a number to see more or less.
print("To print last 5 rows of the series.")
print(data1.tail())#if we not pass any number to the head or tail function, it will print 5 last rows
 
#you can pass a number to see more or less rows in the series
print("To print last 3 rows of the Series")
print(data1.tail(3))
print("To print last 7 rows of the series.")
print(data1.tail(7))

#summery
#head() - Top-bottom approach
#       - default it will print first 5 rows

#tail() -  Bottom-up approach
#       - default it will print first 5 rows

        
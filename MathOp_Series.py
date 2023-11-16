#Mathematical Operation in Series
import pandas as pd
data1 = pd.Series([1,2,3,4,5,6,7,8,9], index=["a","b","c","d","e","f","g","h","i"])
data2 = pd.Series([10,20,30,40,50,60,70,80,90], index=["a","b","c","d", "e", "f","g","h", "j"])
data3 = pd.Series([10,20,30,40,50,60,70])

# Multiply values
print("MUltiplication")
print(data1 * data2)

#incase of size of index is not matched the it shows NaN values for remaining index values
print(data1 * data3)

#print Square value of the Series
print("Square value of the series")
print(data1 ** 2)

#print Cube value of the series
print("Cube values of the Series")
print(data1 **3)

#Addision operation
print("Addission of Series")
print(data1 +data2)
print(data1.add(data2))
#
print(data1.add(data3))

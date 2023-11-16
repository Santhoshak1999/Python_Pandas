#Creating a Pandas Series
# https://www.geeksforgeeks.org/python-pandas-series/

#import pandas as pd
import pandas as pd

#import numpy to create array
import numpy as np

#Create simple array using numpy
array = np.array([12,4,2,734,65,322])

#create Series using pandas
series = pd.Series(array, index=["f","s","t","f","f","s"])

#Print the series
print(series)



#Create a series from dictionary
dictionary = {"Name":"santhosha", "Cource":"MCA", "durarion":"2 years"}
data = pd.Series(dictionary)
print(data)
print("*In the above example, the keys \"Name\", \"Cource\", and \"Duration\" becomes the indexs of the series \nAnd the values of \"Santhosha\", \"MCA\" and \"2 Years\" becomes corresponding data")
print("*The 'dtype:int64' indicates that the data types of the values in the Series is 64-bit interger.")
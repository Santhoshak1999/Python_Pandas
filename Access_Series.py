#There are two ways to access elements of series, they are
# 1.Accessing Element from Series with Position
# 2.Accessing Element Using Lable(Index) 


#Accessing Element from Series with Position
import pandas as pd
import numpy as np
array = np.array([1,2,3,4,5,6])
data = pd.Series(array)
print(data[::2])

#Accessing Elements Using Label(Index):
# In order to access element from series, we have to set values by index label. A series is like a fixed-size dictionary in that you can get and set values by  index label

_array1 = np.array([9,8,7,6,5,4])
data = pd.Series(_array1, index=['nine', 'eight', "seven", "six", "five", "four"])
print(data['nine'])

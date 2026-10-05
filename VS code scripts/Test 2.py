"""Test 2> Playing with lists"""

# Author : ritik.anand@ntnu.no
# Date : 2026-09-04
#%%
list1 = [1,2,3,4,5,6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#%%
import numpy as np
arr1 = np.array(list1)
arr2 = np.array(list2)
print(list1+list2) # concatenating two lists
print(arr1+arr2) # adding two arrays

# %%
print(arr1*arr2) # multiplying two arrays

# %%
list3 = ['apple', 'cherry', 5, 6, 7, 'banana', 'date']
list4 = ['avocado', 'fig', 'grape', 8, 9, 10, False]
#%%
print(list3+list4) # concatenating two lists
# %%
list_a= [1, 2, 3, 4, 5]
list_b= [6, 7, 8, 9, 10]
list_c= ['apple', 'banana', 'cherry', 'date', 'elderberry']

print(list_a*list_b) # concatenating two lists
# %%

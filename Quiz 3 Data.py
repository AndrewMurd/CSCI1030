# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:48:57 2019

@author: andre
"""
import numpy as np
import sklearn.datasets as datasets
import matplotlib.pyplot as pyplot

data = datasets.load_iris().data

data[:10]

def get_data_shape():
    return data.shape
    pass

def get_last_samples(n):
    return data[-n:]
    pass

def get_sepal_width():
    return data[:, 1:3]
    pass

def get_petal_area():
    arr = np.empty((10,))
    for i in range(10): 
        arr[i] = data[i,2] * data[i,3]
    return arr
    pass

def get_samples_top_percentile_by_petal_area(p):
    arr = get_petal_area()
    result = []
    num = np.percentile(arr, p)
    print(num)
    for area in arr:
        if area <= num:
            result.append(area)
    return result
    pass




a = [[1, 2, 3, 4], 
     [5, 6, 3, 4], 
     [7, 8, 9, 2]]

print(a[1][1:3] + a[2][1:3])




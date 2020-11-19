# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:51:23 2019

@author: andre
"""

import pandas as pd
import numpy as np

def build_df():
    
    dic = {'month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb'],
        'city': ['Toronto', 'Montreal', 'Ottawa', 'Vancouver', 'Toronto', 'Montreal', 'Toronto', 'Montreal', 'Montreal'],
        'product_name': ['bread', 'bread', 'bread', 'bread', 'cheese', 'cheese', 'bread', 'bread', 'cheese'],
        'sales': [190, 210, 190, 210, 310, 510, 230, 220, 310]
        }
    
    df = pd.DataFrame(dic,columns= ['month', 'city', 'product_name', 'sales'])
    
    return df;


def cheese_rows(df):
    return df.loc[df.product_name == 'cheese', ["month", "city", "product_name", "sales"]]


def cheese_sales(df, month):
    df1 = pd.DataFrame(df.loc[df.month == month, ["month", "city", "product_name", "sales"]])
    df2 = pd.DataFrame(df1.loc[df1.product_name == 'cheese', ["city", "sales"]])
    
    return df2

df = build_df()
 
cheese_1 = cheese_sales(df, 'Jan')
cheese_2 = cheese_sales(df, 'Feb')

print(cheese_1, '\n')

print(cheese_2)


print(cheese_1.sales.sum())
print(cheese_2.sales.sum())
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:11:31 2021

@author: user
"""

fruits = ['apple','banana','orange','cherry','orange']

name = input('找尋水果')

n = fruits.count(name)

if n != 0:

    index = 0

    for i in range(n):
        index = fruits.index(name,index)
    print(index)
    index +=1
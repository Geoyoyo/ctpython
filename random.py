# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:57:48 2021

@author: user
"""

import random  #隨機亂數，要先import

r = random.random()      #浮點數
i = random.randint(1,50) #整數
print(r)
print(i)

ans = random.randint(1,100)
guess = 0
while ans != guess:
    guess = int(input('輸入1-100之間整數猜數'))
    if guess > ans:
        print('猜小一點')
    if guess < ans:
        print('猜大一點')
print('恭喜猜中')
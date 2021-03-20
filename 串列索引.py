# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:46:50 2021

@author: user
"""

num = [1,2,3,4,5,6,7,8,9]

n1 = num[:5]    #冒號左邊為初始位置，右邊為結束位置
n2 = num[2:7]
n3 = num[2:]
n4 = num[0:6:2] #若有三段，最右邊則為間隔

print(n1)
print(n2)
print(n3)
print(n4)

fruits = ['apple','banana','orange','cherry']

n = fruits.index('orange') #在陣列中找出索引值
print(n)

name = input('找尋水果')
if fruits.count(name) != 0: #以輸入的名稱去找串列中內容
    print('{}在索引值:{}'.format(name,fruits.index(name)))
else: print('找不到')


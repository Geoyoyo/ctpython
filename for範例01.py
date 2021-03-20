# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:03:37 2021

@author: user
"""

start = int(input("初始值:"))
end = int(input("終止值:"))
sep = int(input("間隔值:"))
for i in range(start,end,sep):
    if i % 2 == 0:  #取偶數
        print(i,'是偶數')
    else:
        print(i,'是奇數')
print('程式執行完畢')
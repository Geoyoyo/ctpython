# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:47:25 2021

@author: user
"""
"""
欄位順序：
左至右:0,1,2,3,4,5.....
右至左:-1,-2,-3,-4,-5....
"""
data = [10,20,'John',3.14,10,False]

print(data[2])
print(data[5])
print(data[1])

data[2] = 50 #重新定義data的欄位內容
print(data[2])


#抓欄位內容的方式
for i in range(6):
    print(data[i])
    
print('='*50)

for i in range(len(data)):  #len表示長度
    print(data[i])
    
print('='*50)

for i  in data:            #只有資料沒有索引值
    print(i)






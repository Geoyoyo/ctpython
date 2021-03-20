# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:07:43 2021

@author: user
"""

"""
求使用者輸入一個範圍的整數，
    (1)求4的倍數有哪些?
    (2)求哪些是質數?(只可以被自己跟1整除)使用巢狀迴圈做
"""

start = int(input("初始值:"))
end = int(input("終止值:"))
for i in range(start,end+1,1):
    for n in range(2,i):
        if i % 4 == 0:  
            print(i,'是四的倍數')
            break
        elif i % n == 0 :
            break 
    else:
        print(i,'是質數')
print('程式執行完畢')
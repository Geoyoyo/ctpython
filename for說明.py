# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
range(10)      # 10代表終止值，迴圈只會跑到9，終止值減一
range(0,10)    # 0代表初始值
range(0,10,1)  #1代表間隔值，若為2則為0,2,4,6,8
"""


print(range(10))
print(list(range(10))) #list為把資料轉為串列
print(list(range(1,10)))
print(list(range(1,10,2)))

for i in range(10):
    print(i)
    print('平方：',i*i)
    
total = 0
for i in range(1,5):
    total += i  # 把值累加
print('總和:',total)

total = 1
for i in range(1,4):
    total *= i  # 階層
print('總和:',total)

for i  in range(10,1,-1):
    print(i)
    
print('程式執行完畢')




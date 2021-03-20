# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:17:43 2021

@author: user
"""
#break 跳出此迴圈(僅用在迴圈中)
#continue 跳到下一個敘述，如1,2,3,4，在2設定continue後，變為1,3,4(僅用在迴圈中)


for a in range(2,10):
    for b in range(1,10):
        print (a,'*',b,'=',a*b,sep='',end='\t') # \t 代表 Tab鍵
    print()
    
for i in range(100):
    if i == 15:
        break
    if i % 3 == 0:
        continue

    print(i)
    print(i,'不是3的倍數')    
    
print('='*50)

for a in range(1,10):
    for b in range(1,10):
        print('a=',a,'b=',b)
        if a == 3:
            break
print('程式執行完畢')

for i in range(100):
    if i % 3 == 0:
        print(i)
        print(i,'不是3的倍數') 
    else :
        print(i)
        print(i,'是3的倍數') 








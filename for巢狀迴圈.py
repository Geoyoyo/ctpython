# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:22:36 2021

@author: user
"""

for i in range(1,5):
    print('i:',i)
    for a in range(1,4):
        print(a,end=',')
    print()
print('程式執行完畢')

print('='*50)

for i in range(1,5):
    for a in range(0,i):
        print(i,end='')
    print()
print('程式執行完畢')

print('='*50)

for i in range(1,5):
    for a in range(1,4):
        print(i,end='')
    print()
print('程式執行完畢')

print('='*50)

for i in range(5,0,-1):
    for a in range(0,i):
        print(i,end='')
    print()
print('程式執行完畢')
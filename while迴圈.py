# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:23:53 2021

@author: user
"""
i = 0
while i < 10: # while為布林值迴圈，每次判斷是否後再決定執行與否
    print(i)
    i += 1    # 計次值
print('程式執行完畢')

ans = 51
guess = 0
while ans != guess:
    guess = int(input('輸入1-100之間整數猜數'))
    if guess > ans:
        print('猜小一點')
    if guess < ans:
        print('猜大一點')
print('恭喜猜中')
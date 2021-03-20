# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:13:13 2021

@author: user
"""

"""
使用者猜亂數，1-100
1.須提示使用者要猜的區間，依據猜的答案做變化
2.猜五次沒猜中，要離開
"""

import random  #隨機亂數，要先import

ans = random.randint(1,100)
guess = 0
start = 1
end = 100
i = 0


while ans != guess :
    guess = int(input('輸入1-100之間整數猜數'))
    i += 1
    if guess == ans:
        print('恭喜你猜對了')
        break
    if guess > ans:
        print('答案介於',start,'-',guess -1,'之間')
        end = guess-1
    if guess < ans:
        print('答案介於',guess + 1,'-',end,'之間')
        start = guess+1
    if i == 5:
        print('你猜了五次，失敗!')
        break
print('遊戲結束')


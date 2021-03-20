# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:19:37 2021

@author: user
"""

"""
字串格式化

"""
money = 1000
name = 'John'
rate = 0.18

print('姓名:%s,存款:%d,利率:%f'%(name,money,rate)) 
# %s代表字串、%d代表整數、%f代表浮點數

print('姓名:%s,存款:%d,利率:%.2f'%(name,money,rate))
# %.2f代表小數點後兩位浮點數，數字代表小數點後幾位

print('金額:%10d,利率:%5.2f'%(money,rate))
# %10d代表整數前要補的空格(範例中1000有四碼，則須補六)
# %5.2f代表藥補的空格跟小數點後幾位

print('姓名:{},利率:{},金額{}'.format(name,rate,money))
# 大括號中數字為format中位置，沒有填就照順序

print('姓名:{0},利率:{1},金額{0}'.format(name,rate))
# 大括號中數字為format中位置

print('金錢:{0:,},利率:{1:.2f}'.format(money,rate))
print('利率:{1:5.2f},金額:{0:,}'.format(money,rate))
# {0:,}大括弧中冒號左邊為位置、右邊為格式(逗號代表千分位)

print('金錢:{0:,},利率:{1:0<8.2f}'.format(money,rate))
# {1:0<8.2f} 小於符號為右邊補零
print('金錢:{0:,},利率:{1:0>8.2f}'.format(money,rate))
# {1:0<8.2f} 大於符號為左邊補零

print('金錢:{0:,},利率:{1:*<8.2f}'.format(money,rate))
# {1:*<8.2f} 左右可補其他符號
print('金錢:{0:,},利率:{1:=>8.2f}'.format(money,rate))
# {1:=>8.2f} 左右可補其他符號



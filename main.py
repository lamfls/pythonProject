#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = 0
while n == 0:
    x = int(input("请输入一个数："))
    if x > 0:
        print(x, "的绝对值是", x)
    else:
        pre_x = x
        x = -x
        print(pre_x, "的绝对值是", x)
    n = int(input("是否继续进行下一次计算(0为继续计算,否则跳出计算)："))
    if n != 0:break

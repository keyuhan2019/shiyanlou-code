# -*- coding:utf-8 -*-

a = [[200, 50], [190, 50], [180, 50], [170, 50], [170, 60], [170, 70], [170, 80]]
x = [170, 60]
for i in a:
    if x[0] == i[0] and x[1] == i[1]:
        food_value = 0
        break
    else:
        food_value = 1
print(food_value)
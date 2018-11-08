import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('传入类型错误')
    if x >= 0:
        return x
    else:
        return -x


a = my_abs(1)
print(a)


# 默认参数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


b = move(1, 2, 3)
print(b)


def add(L=[]):
    L.append('END')
    return L


print(add())
print(add())
print(add())


def add_none(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_none())
print(add_none())
print(add_none())


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)


calc(1, 2)
list_1 = [1, 2, 3, 4]
calc(*list_1)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('jiexiaoqiang', 24, city='chongqing')
dict_1 = {'city': 'beijing', 'father': "father"}
person('xxl', 22, **dict_1)


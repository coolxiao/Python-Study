print('I\'m OK')
# list 集合
list = ['s1', 's2', 's3']
print(list)
list.insert(0, 's0')  # 插入元素
print(list)
list.pop()  # 删除末尾元素 加上index 就是删除第几个元素
list.pop(0)
print(list)
print(len(list))
# tuple 元祖 tuple一旦初始化就不能修改
classmates = (1, 2, 3)
print(classmates)
# t = (1)表示定义一个只有一个元素的元祖 而不是元素是1 ，t = (1,) 才是第一元素是1的元祖

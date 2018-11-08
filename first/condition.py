birth = input('请输入年纪：')
if int(birth) > 18:
    print('你成年了')
else:
    print('小学生 bye')
names = ['jiexiaoqiang', 'xxl', 'zhanglang']
for name in names:
    print(name)
sum = 0
index = 0
while index < 99:
    index = index + 1
    sum = sum + index
    print(sum)
print(sum)

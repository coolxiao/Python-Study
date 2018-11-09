import os

f = open('D:/123.txt', 'r')
print(f.read())
f.close()

with open('D:/123.txt', 'r') as f:
    print(f.read())

print(os.name)
print(os.path.abspath('.'))

from types import MethodType


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('xxl', 24)
print(s.name, s.age)


# 变量前面加__表示是私有的 外部不能访问
class Teacher(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


class School(object):
    pass


def set_name(self, name):
    self.name = name


sc = School()
sc.name = "清华"
print(sc.name)
sc.set_name = MethodType(set_name, sc)
sc.set_name("踩踩")
print(sc.name)

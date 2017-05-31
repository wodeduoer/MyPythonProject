""""
docstring
"""


def fib(n):
    a, b, c = 0, 1, 0
    while a < n:
        # print(a, end=' ')
        a, b = b, a + b
        c = c + 1
        print("a:", a, "b:", b, "c:", c)
    print("你好！！！")


# fib(100)


# 测试range函数
str1=range(1,9)
print(str1.index(3))  # value=3的index为2

str2=range(1,9,2)
print(str2.index(3))  # value=3的index为1


# sort dictionary
D = dict(name='xixibaishui', job='IT', gender='male', age=31)
for x in D.keys():
    print(x, '=>', D[x])

D3 = {}
x1 = [x for x in D]
x1.sort()  # 利用列表的排序对字典排序

for x3 in x1:
    print(x3, D.get(x3))
    D3.setdefault(x3, D.get(x3))

print(D3)

# 20170526:jinzi:利用x1.sort后可直接通过set赋值字典,而不必使用for循环:不对set赋值后是set而非字典
D4 = set(x1)
print(D4)  # set赋值后是set而非字典:{'age', 'gender', 'job', 'name'}

#  集合可以交/并/加/减
set1 = set(D.keys())
set2 = set1.copy()
set2.pop()
set2.pop()
set2.update(set(D.values()))
print('set1:=>', set1)
print('set2:=>', set2)

print(set1 & set2, set1 | set2)  # python不支持+
print(set1 - set2)
print(set2 - set1)

# enumerate枚举函数:字符串，列表，字典，set集合及元组
str1 = 'xixibaishui'
list1 = ['aa','bb','cc','dd','d','d','d']
dict1 = {'name': 'Xixibaishui', 'job': 'IT', 'gender': 'male', 'age': 31}  # 默认只枚举字典的key

# 字符串
print('字符串--------------------------')
for k,v in enumerate(str1):
    print(k,v)

# 列表
print('列表--------------------------')
for k,v in enumerate(list1):
    print(k,v)

# 字典(默认只枚举key)
print('字典--------------------------')
for k,v in enumerate(dict1):
    print(k,v)

for k,v in enumerate(dict1.values()):
    print(k,v)

# set集合
print('set集合--------------------------')
for k,v in enumerate(set(str1)):
    print(k,v)
for k,v in enumerate(set(list1)):
    print(k,v)

# 元组
print('元组--------------------------')
for k,v in enumerate(tuple(str1)):
    print(k,v)

for k,v in enumerate(tuple(list1)):
    print(k,v)

# 20170529:十进制,八进制与十六进制
int('0100'),int('0100',8),int('0100',16)  # int可把字符串转化为指定进制的数字

"%o %x %X" % (64,64,255)  # 十进制数字转化为指定进制
# 小数类型 from decimal import Decimal


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
str1 = range(1, 9)
print(str1.index(3))  # value=3的index为2

str2 = range(1, 9, 2)
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
list1 = ['aa', 'bb', 'cc', 'dd', 'd', 'd', 'd']
dict1 = {'name': 'Xixibaishui', 'job': 'IT', 'gender': 'male', 'age': 31}  # 默认只枚举字典的key

# 字符串
print('字符串--------------------------')
for k, v in enumerate(str1):
    print(k, v)

# 列表
print('列表--------------------------')
for k, v in enumerate(list1):
    print(k, v)

# 字典(默认只枚举key)
print('字典--------------------------')
for k, v in enumerate(dict1):
    print(k, v)

for k, v in enumerate(dict1.values()):
    print(k, v)

# set集合
print('set集合--------------------------')
for k, v in enumerate(set(str1)):
    print(k, v)
for k, v in enumerate(set(list1)):
    print(k, v)

# 元组
print('元组--------------------------')
for k, v in enumerate(tuple(str1)):
    print(k, v)

for k, v in enumerate(tuple(list1)):
    print(k, v)

# 20170529:十进制,八进制与十六进制
int('0100'), int('0100', 8), int('0100', 16)  # int可把字符串转化为指定进制的数字

print("%o %x %X" % (64, 64, 255))  # 十进制数字转化为指定进制
# 小数类型 from decimal import Decimal

# 20170531
# 类型属于以对象而非变量
# 共享引用和在原处修改:列表/字典等在原处修改不仅仅修改本身变量，其共享引用的变量也会被修改
# 如何破解：切片/copy/import copy


# 字符串
# 二进制转换为十进制1
B = '1101'
I = 0
while B:
    # I = I * 2 + (ord(B[0]) - ord('0'))
    I = I * 2 + int(B[0])
    print(I, B)
    B = B[1:]
print(I, B)

# 二进制转换为十进制2
B2 = '1101'
I1 = 0
I2 = I1
while B2:
    I2 = I2 + int(B2[-1]) * (2 ** I1)
    print(I2)
    I1 += 1
    print(I1)
    B2 = B2[:-1]
    print(B2)
print(I1, I2, B2)

# 20170601:jinzi:元组:本身不含方法，可通过列表对其排序
t1 = 'efg', 'cd', 'ab'
tmp = list(t1)
tmp.sort()
t1 = tuple(tmp)
print(t1)

# 元组的列表解析list comprehension
t2 = (1, 4, 7, 2, 5, 8)
list2 = [x ** 2 + x for x in t2]
d3 = {x: x ** 2 + x for x in t2}
t3 = (x ** 2 + x for x in t2)
print('列表====>', list2)
print('字典====>', d3)
print('元组====>', t3)
# 列表====> [2, 20, 56, 6, 30, 72]
# 字典====> {1: 2, 4: 20, 7: 56, 2: 6, 5: 30, 8: 72}
# 元组====> <generator object <genexpr> at 0x00000148DA6C6938>

# 为何元组未成功解析？经查询，原因为：generator comprehension
t4 = tuple(x ** 2 + x for x in t2)  # 列表解析的结果默认都是列表，所以需使用tuple转换之
print('元组2====>', t4)

"""
列表解析是名副其实的序列操作--它们总会创建新的列表，但也可以用于遍历包括元组、字符串以及其他列表在内的任何序列对象。
列表解析甚至可以用在某些实际并非储存的序列之上--任何可遍历的对象都可以，包括可自动逐行读取的文件
"""

# 交互
while True:
    reply = input('Enter whatever you want:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('What you enter [', reply, ' ] is not digit,please reEnter')
    else:
        print(int(reply) ** 2)
print('Bye')

# 20170602 循环
# 同一个结果的不同循环形式
# 1:while
x = 'spam'
while x:
    print('while=====>', x)
    x = x[1:]

# 2 for
x = 'spam'
for y in range(4):
    print('for=====>', x[y:])

# 根据输入的数字判断是否是质数
list3 = []

while True:
    is_prime = input('Enter your num,so we can judge whether it\'s a prime\n')
    if not is_prime.isdigit():
        print('What you Enter is not a digit,reenter please!')
    else:
        break

xx = int(is_prime) // 2
while xx > 1:
    if int(is_prime) % xx == 0:
        print(is_prime, 'has the factor ', xx)
        list3.append(xx)
    xx -= 1

if len(list3) > 0:
    print(is_prime, 'has factors as follows:', list3)
else:
    print(is_prime, ' is a prime')

# 注意while中的else:除非while与else间含break，否则无论while执行几遍(即使0遍)，else部分也会执行


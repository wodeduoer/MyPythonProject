## lambda,filter,map,reduce等匿名函数

#1：filter()为已知的序列的每个元素调用给定的布尔函数，调用中，返回值为非零的元素将被添加至一个列表中
#2：map()将函数调用映射到每个序列的对应元素上并返回一个含有所有返回值的列表
#3：reduce函数会对参数序列中元素进行累积.在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里。用的话要先引入
from functools import reduce

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print(*filter(lambda x: x % 3 ==0,foo))
print(list(filter(lambda x: x % 3 ==0,foo)))
print(*map(lambda x: x * 2+3,foo))
print(reduce(lambda x, y: x + y,foo))

#测试先通过filter()过滤，然后映射或累积:
#print(reduce(filter(lambda x: x % 3 ==0,foo), foo))  ##TypeError: 'filter' object is not callable


def func1():
    list4 = []
    for i in range(5):
        list4.append(lambda x:i ** x)
    return list4

ff = func1()    # 赋值给ff,同时传值ff.x=2
for i in range(5):
    print(i, '==>', ff[i](2))


def func2():
    list4 = []
    for i in range(5):
        list4.append(lambda x,i=i:i ** x)
    return list4

ff2 = func2()    # 赋值给ff,同时传值ff.x=2
for i in range(5):
    print(i, '==>', ff2[i](2))

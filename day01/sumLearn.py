##################################面向对象#####################

# ####公有和私有 name mangling  改编,假私有
# class Bird:
#     num = 0
#     __age = 0;
#     def __init__(self):
#         self.num += 1
#         self.name = 'bird'
#
#     def getA(self):
#         return self.name
#
#     def getAge(self):
#         return self.__age
# b1 = Bird()
# # print(b1.getAge())
# print(b1._Bird__age)

#%%%%%%多态



# class Bird:
#     num = 0
#
#     def __init__(self):
#         self.num += 1
#         self.name = 'bird'
#
#     def getA(self):
#         return self.name
#
#
# b1 = Bird()
# b2 = Bird()
# print(Bird.num, b2.name, b1.num, b1.name)
#￥￥￥￥继承
# class Bird(list):
#     num = 0
#
#     def __init__(self):
#         self.num += 1
#         self.name = 'bird'
#
#     def getA(self):
#         return self.name
#
#
# b1 = Bird()
#
# b2 = Bird()
# b2.append(1)
# print(b2 )


# ################图形############################
# import tkinter as tk
# t = tk.Tk()
# L = tk.Label(t,text = 'label')
#
# L.pack()
# t.mainloop()

# import easygui as g #推荐
# # from easygui import *  #导入全部的
# # g.msgbox('a')
# g.textbox()



#######################with，else语句#################################
###with
# try: #省略finally，因为打开错误的话finally有可能因为没有打开文件，而不能关闭
#     with ('E:/aa.txt','w') as f:
#         for ec in f:
#             print(ec)
# except OSError as r:
#     print('错误',r)


# try:
#     f = open('E:/aa.txt','w')
#     for ec in f:
#         print(ec)
# except OSError as r:
#     print('错误',r)
# finally:
#     f.close()


####else
# 要么，要么
# for while： else 干完执行，干完不执行
# 没有问题就干

# try:
#     print(int('5'))
# except:
#     print('yichang ')
# else:
#     print('额外的else部分')

# for i in range(10):
#     print('i=-',i)
# else:
#     print('@@@@@wanle')

# for i in range(10):
#     print('i=-',i)
#     break #加了就不执行else
# else:
#     print('@@@@@wanle')

#########异常处理try: except exception:
# raise自己引发异常
# raise ZeroDivisionError
# raise TypeError
# raise ZeroDivisionError('出书为零')

###直接except：不推荐
# try:##直接捕获到第一个异常，剩下的不会被处理
#     f = open('ss')
#     a = 5 / 0
#     f.close()
# except OSError as r2:
#     print('打不开',r2)
# except ZeroDivisionError as r1:
#     print('sss',r1)
# finally:
#     f.close() #防止前面执行的操作没有被写入到文件里面
#     print('over')

# try:##直接捕获到第一个异常，剩下的不会被处理
#     f = open('ss')
#     a = 5 / 0
#     f.close()
# except (OSError,TypeError,ZeroDivisionError):
#     print('打不开')



# try:
#     f = open('ss')
# except Exception :
#     print('打不开')
# else:
#     print('over')

#####################文件
###写入对象等pickle，unpickle
# import pickle
#
# # #读取
# # pickle_read = open('e:/object.pkl','rb')
# # l2 = pickle.load(pickle_read)
# # print(l2)
# #
# pr = open('e:/object.pkl', 'rb')
# ol = pickle.load(pr)
# ol1 = pickle.load(pr)
# print(ol)
# print(ol1)
#
#
# pr.close()

# ######写入
# l1 = [1, 2, 3, 4, 5, 'a', [11, 33, 44]]
# pickle_file = open('e:/object.pkl', 'wb')
# pickle.dump(l1, pickle_file)
# pickle.dump(['i','love'],pickle_file)
# pickle_file.close()
#
# # #文件读每一行
# # f = open(r'e:\file.txt')
# l1 = []
# # for r1 in f:
# #    l1.append(r1)
# # print(l1)
#
# for r1 in f:
#    print(r1)

##########集合,无序，没有重复,add,remove,

# s1 = {1, 2, 3, 4, 5}  # 没有体现映射关系就是集合
# s2 = set([1, 2, 3, 3, 3, 3, 3])
# s3 = set('abc')
# print(s2, s3)
# print(type(s1))
#
# ###不可变集合frozen
# s4 = frozenset(s1)
# print(s4)
#

# ###################### 字典=关系数组=哈希表
# # in , not in查找
# d1 = {'a': 1, 'b': 2}
# print(d1.get(2))#'none
# d1.setdefault('c',3)
# print(d1)
# d2 = {'a':4,'b':5}
# d1.update(d2)
# print(d1)

# d1.popitem()#随机弹出

# # values,keys,items
# d2 = dict.fromkeys(range(32),'zan')
# for v in d2.keys():
#     print(v)
# for v in d2.values():
#     print(v)
# for it in d2.items():
#     print(it)

# d2 = {}
# d2 = d2.fromkeys((1, 2, 3), 'a')
# d3 = dict.fromkeys((1, 2, 3))
# # d3 = dict.fromkeys((1, 2, 3),('a','b','c'))#这个不行
# print(d2, d3)

# d1 = {'a':1,'b':2}
# tp = d1.items()
# d2 = dict([('a', 1), ('b', 2)])
# d3 = dict((('a', 1), ('b', 2)))
# d4 = dict(a='one',b='two')#a不能用数字
# print(d3)
# print(type(d3))

###递归

# def fatorial(n):#阶乘
#     if n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
# print(fatorial(3))


# BIF filter /重要，可结合匿名函数
# # map 映射
# print(list(map(lambda x: x * 2, range(10))))

# filer(f.B)返回B中经过f处理为true的部分

# lis = filter(lambda x: True if x % 2 == 0 else False, [1,2,3,4,5,6,7])
# print(list(lis))

###################函数


# # 匿名函数
# g = lambda x, y: x * y m
# print(g(2, 3))

# 内嵌函数和闭包
# def f1():
#     print('fun1')
#     def f2():
#         print('f2')
#     f2()
# f1()

# 闭包
# #返回多个值
# def m3():####
#     return 1,2,3
# print(list(m3()))

# 闭包
# def fx(a):
#     def fy(b):
#         return a + b
#
#     return fy
#
#
# r = fx(1)
# print(r(2))
# print(fx(1)(2))

# =========================python 3 增加 nonlocal=============

# def fx(a):
#     def fy(b):
#         nonlocal a
#         a = a + b
#         return a
#
#     return fy
#
#
# r = fx(2)
# print(r(2))
# print(fx(1)(2))


# 可变参数-收集参数
# def mp2(*p):
#     '多重类型，前面的参数要用关键字形式赋值，建议附上初始值'
#     print(len(p))
#     print(p)
#     print('==================')
#     for te in p:
#         print(te)
#         # print(te, end='  ')
#
#
# # mp2([1, 2, 3, 4, 5, 'aaa'])
# mp2(1, 2, 3, 4, 5, 'aaa')

# 函数文档
# def mp():
#     '函数文档name猜都是'
#     print("a test")
# # mp()
# print(mp.__doc__)


# #字符串格式化
# s1 = 'a{0}--{a}=1';
# s2 = s1.format('0',a='555')
# print(s2)
# print('%c %c'% (97,98))
# s3 = '%c %c'% (97,98)
# print(s3)
#
#


# 014字符串操作, tuple ,list,str 属于sequence
# s1 = 'abcdeddDfg555a'
# print('c' in s1)
# print(s1, s1.capitalize())  # 首字母大写
# print('sSfDddFf'.casefold())
# print(s1.center(15))
# s2 = s1.center(30,"1")
# print(s1.center(100,'2'))
# print(s1.count('dd'))
# print(s1.endswith('g'))
# print(s1,'\n', s1.expandtabs())

# print(s1.isalnum())

# s2 = '1'
# print(s2.join('aaaaaaaaa'))
# print(s1.partition('de') )

# print(s1.split('d'))

# s3 = '          a b c 1 2 3           '
# print(s3.strip())
# print(s1.strip('a'))

# s4 = 'aBc'
# print(s4.swapcase())
#####################z重点
# # print(s1.translate(str.maketrans('a','z')))
# s5 = 'a b c'
# print(s5.zfill(1))

# 元祖#tuple操作
# t1 = (1, 2, 3, 4)
# t2 = 1, 2, 3, 4
# t3 = 1,
# print(type(t1), type(t2), type(t2))
# print(8 * t3)

# t1 = t1[:1] + (999,) + t1[1:]# 添加元素
# print(t1)
# del t1
# del t1(1)#不能删除


# # 列表操作
# l1 = [1, 2, 3]
# l2 = [4, 1, 1]
# # print(l1 > l2)  # 之比较了一个1和1
#
# print(l1 + l2)
# print(l1 * 2)
#
# print(1 not in l1)
# print(1 in l1)
# l3 = [9, l2]
# print(l3)
#
# print(1 in l3[1])#在第二个元素里面
# print(l3[1][2])

# print(l2.count(1))
# print(l2.index(1,2,3))
# l2.reverse()
# print(l2)

# l2.sort()
# print(l2)
# l2.sort(reverse=True)
# print(l2)

# #z=类似于指针
# l3 = l1
# l1.append(999)
# print(l3)

# l3 = l1.copy()
# l1.append(999)
# print(l3)

# #切片
# lis = [0,1,2,3,4,5,6,7,8,9]
# print(lis[0:10:2])

# # @列表删除元素
# lis = [1, 2]
# # lis.remove(1)
# # del lis[0]
# nn =lis.pop(0)
# print(nn,lis)

# print(lis)

# #列表扩展
# lis = [1, 2]
# lis.append(3)
# lis.extend([4,5])
# lis.insert(0,0)#顺序索引都是从0开始
# print(lis)


# #断言
# assert 3 > 4#正确没有任何提示
# print('false')#不会执行到这一句

# #条件表达式
# small = 5 if 6> 5 else 6
# print(small)


# ## 随机数范围测试
# import random as rd
# rdnum = rd.randint(1, 3)
# print(rdnum)


# print("Let\' go")
# print("c:\\now")
# str1 = "c:\\now"
# print(str1)
#
# print(r'c:\a\b\c')  # 原始字符串
#
# print("""a
# b
# c
# d""")  # 长字符串

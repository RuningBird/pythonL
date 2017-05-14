###################函数
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

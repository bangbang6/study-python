# print(r'''\n''')
# #r表示原始字符串,就不会转义以及原始字符串
#
# #字符串操作
# print('sada'[1:3]) #3不取
# print('sada'[1:-1])
# print('sada'[1:])
#
#
# print(type((1,2,'asc',[1,2])))#tuple 元祖类型 str list 一致操作
#
# print([1,2,3]+[4,5])
#
# print('a' in 'abc')
#
# print(max(['b','a']))
#
# print(ord('a'))
#
# print(type({1,2}))  #字典也是一种集合 集合主要是 - & | 操作
# # 列表 [] 元祖 () 字符串 ''
# # 集合{} 字典 {}
# #字典是key value key 必须是不可变的类型 比如数字 元祖可以 字符串 1和'1'不是一个同一个key 集合 列表 tuple不可以 list及以后是引用类型
#
# print(type({'Q':'一技能','w':'二技能'}['w'])) #通过key来访问
# print(type({[1,2]:'一技能','1':'二技能'}[(1,2)])) #通过key来访问


a = 1
b=a
print(id(a))#地址

a = (1,2,3,[1])
a[3][0]=2
print(a)#这里改变额是list

print(2**3)#指数

print({3} < {2})

#逻辑运算符 and or 不是|| && 非是not 不是!
#成员预算福 in not in 字典的是针对key
print('a' in {'a':11})

#身份运算符 is  不是 == 内存地址一样才想同

a = (1,2,3)
b = (1,2,3)
print(int(b is a) ) #引用类型就不行 因为地址不一样 如果是基础类型 那么 b is a True
# isinstance 判断类型 isinstance(a,int)
print(isinstance(a,(list,tuple)))#元祖里随便一个都可以
#print('aaa'+1) 不行

print(False or (True))

AC = 1 #常量最好大写 pylint 检查错误下划线






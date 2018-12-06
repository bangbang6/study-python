def add(x,y):
    return x + y
f = lambda x,y : x + y #只能写简单的语句 返回不用写return #匿名函数 即lambda 表达式 即语句块只能是简单表达式
print(f(1,2))

#三元表达式 x if x>y else y

#lamdba表达式 很容易用到三元表达式
#sub那里传的函数简单的话就可以用value>什么什么来写
f = lambda x,y : x + y if x > y else y - x #只能写简单的语句 返回不用写return #匿名函数 即lambda 表达式 即语句块只能是简单表达式
print(f(1,2))

list1 = [1,2,3,4]
def squre(x):
    return x * x
print(list(map(squre,list1)))
list2 = [1,2,3,4,5]  #个数不等也没事 就是运行相同位置的
#结合lamble 表达式
print(list(map(lambda x,y :x * x + y,list1,list2)))


from functools import reduce

list_x = [1,2,3,4]

print(reduce(lambda x,y:x+y,list_x,10))

print(list(filter(lambda x: True if x ==1 else False,list_x)))

list2 = ['a','B','c','D']
print(list(filter(lambda x : ord(x) > 50 and ord(x) < 90,list2)))


#decorator
import time
def decorator(fuc):
    def wrapper(*args,**kw):
        print(time.time())
        print(args) #args是元祖
        print('kw',kw)
        fuc(*args,**kw)
    return wrapper
''' def f1(x):
    print(x)                    #装饰器
f = decorator(f1)
f(1) '''

# **kw 表示传入字典类型 任何参数列表都可 kw是字典 **kw是关键字参数 *args 是多个普通参数 args是元祖
def f2(x,y,**kw):
    print(x,y,kw)
f2 = decorator(f2)
f2(4,5,a=1,b=2) #关键字参数
#ppython 为装饰器提供啦语法糖 @  就是不用再用f 直接用f1 不改变调用方式 直接f1 就能增加新功能 这才是装饰器作用 不用改大部分代码
#就是加个2decorator 就能加功能 无敌
#其实就算是把 f1 = decarator(f1) 重赋值 看f2 即可
#作用 其实就是提出公共代码 这样子别人直接使用到函数上就行
@decorator
def f1(x):
    print(x)                    #装饰器

f1(1)

#解决可变参数的问题 假如有两个函数参数个数不一样 就必须用可变参数 把参数写成 *args



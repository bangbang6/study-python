#函数就是让别人不用看里面具体实现 直接用即可
#如果没写return 那么默认返回None 是一种基本类型
''' import sys  
sys.setrecursionlimit(500) '''
#设置最大的递归常熟
''' def add(x,y):
    return x + y
def printx(x):
    print(x)
   
printx(add(1,2))
a = input()
print('a is',a) '''

#返回多个值 自动变元祖
def m(x, y):
    return x, y
#即可 返回的就是元祖
print(m(1,2))
#获取函数返回值是元祖最好不要用[0]等等来取值
#一般这样子
x1, x2 = m(1,2)
print(x1)
#这样子有实际意义  这样子可以发现python会自动给a,b这种东西加上()变成元祖
#so 交换数字 直接 x,y = y,x
#序列解包
x,y,z = 1,2,3
#直接赋值成功 应为会自动相当于加() 这样子代码一下子少啦很多
d = x,y,z
print(type(list(d)))    
#序列解包 不能像js一样只取几个
a,b,c = d
#默认参数必须放在最后面
#可以通过关键字实参来调用函数 和默认参数一起使用 很简单
def test():
    return
print(test())

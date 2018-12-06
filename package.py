#包里必须包含__init__.py 他的名字是报名
#import c7  as m  不能直接道路变量 只能道路模块 as能简化后面的使用的路径长度
#c7.a 使用c7模块的a

#from c7 import a 可以直接引入变量/函数 会执行c7的代码
# from t import c7 引入模块也可以 后面通过.来用变量
# c7.a   
''' from c7 import * #把模块的东西 __all__搞进来
print(a)
print(b) '''

#一般会用下面的映入

''' from c7 import a,b
print(a)
c = 1
import sys
print(sys.path) '''


''' import t
print(t.sys.path) '''
#如果导入包来导入一些系统模块那么需要通过包名.模块名来使用

#模块不能循环引入 比如1引入2 2映入3 3映入1 这样循环啦

print(1,end=('\n'))

#转字符串
A = 1.23456
print(type(str(A)[0:3:2]),end='\n')

from object import Student #这种导入方法最好

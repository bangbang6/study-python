import re
'''1. // \w不包括& \n 空格 但是包括_下划线 相当于a[A-Za-z0-9_]f \d也能匹配.
// \s 匹配   \n 空格 \s 等等 但是没 & 
. 匹配除啦换行符\n以外的字符
 '''
 



''' //2.{n}里面填的数字表示连续几个匹配  {3,6}表示有6个连在一起就6个 最少3个 (越大越优先) 
//为什么越大越优先 因为贪婪策略 他会一直往后找符合条件的 直到遇到不符合的字符 所以会停 '''

''' 3.加上问号就是非贪婪模式 匹配到满足的条件就结束而不是继续查找下一个看是否符合'''


''' 4.数量词 *表示匹配前面的0次或者多次 就可以不用{}指定数字 +一次或者无限多次 ?表示匹配0次或者一次 '''



''' //5.重要: ? 有两个作用 直接更在字符后面的是表示0-1 已经有啦数量词在加?表示非贪婪模式 所以  [1]??表示0-1匹配非贪婪 即0 一个都没有匹配 '''


''' 6.边界匹配  防止\d{4,8} qq9位也能配出前8位的bug ^\d{4,8}$即可'''

''' //7.()表示组的概念 (python){3,6}表示python重复3-6次 ()对应[] [] 表一个字符 ()表字符组 '''

''' 8.模式 re.I 忽略大小写 可以接受很多种 '''

''' 9.re.S表示.可以匹配换行符 '''
a = 'abc,acc,adc,aec,afc,ahc,python'
r = re.findall('[A-Za-z0-9_]{3,6}?',a)
print(r) #返回列表
#print('python' in a)

b = 'pythonnnnn'
#去重n
#只留1个
r = re.findall('python?',a)
print(r) 
#一个不留
r = re.findall('python??',a) #因为非贪婪模式所以取0
print(r) 
#同理你诺想要1-2 那么{1-2}?表示1 不加?表示2

c='pythonpythonpythonapython'

r = re.findall('((python)+)',c,re.I|re.S) #search 只返回第一个符合的 而且有group方法 
print(r)


#re.sub 替换操作 string.replace

#print(re.sub('abc','Go',a,0)) #0表示全部匹配 1表示只匹配第一个

''' b = a.replace('abc','go')
print(b) '''

#re.sub的高级用法 第二个参数可以是函数

def convert(value): #group(0)是匹配出来的字符串 group(1)是第一个组匹配的东西依次类推
    print(value.span())#value 是对象  <_sre.SRE_Match object; span=(0, 3), match='abc'> span是源字符串的位置 给的是元祖(0,3)即0,1,2 span()返回span表示的东西
    return 'function'
print(re.sub('abc',convert,a,0)) #匹配到第一个结果会放到value里 函数返回的结果是新的字符串替换前面的字符串

#设计方式 我们可以自己定义一个函数 但是其中一部分的东西我们写不了  要给用户自己具体实现 这时候我们就可以开放一个函数参数作为借口 我们把他当参数 我们给他传参数
 

r = re.search('((python)+)',c)
print(r.groups()[0])

#r = re.match() 这个必须开头就满足正则
origin = 0
def go(step):
    #nonlocal origin 闭包才用
    global origin
    origin = origin + step
    return origin
print(go(3))
print(go(4))

origin = 0  #把全局变量少啦    
def factory(y):
    def go(step):
        nonlocal y 
        
        new_pos = y + step
        y = new_pos
        return new_pos
    return go
x = factory(origin)
print(x(3))
print(x(4))
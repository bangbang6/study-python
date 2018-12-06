''' a = [1]
b = [1]
for target_list in a:
    pass
else:
    pass '''
# for 没有什么i++ 只有in 那么只有用range函数 range(0,10)不包括10 range(0,10,5)打出 0 5
#print(type(range(10))) #range也是一种类型

#for 语句如果通过break弄断的 那么不会走else语句 其他的都会 反正走到啦最后就会else语句

''' for target_list in a:
    for i in b:
        if i == 1:
            break '''
        

#那个只能跳过内部循环所以还是会执行后面的列表 以及执行else语句 因为外部的是执行完辣的

#range

for i in range (10,-1,-2):
    print(i)
#range后面的就是走的趋势 ,关键看第3个参数

a = (1,2,3,4,5,6,7)

b = a[0:len(a):2]
print(b) 

''' class classname(object):
    pass '''

    
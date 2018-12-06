from enum import Enum,unique
@unique
class VIP(Enum):
    YELLOW=1 #黄砖 当做1存到数据库
    Green=2
    BLUE = 'str'
   # YELLOW_ALIES = 1 #不会再循环的时候打错来
print(VIP.YELLOW.value)
#print(type(VIP.YELLOW_ALIES)) #但是有 is 操作符
#转枚举类型

a = 1
print(VIP(a))



''' for v in VIP:
    print(v) 
for v in VIP.__members__:#会打印出所有返回元祖
    print(v) '''


#列表推导式
a = [1,2,3]
print([i*i for i in a if i > 1])
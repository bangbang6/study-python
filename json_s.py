#json 跨语言传数据 对应不同语言的不同数据结构
import json
a = '{"name":1, "age":2}'
print((json.loads(a))['name'])
print(type(json.loads(a))) #相当于json.parse()

#json.dumps()#相当于#json.strimpy()
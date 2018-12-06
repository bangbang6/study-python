class Test():
    def __len__(self):
        return 8
    def __bool__(self):
        return True  #这个更重要
test = Test()
print(Test.__dict__)
print(bool(test))
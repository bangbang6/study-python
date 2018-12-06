class Student():#括号里面是继承的类
    #__为首的(结尾不能是__)变量或者函数就是私有的 不能在外部直接用只能类内部用 出啦__init__ 
    #还有些私有变量就是不想给外部直接调用而是给内部方法用的值 外面只用方法来该值 如score变量
    #类变量 类似静态变量   
    name = 'default'
    age = 0
    __sum = 1
#在类里面的函数必须加入self形式参数 self就是当前   this
    def __init__(self,name,age):
        #实例变量
        self.name = name
        self.age = age
        self.__score = 0 #会把名字变成 _Student__score 但是在外面可以用 所以其实不存在私有变量 java好点
        pass
    #构造函数
    def __printAge(self): #这个东西隐藏到Student里面去啦 还是_Student__printAge
        print(Student.name)
        print(self.name)
        print(self.__class__ == Student)
        Student.name = 'asd' #只能通过Student来用类变量 不能直接name 这个和模块不同
    #类方法 没self那么访问不了实例变量 一般只用类方法不用静态方法
    def printScre(self,score):
        #为什么用方法比直接还变量好呢 因为可以加判断 这样子就防止外部改层负分
        if score < 0:
           print('不能小于0')
           return
        self.score  = score
    @classmethod #装饰器
    def printSum(cls):
        print(cls.name)
    @staticmethod
    def add(x,y):#静态方法 不传入cls 直接用Student来访问类变量
        pass
student = Student('bang',12) #自动调用构造函数
#student.printAge() #自动传self
Student.printSum()
#student.__score = 1  这里相当于添加啦实例变量 所以下面即使调用这个也是会有效的 和私有不私有的无关 在类里面的__定义才是私有的 外面定义的不是私有的
print(student._Student__score)
print(type(student))
print(Student.__dict__)
print(student.__dict__) ##打印对象
#print(Student.sum) 会报错 直接没当他有这个属性 但是会沿着链网上找除非都没有就报错




#继承 只有实例变量会要自己写其他直接继承
#1.类变量和方法直接继承可以使用 构造函数没写的话 没继承的话是 参数是空 继承的话就是和父类的一样
#2.可以多个父类
#3.Human.__init__(name,age)来用父类的方法 类似super 但是可与不在首行 注意 :这里调用方法的时候必须自己传self 相当于把他看成一个普通方法 以前都是python自动传的 因为之前是python自动帮我们调用init
#接上 因为init是实例方法 包括printage 如果你是实例调用那么不需要写self 因为self就是前面的对象 但是你通过类名来调用 本身就是不合法,你把它当普通函数,那么用类你不知道self是什么所以不行 除非传一个实例student进去或者self
#4.所以3那种方法不好 所以我们现在知道init classmethod其实要传 但是调用时自动帮你传 除非你调用者不是规范的
# 5.采用super(Student,self).__init__(age,name)来 这样就不用human 就算 父类改啦这句代码也不要该 super(Student,self) 相当于找到human实例
#6.所以 suoer(Student,self))可以调用父类所有实例方法 但是其实继承啦,就可以直接调用 但是子类有同名方法就会覆盖,所以这时候还想要父类的方法就必须用这个方法来实现
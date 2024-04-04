x=5
y=10
print(x+y) 

def say_hi(name):
    print(f"Hello whats your {name}")
say_hi('John')
x='awesome'
def  my_func(c):
    print("python is " + c)
my_func('i love ')


t= 1
b= 39393939
c= -344
print(type(t))
print(type(b))
print(type(c))

a='''lorem uuuu'''
print(a)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # Corrected method name '__init__'

e = Student('jon', 'doe')
e.printname()
















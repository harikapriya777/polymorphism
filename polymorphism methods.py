#operator overriding
'''class a():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class b():
    def __init__(self,b):
        self.b=b
x=a(3)
y=b(4)
print(x+y)'''


#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
x=new()
x.sum()
x.sum(3,4,5)
x.sum(6,2)'''
        

'''class new():
    def sum(self,a=2,b=3,c=4):
        if a==2 and b==3 and c==4:
            print("the sum is",a+b+c)
        elif a==5 and b==6:
            print("the product is",a*b)
        else:
            print("program ends")
x=new()
x.sum()
x.sum(5,6,7)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("Dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#task
'''class Vehicle():
    def speak(self):
        print("Vehicals can beep")
class camera():
    def speak(self):
        print("camera clicks")
a=Vehicle()
b=camera()
a.speak()
b.speak()'''


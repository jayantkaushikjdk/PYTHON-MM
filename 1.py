
#1to calcuate the average of 5 integers
a=eval(input("enter 1 no.:"))
b=eval(input("enter 2 no.:"))
c=eval(input("enter 3 no.:"))
d=eval(input("enter 4 no.:"))
e=eval(input("enter 5 no.:"))
avg=(a+b+c+d+e)/5
print("avg:",avg)




#2to calculate simple interest
p=eval(input("enter priniple amount"))
r=eval(input("enter rate"))
t=eval(input("enter time"))
s=(p*r*t)/100
print("simple interest=",s)





#3
import math
a=eval(input("enter radius: "))
c=math.pi*a*a
print("area of circle: %.1g"%c)




#4
import math
a=eval(input("enter radius:"))
b=eval(input("enter height:"))
c=math.pi*a*a*b
print("volume of cylinder %.2f"%c)
r=12
r="hello"
print(id(r))
list1=[1,'abc',4,5,6,'rfd']
print(list1)
print(id(list1))
print(type(list1))









#5

a='abc'
b='djf'
c='cjd'
d='ehd'
print(a,b,c,d,sep='h')
x=a*5
print(x,sep='3')



#6
a,b=22,32
c,d=33,56


print(a>b and c<d)
print(a>b or c<d)
print(not(a>b and c<d))
print(not(a>b or c<d))
print(a!=b and c==d)



#7 membership operators

s=" hi I like to eat some stuff while watching movie"
print('eat' in s)
print('light' not in s)
print('like' not in s)




#8
i=input("enter str 1 :")
d=input("enter str 2 :")
x=d in i
print(d,"in",i ,'d' in 'i')

             
#9
a=17
b=24
print(a&b)

             
#10

a=17
b=24
print(a|b)




#11
a=17
b=24
print(a^b)




#12
a=12
b=34
c=a
a=b
b=c
print(a,b)



#13
dj=lambda x  :x*2
for i in range (1,100):
    print(dj(i))
#14
    add=lambda a,b: (a+b)
sub=lambda a,b: (a-b)
mul=lambda a,b: (a*b)
din=lambda a,b: (a//b)
pow=lambda a,b: (a**b)
while True:
    ch=input('enter')
    if ch=="+":
        a,b=eval(input())
        print(add(a,b))
    elif ch=="-":
        a,b=eval(input())
        print(sub(a,b))
    elif ch=="*":
        a,b=eval(input())
        print(mul(a,b))
    elif ch=="//":
        a,b=eval(input())
        print(din(a,b))
    elif ch=="**":
        a,b=eval(input())
        print(pow(a,b))
    elif ch==".":
        break
    else:
        print("invalid")

#factoriial  to 10
def series(n):
    for i in range (1,n+1):
        print(i**2)
n=eval(input())
series(n)



'''def double(n):
    return n*2
l=[4,56,43,56,7323,4566,333]
ln=map(double,l)
print(list(ln))'''


'''def sal(n):
    return n+n*1
l=[8434,3423,5645,65856,1234,453,12341234]
ln=map(sal,l)
print(list(ln))'''


'''rad=[23,45,234,234,234]
def area(r):
    return 3.14*r*r
ar=map(area,rad)
print(list(ar))'''


'''l=['dfasd','ere','efs','dfdas','fhsf']
ln=map(lambda n: len(n),l)'''

l1h=[23,44,33,55,66]
l2r=[32,43,54,65,76]
def vol(n,r):
    return 3.14*r*r*n
x=map(vol,l1h,l2r)
print(list(x))


'''def add(a,b):
    hoi
em chestunaro


    return a+b
print(add.__doc__)
print(add(2,4))'''


'''def arg(**v):
    for x,y in v.items():
        print(x,"=",y)

arg(a=4,f=4)
arg(ad="erwrt",h="wegbthnyjm_")'''


'''s="this is my first String"
print(s)
print(s[11])
print(s[-6])'''


'''str="How are you?"
print(str[4:7:1])
print(str[2:5])
print(str[8:11:1])
print(str[10:7:-1])
print(str[8::1])
print(str[-1:00:-1]) '''
'''a=input()
b=input()

print(a[:2])
print(b[-2:])'''
'''s=input()
print(s[1:-1])'''
'''s=input()
print(s[-1]+s[1:-1]+s[0])'''

  


a="code"
b="tantra"
print(a+b+b+a)




a=input()
n=int(input())
if n>len(a) or n<0:
    print("invalid")
else:
    print(a[:n]+a[n+1:])





a=input()
b=input()
if len(a)>1 and len(b)>1:
    print(a[1:]+b[1:])
else:
    print("null")




a=input()
print(a*4)
print(a[::-1]*3)




a=input()
if len(a)>=3:
    print(a[0:3]*3)
else:
    print(a)




a=input()
n=int(input())
print(a*n)


a=input()
n=int(input())
if n<0 or n>len(a):
    print("n shld be positive")
else:
    print(a[0:n+1]*n)





a=input()
print(a.center(11,"#"))






a=input()
print(a.count("a"))
print(a.replace("a","b"))
l1=["1","2","3","4"]
print(".".join(l1))



a=input()
b=input()
print((a*3)+b)




a=input()
b=input()
if len(a)==len(b):
    print(" same length")
elif len(a)>len(b):
    print(a + b + a)
else:
    print(b + a + b)




'''a=input()
x=input()
y=input()
z=input()
print(a.startswith("jj"))
print(a.endswith("hhh"))
print(len(a))
print(a.find(z))
print(max(a))
print(min(a))'''



a=input()
if a.startswith("Python"):
    print(a)
else:
    print("Python"+" "+a)




str=input()
print(str.split())


a=input().split()
print(a)



a=input().split(",")
print(a)
print(type(a))




a=input().split()
print(a)
a[3]="rdf"
print(a)
print(a[5])





a=input().split()
print(a)
print(a[0:])
print(a[0::3])
for x in a:
    print(x)





a=input().split()
print(a)
x=eval(input())
if x>=-len(a)<x:
    print(a[x])
else:
    print("invalid")








a=input().split()
print(a)
a.append(("5","7"))
a.extend(("6","8"))
print(a)


a=input().split()
for i in range(0,len(a)):
    a[i]=int(a[i])
if a[0]==3 or a[-1]==3:
    print("true")
else:
    print("false")



a=input().split()
b=input().split()
x=int(input())
print(a+b)
print(a*x)


a=input("data:").split()

if a[0]==a[-1]:
    print("equal")
else:
    print("not equal")



a=input("data:").split()
print("before updatation:",a)
x=int(input())
if x>=-len(a)<x:
    b=input().split()
    a[x]=b
    print("after updatation:",a)
else:
    print("invalid")
    





a=input("data:").split()
for i in range(0,len(a)):
    a[i]=int(a[i])
if a[0]>a[-1]:
    print(a[0])
else:
    print(a[-1])





a=input("data:").split()
b=a
print(b is a)



a=input("data:").split()
b=list(a)
print(b is a)



a=input("data:").split()
b=a[:]
print(b is a)



a=input("data:").split()
b=a.copy
print(b is a)




a=input("data:").split()
b=input("data:").split()

if a[0]==b[0] or a[-1]==b[-1]:
        print("True")
else:
    print("False")
  




a=input("data:").split()
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(a)
print(b)





a=input("data:").split()
print(all(a))
a=input("data:").split()
print(any(a))
b=input("data:").split()
print(all(a))
b=input("data:").split()
print(all(a))






a=input("data:").split()
mi=min(a)
print(int(mi))
ma=max(a)
print(int(ma))
print(int(ma)-int(mi))




a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
print(sum(a))
b=[]
for i in range(len(a)):
    b.append(a[i]**2)

print(b)
b[i]=int(b[i])
print(sum(b))


'''a=input("data:").split()
b=input("data:").split()
if len(a)==len(b):
    for i in range(len(a)):
        a[i]=int(a[i])
    for i in range(len(b)):
        b[i]=int(b[i])
    c=[abs(a[i]-b[i])]
    d=[]
    print(d.append(c))
else:
    print("Different lengths")'''
    
   



a=input("data: ")
l=a.split()
t=tuple()
print(a)
print(l)
print(t)
i=int(input())
if 0<i<len(t) or -len(t)<i<-1:
    print(t[i])



a=tuple(input("data: ").split())
i=int(input())
print(a*i)
b=tuple(input().split())
print(a+b)





a=tuple(input("data: ").split())
i=input()
if i in a:
    print("True")
else:
    print("False")





a=tuple(input("data: ").split())
b=tuple(input("data: ").split())
if a==b:
    print("True")
else:
    print("False")




t=tuple(input("data: ").split())
a=input("data: ")
l=list(t)
if a in l:
    l.remove(a)
    print(l)
else:
    print("Not Present")




t=tuple(input("data: ").split())
i=int(input("Start index"))
j=int(input("End index"))
if (i<len(t) and j<len(t)) and (i>=-(len(t)) and j>=-(len(t))):
    print(t[i:j])
else:
    print("Enter valid index")













a=tuple(input("data: ").split())
print(a)
i=input()
if i in a:
    print(a.count(i))
else:
    print("Enter valid element")






for i in range(len(a)):
    a[i]=int(a[i])
t=tuple(a)
print(sum(t))






d={}
print(d)
d1={1:23,5:98,4:24}
print(d1)
print(d1[5])
print(d1.get(4))
for k,v in d1.items():
    print(k,v)






a=(input("data: ").split())
b=(input("data: ").split())
print(dict(zip(a,b)))







if len(a)==len(b):
    for i in range(len(a)):
        d[a[i]]=b[i]
        print(sorted(d.item()))
else:
    print("invalid")




a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
k=input("key:")
if k in d:
    print("value:",d.get(k))



a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
for k,v in d.items():
    print(k ,v)



a=(input("data: ").split())
print(a)
c=[]
for i in range(0,len(a)):

    c.append(len(a[i]))
print(dict(zip(c,a)))




i=input()
if i==i[-1::-1]:
    print("palidrome")
else:
     print(" not palidrome")
    



def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=eval(input())
for i in range(1,n+1):
    print(fib(i))





a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
k=input("key:")
if k in d:
    d.pop(k)
    s=sorted(d.items())
else:
    ("Doesnot exist")
print(s)




a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
l=[]
s=sorted(d.items())
for k in a:
    if k in d:
        l.append(d[k])
print(max(l))
print(min(l))



a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
k=input("key:")
if k in d:
    j=input("value:")
    d[k]=j
    print(d)
else:
    print("Doesnot exist")



a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
print(all(d))
print(any(d))
print(len(d))
print(sorted(d.items()))




a=(input("data: ").split())
b=(input("data: ").split())
d=dict(zip(a,b))
print((d))
c=dict(zip(b,a))
print(c)


a=input("data: ")
b=input()
if b in a:
    print(a.remove(b))






class Student():
    r=0
    n=None
    def detail(self):
        r=int(input())
        n=input()
        print(r,n)
        
s1=Student()
s1.detail()








class STU:
    def det(self,r,n):
        self.r=r
        self.n=n
    def pd(self):
        print(self.r,self.n)
s1=STU()
s1.det(1,"ddf")
s1.pd()

s2=STU()
r=int(input())
n=input()
s1.det(r,n)
s1.pd()





class Student():
    def __init___(self,r,n):
        self.r=r
        self.n=n
        print(self.r,self.n)
r=int(input())
n=input() 
s1=Student(r,n)






class Employee:
    pass
emp1=Employee()
name=input()
emp1.name=name
age=int(input())
emp1.age=age
salary=int(input())
emp1.salary=salary
print(emp1.name)
print(emp1.age)
print(emp1.salary)





class Employee:
    pass
emp1=Employee()
emp1.name=input()
emp1.age=int(input())
emp1.salary=int(input())
print(emp1.name)
print(emp1.age)
print(emp1.salary)




class Student:
    pass
s1=Student()
s1.name=input()
s1.age=int(input())
s1.degree=(input())
print("s1.name",s1.name)
print("s1.age",s1.age)
print("s1.degree",s1.degree)






class Car:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
Honda=Car()
carname=input("car name: ")
Honda.setName(carname)
print("Honda car name:",Honda.getName())




class Car:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
Honda=Car()
carname=input("car name: ")
Honda.setName(carname)
print("Honda car name:",Honda.getName())






class book:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def show(self):
        print(self.id,self.name,self.price)
b1=book(101,'Python',250)
b1.show()









class student:
    def get_info(self):
        self.id=input('Enter id')
        self.name=input('enter name')
        
    def show_info(self):
        print(self.id,self.name)


class result(student):
    def get_result(self):
        self.marks=int(input('enter marks'))
    def show_marks(self):
        print(self.marks)
    def sow_r(self):
        print(self.id,self.name,self.marks)

r=result()
r.get_info()
r.show_info()
r.get_result()
r.show_marks()
r.sow_r()






class employee:
    def get_info(self):
        self.id=input('Enter id')
        self.name=input('enter name')
        
    def show_info(self):
        print(self.id,self.name)






class salary:
    def get_salary(self):
        self.sal=int(input('enter salary'))
        self.ben=int(input('enter ben'))
    def show_salary(self):
        print(self.sal)
    def sow_r(self):
        print(self.id,self.name,self.sal)
        print(self.sal+self.ben)
class calculate(employee,salary):
    pass
r=calculate()
r.get_info()
r.show_info()
r.get_salary()
r.show_salary()
r.sow_r()




class A:
    def __init__(self):
         print('inparent class')
class B(A):
    def __init__(self):
        super().__init__()
        print('inchild class')
ob=B()



class student:
    def get_info(self, id=None,name=None):
        self.id=id
        self.name=name
        print(self.id,self.name)
r=student()
r.get_info()
r.get_info("12216307")
r.get_info("12216307","arefrv")




class student:
    def get_info(self, id=None,name=None):
        self.id=input('Enter id')
        self.name=input('enter name')
        print(self.id,self.name)
r=student()
r.get_info()
r.get_info("12216307")
r.get_info("12216307","arefrv")




class student:
    __reg=" "
    __name=" "
    def __get_info(self,r,n):
        self.__reg=r
        self.__name=n
    def show_info(self,r,n):
        self.__get_info(r,n)
        print(self.__reg,self.__name)
s=student()
s.show_info("12216307","abc")




a=list(a for a in range(1,11))
print(a)
b=[x for x in "python"]
print(b)
c=[x*y for x in range[1,2,3,4] for y in range[1,2,3,4]]
print(c)
d=[x for x in range[1,2,3,4] for y in range[1,2,3,4] if a==b]
print(d)







d1={i:i**2 for i in range(1,11)}
print(d1)
d2={i.lower():i for i in "PYTHON"}
print(d2)
d3={i:chr(i) for i in range(65,100)}
print(d3)





f=open('mi.txt',"w")
f.write("THIS IS MY FILE")
f.close()

d=open("sudent.txt","w")
r=input("enter")
n=input("name")
d.write(r)
d.write(n)
d.close()




f=open('mi.txt',"r")
s1=f.read()
print(s1)

f=open('mi.txt','r')
for i in f:
       print(i)





f=open('mi.txt',"r")
s1=f.read()
print(s1)



f=open('c.txt',"w")
for i in "mi.txt":
    f.write(i)
f.close()



f=open('mi.txt',"r")
v=open('mi.txt',"a")
v.write("abc")
f.close()
v.close()





f=open('mi.txt')
l=0
w=0
c=0
for x in f:
    l=l+1
    w=w+len(x.split())
    c=c+len(x)
print(l)
print(w)
print(c)


import pickle
stu={1:["wedf","sdfghjk"],2:["wsdf","sxdfcgv"],3:"dcvb"}
fw=open('stu.dat',"wb")
pickle.dump(stu,fw)
fw.close()

fr=open('stu.dat',"rb")
data=pickle.load(fr)
try:
    while True:
        print(data)
        pickle.load(fr)
except:
    print('file read')
print('hello world')


a=int(input())
b=int(input())
try:
    c=a//b
    print(c)
except:
    print("SDFGHJ")
print("qqqqqqqqwerty")


ma={"wedf":23,"wsdf":45,"rfdc":34}
n=input()
try:
    print(ma[n])
except KeyError:
    print("kjvbjhgbgfdfd")
print("end")



try:
    a=int(input())
    b=int(input())
    c=a+b
    c=a-b
    c=a/b
    c=a*b
except ZeroDivisionError:
    print("0 error")
except NameError:
    print("name")
except Exception:
    print("zsxdfghj")


try:
    print("1")
    try:
        print("2")
    except:
        print("3")
    finally:
        print("4")
except:
    print("5")
finally:
    print("6")


try:
    print("outer")
    try:
        print("inner")
        print(10/0)
    except ZeroDivisionError:
        print("ZERO")
    finally:
        print("in fin")
except:
    print("out excp")
finally:
    print("outer finally")


try:
    print("outer")
    try:
        print("inner")
        print(10/0)
    except ZeroDivisionError:
        print("ZERO")
    finally:
        print("in fin")
except:
    print("out excp")
finally:
    print("outer finally")


try:
    f=open("My..txt","r")
    print(f.read())
except IOError:
    print("error")
else:
    print("Content written")


def checkage(a):
    if a<0:
        raise ValueError("age shld >= 0")
    print("Age is value")
try:
    a=int(input("Age: "))
    checkage(a)
except ValueError as err:
    print(err.args)
finally:
    print("executed")


try:
    a=5
    b="fgb"
    print(a+b)
except TypeError:
    print("unsupported")
print("out")


class Ourexp(Exception):
    def __init__(self,message):
        self.message=message
class usingexp:
    try:
        a=int(input("a:"))
        b=int(input("b:"))
        if b==0:
            raise Ourexp("b >0")
        d=a/b
        print(d)
    except Ourexp as e:
        print(e.message)
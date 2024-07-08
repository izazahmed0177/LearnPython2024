
# python list

x=[1,2,3,4]
x1=[1,2,3,4,"emon",1.443]
x2=[1,2,3,4,"emon",[12,34,56,6.77,"jjhg"],1.443]
u=[]
print(type(u))
print(type(x))
print(x)
print(x1)
print(x2)
print("=======================")

x3=(1,2,3,4)
y=list(x3)
print(type(x3))
print(type(y))
print(x3)
print(y)
print("=======================")
print("=======================")
lis=[1,2,3.56,4,"emon",3+6j,[12,34,"aksh",56,6.77,"jjhg"],1.443]
print(lis)
print(lis[2])
print(lis[4])
print(lis[5])
print(lis[6])
print(lis[6][2])
print(lis[:-1])

print("=======================")
print("======== list method ===============")

li=[11,1,6,2,-9,3,4]
li2=[11,1,6,2,-9,3,4]
li3=[11,1,6,2,-9,3,4,6,7,6]
print(li)
li.append(10)

li2.sort()
print(li2)
li3.reverse()
li2.reverse()
print(li2)


li1=li.copy()
print(li)
print(li1)
print(li2)
print(li3.count(6))
print("=======================")
li4=[11,1,4,6,2,-9,3,4]
li6=[11,1,4,6,2,-9,3,4]
print(li4)
li4.pop(3)
print(li4)
li4.insert(0,30)
print(li4)
li4.remove(4)
print(li4)



li5=[11,-9,3,4]
li4.extend(li5)
print(li4)
print(li6)
li6.clear()
print(li6)

print("=======================")
print("======== list operator ===============")

val=["apple","banana","mango"]
val1=["apple11","banana22","mango33"]
print(val)
print(val*3)
val2=val+val1
print(val+val1)
print(val2)
print(len(val))
print(len(val2))

for i in val:
    print(i)

print("=======================")

for i in val2:
    print(i)
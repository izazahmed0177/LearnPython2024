def fun():
    print("Hello bangladesh")

fun()

def function1(x,y,z):
    print(x+y+z)

function1(4,5,6)

# Arbitrary Arguments

def function2(*x):
    print(x)

function2(6,7,8,9)

def fun1(k1,k2,k3):
    print("flower" ,k1,k2,k3)

fun1(k1="rose",k2="water lile",k3="maregold")

def fun2(**k3):
    print("flower" ,k3)

fun2(k1="rose",k2="water lile",k3="maregold")

def fun3(x='python'):
    print(x)

fun3()
fun3(x='java')

# return value

def function2(x):
    return x*3

print(function2(5))
print("=================")
n=int(input("inter a number: "))
print(function2(n))
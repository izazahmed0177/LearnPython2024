
# if,elif,else statement

x1=int(input("Enter a number:"))

# if x>0:
#     print('number grater them 0 number are:',x)
# elif x<0:
#     print('number less them 0 number are:',x)
# else: print('number is equal them 0 number are:',x)



if x1>0:
    print('number grater them 0 number are:',x1)
    if x1%2==0:
        print('even')
    else:print("odd")
elif x1<0:
    print('number less them 0 number are:',x1)
else: print('number is equal them 0 number are:',x1)

print('================')
x2 = 5

if x2 >= 5:
    print('hello')

elif x2<=5:
    print('Bye ')

elif x2==5:
    print('Hi')

else:
    print('Nothing ')


print('====================')


x = -10
if x>0:
    print('Right')
    if x == -10:
        pass
elif x<0:
    if x != 0:
        print("Love")
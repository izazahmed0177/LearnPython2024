

# loop

# print(range(0,101))

# for loop

numbers=[1,2,3,4,5,6,6,7]
count=0

for i in numbers:
    print(i)

print('======')

for i in numbers:
    count +=i;


print(count)

for i in range(4):
    print(i)

for i in range(4):
    print('bangladesh')

print('=======================')

# nestade for loop

for i in range(4):
    print('bangladesh')
    for j in range(2):
        print("hello")

# loop with condition
print('*************************')

for i in range(5,50):
    print(i)
print("=================")

for i in range(5,51,5):
    print(i)

print("----------------------------")
# use if condition
for i in range(5,51):
    if i%5==0:
        print(i)
print("----------------------------")
print("---------while loop-------------------")
# whilr loop

x=1
while x<46:
    print(x)
    x=x+1;

print("----------------------------")
y=10
while y<61:
    print(y)
    y=y+10;

print("----------------------------")
print("----------------------------")
print("-------------infinite loop---------------")

# infinite loop

# p=True
# while p:
#     print("hello")

# p=1
# while p>=1:
#     print("hello")
#     x=x+1


# p=1
# while p:print("python")


print("----------------------------")
print("----------------------------")
print("------------- brack statement ---------------")

for i in range(1,21):
    print(i)
    if i==10:
        break

print("----------------------------")
print("----------------------------")
print("------------- continue statement ---------------")

for i in range(1,21):

    if i==10:
        continue
    print(i)

print("----------------------------")
for i in range(1,21):

    if i%2==0:
        continue
    print(i)


print("----------------------------")
print("------------- pass statement ---------------")

for i in range(1,21):
    pass
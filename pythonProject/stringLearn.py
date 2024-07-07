
# string

str1="hello"
str2=""""
izaz
    ahmed
         emon
"""

print(str2)
print("==========================")
print(str1)
print(str1[1])
print(str1[4])
print(str1[-1])
print(str1[-2])
print(str1[:])
print(str1[1:])
print(str1[:3])
print(str1[1:4])
print(str1[2:-1])
print("=====================")
print("=====================")
print("========string formating=============")

# string formating

x="I have a red car.It is vary nice"
# use formating
y="I have a {color} car.It is vary {attribute}".format(color='yello',attribute='good')
print(x)
print(y)
color="Green"
attribute="beautifull"
# use f string
z=f"I have a {color} car.It is vary {attribute}"
print(z)

print("=====================")
print("=====================")
print("========Scape Sequence=============")

# Scape Sequence

name="hello\nworld\npython"
name1="hello\n'world'\npython"
name2="hello\n\"world\"\npython"
name3="hello\n\"world\"\npython  learn"
name4="hello\n\"world\"\npython\tlearn"
name5="hello\n\"world\"\npython\t/\learn"
name6="hello\n\"world\"\npython\t\/learn"
print(name)
print(name1)
print(name2)
print("==============")
print(name3)
print(name4)
print(name5)
print(name6)
name7="hello\n\"world\"\npython\tlearn\b"
print("==============")
print(name7)
str3="my country Bangladesh"
str4="my country is \rBangladesh"
str5="my country \ris Bangladesh"

print(str3)
print(str4)
print(str5)



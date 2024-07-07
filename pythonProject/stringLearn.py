
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

print("=====================")
print("=====================")
print("======== string operators =============")
# string operators
value=" hello"
value2=" hello"
value0=" hello"
value1=" world"
print( value * 5 )
print( value0 + value1 )
print('a' in value2)
print('e' in value2)
print('e' not in value2)

print("=====================")
print("=====================")
print("======== string modify =============")
# string modify

n="haPPy New year"
print(n)
print(n.lower())
print(n.casefold())
print(n.upper())
print(n.capitalize())
print(n.title())
print(n.swapcase())
print(n.split())
print(n.replace('New','old'))
print("========")
p="izaz "
q="Ahmed Emon"
print(p.join(q))

print("=====================")
print("=====================")
print("======== string state checking =============")

# string state checking

data='python'
data2='PYTHON'
data3='PYTHOn'
data1='python 123'
data4='123'
data6='123.233'
data5='12a87'
print(data.isalpha())
print(data1.isalpha())
print(data.islower())
print(data.isupper())
print(data2.isupper())
print(data3.isupper())
print(data4.isdigit())
print(data5.isdigit())
print(data4.isdecimal())
print(data6.isdecimal())
print("=====================")
data7='else'
data8='Hello world'
data9='Hello World'
data11='Hello World'
data10='  '
print(data7.isidentifier())
print(data8.istitle())
print(data9.istitle())
print(data11.isspace())
print(data10.isspace())



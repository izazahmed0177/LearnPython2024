

#logical operator: or ,and, not


num1=10
num2=20
num3=10
num4=5

# logical or
print(num1>num2 or num1==num2)
print(num1<num2 or num1==num2)

print(num1>num2 or num1!=num2)
print(num1<num2 or num1!=num2)

# ===============
print('==================')

# logical and

print(num1>num2 and num1==num2)
print(num1<num2 and num1==num2)

print(num1>num2 and num1!=num2)
print(num1<num2 and num1!=num2)

# logical not
print('===----==or not===========')

print(not (num1>num2 or num1==num2))
print( not (num1<num2 or num1==num2))

print( not (num1>num2 or num1!=num2))
print(not (num1<num2 or num1!=num2))

print('====and not =========')
print(not (num1>num2 and num1==num2))
print( not (num1<num2 and num1==num2))

print( not (num1>num2 and num1!=num2))
print(not (num1<num2 and num1!=num2))

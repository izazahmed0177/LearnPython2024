
# python set

# set unorder list \\ do not support duplicat
# do not support indexing
set1={10,30,20,34,5,7,2,40,20}
set2={10,30,20,34,5,"apple",45.776,5+7j,7,2,40,20}
# list order list \\  support duplicat
# support indexing
list1=[10,30,20,34,5,7,2,40,20]
print(type(set1))
print(type(list1))
print(set1)
print(list1)
print(set2)

t1=(10,30,7,20,34,5,7,2,40,20)
set3=set(t1)

print(t1)
print(set3)

print("=======================")
print("=======================")
print("========== set method =============")

s={'python','java','c','rrr'}
c={'ruby','C#','ccc'}
d=c.copy()
print(s)

s.add('r')
print(s)

s.update(c)
print(s)
s.discard('ccc')
print(s)
s.remove('rrr')
print(s)
# pop any last item remove
s.pop()
print(s)
print(d)
d.clear()
print(d)

print("=======================")
print("=======================")
print("========== set operator =============")

month1={'january','march','may','july','octmber',}
month2={'january','february','april','may','june',}
union=month1.union(month2)
print(union)

intersection=month1.intersection(month2)
print(intersection)

diffirence1=month1.difference(month2)
diffirence2=month2.difference(month1)
print(diffirence1)
print(diffirence2)

symdiff=month1.symmetric_difference(month2)
print(symdiff)






student={}
print(type(student))

st={"name":"arif","id":1,"roll":45}
print(st)
print(student)
student[0]='arif'
print(student)
student['roll']=4
print(student)
student['email']='aaa@gmail.com'
print(student)
print('======================')
print('======================')
print('===========Access===========')

st1={"name":"arif","id":123,"roll":45}

print(len(st1))
print(st1['roll'])
print(st1.keys())
print(st1.values())
print(st1.items())

print('======================')
print('======================')
print('===========nested dic===========')

studentData={
    'student 1':{
        "name":"arif",
        "id":123,
        "roll":45,
        'blood group':'B+'

    },
    'student 2':{
        "name":"arif11",
        "id":1234,
        "roll":456,
        'blood group':'O+'

    },
    'student 3':{
        "name":"arif22",
        "id":12345,
        "roll":4567,
        'blood group':'A+'
    },
}

print(studentData)
print(studentData['student 2'])
print(studentData['student 2']['blood group'])
print(studentData['student 2'].values())
print(studentData['student 1'].keys())
print(studentData['student 3'].items())

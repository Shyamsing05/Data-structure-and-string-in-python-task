
student={ 'alice' :{'class': 5, 'marks':98.5},'riya':{'class': 11, 'marks':91},'sam':{'class': 6, 'marks':60.2}}

name = input("Enter student's name : ")
if name == 'alice':
    print(student['alice'])
elif name =='riya':
    print(student['riya'])
elif name =='sam':
    print(student['sam'])
else:
    print("Student not found")
from pydantic import BaseModel

class Student(BaseModel):
    age:int
    name:str
    phone:str



def student_data(student: Student):
    print(student.name)
    print(student.age)
    print(student.phone)
    print(type(student.name))
    print(type(student.age))
    print(type(student.phone))


# Passing age as an integer
data={
    "age":23,
    "name":"Ali",
    "phone":"03343545"
}
student=Student(**data)
student_data(student)

# Passing age as a string
data={
    "age":"23",
    "name":"Ali",
    "phone":"03343545"
}
student=Student(**data) # pydantic convert "23" to integer 23
student_data(student)   



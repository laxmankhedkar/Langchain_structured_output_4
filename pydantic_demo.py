from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name : str = 'Laxman'    # default value 
    age : Optional[int] = None  # set a value optional 
    email : EmailStr
    cgpa : float = Field(gt = 0, lt = 10, default= 5)

new_student = {'age':'24','email':'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['name'])


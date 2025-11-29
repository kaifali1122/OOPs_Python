# Polymorphism - allow method in diffent classes to have same name but different behaviour
#                [Method name same ho but uska function diffenrt ho]

# Example- Std_details Student me bhi hai or Graduate me bhi hai but behaviour alag alag hai

class Student: #class
    def __init__(self, name , grade , percentage): # method 
        self.name= name #attributes
        self.grade = grade 
        self.percentage = percentage 
    def Stu_details(self):
        print(f'{self.name} is in {self.grade}, with {self.percentage}%') 

# Inheritance 
class Graduate(Student): #here we inherit Student 
    def __init__(self,name, grade , percentage, stream):
        super().__init__(name, grade, percentage) #using super 
        self.stream= stream

    def Stu_details(self):
        super().Stu_details() #Here we inherit Method
        print(f'in {self.stream} Stream')    



#object
Student1= Student('Kaif',11,94)
Student2= Graduate('Atif',11,93,"PCM")

Student1.Stu_details() # Kaif is in 11, with 94%
Student2.Stu_details() # Atif is in 11, with 93%

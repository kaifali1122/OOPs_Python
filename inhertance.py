# Inheritence - allow one class [child] to reuse the properties/ attributes and method of another class[parents]

# super()- for connection with parent class we have to use super to make relation
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
         #Here we inherit Method
        print(f'in {self.stream} Stream',super().Stu_details())    



#object
Student1= Student('Kaif',11,94)
Student2= Graduate('Atif',11,93,"PCM")

Student1.Stu_details() # Kaif is in 11, with 94%
Student2.Stu_details() # Atif is in 11, with 93%

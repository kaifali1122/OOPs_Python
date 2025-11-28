#class- blueprint or template 
class Student: #class
    def __init__(self, name , grade , percentage): # method 
        # [__init__ - reserved for first method] [(self)- used to make connection/ relation between class and Object]
        self.name= name #attributes
        self.grade = grade 
        self.percentage = percentage 
    def Stu_details(self):
        print(f'{self.name} is in {self.grade}, with {self.percentage}%')

# objects-instance of class
Student1= Student('Kaif',11,94)
Student2= Student('Atif',11,93)

Student1.Stu_details() # Kaif is in 11, with 94%
Student2.Stu_details() # Atif is in 11, with 93%

#modify object property/attributes
Student1.percentage = 95 
Student2.grade = 12 
Student2.name = 'Kashif'

# modified data 
Student1.Stu_details() # Kaif is in 11, with 95%
Student2.Stu_details() # Kashif is in 12, with 93%

#Delete object property/attributes
del Student1.percentage
del Student2.grade

# modified data 
# Student1.Stu_details() # Error- "'Student' object has no attribute 'percentage'"
# Student2.Stu_details() # Error- "'Student' object has no attribute 'grade'"

#delete whole object 
del Student1

print (Student1)

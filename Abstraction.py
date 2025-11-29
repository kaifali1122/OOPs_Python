# Abstractin- Hiding unnecessary detils from user through class and method

# Example - here i class percentage of every one increse by 2
#           but in object it does not reflect its wass hidden for user
#  
class Student: #class

    def __init__(self, name , grade , percentage): # method 
        self.name= name #attributes
        self.grade = grade 
       
        self.percentage = percentage 
        
    
    def Stu_details(self):
        #here we added 2 in percentage but it was hidden from user
        print(f'{self.name} is in {self.grade}, with {self.percentage+ 2}%') #here we added 2 in percentage but it was hidden from user

#object
Student1= Student('Kaif',11,94)
Student2= Student('Atif',11,93)

Student1.Stu_details() # Kaif is in 11, with 96%
Student2.Stu_details() # Atif is in 11, with 95%

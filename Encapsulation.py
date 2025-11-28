# Encapsulation- it restrict access to certain attribute 
# of mrthod to protect data nd enforce control access

# Example- here we make percentage private using '__'
# now percentage is encapsulte no one can directly access it

class Student: #class
    def __init__(self, name , grade , percentage): # method 
        self.name= name #attributes
        self.grade = grade 
        # using '__' we can limit percentage access
        self.__percentage = percentage 
        # now no one can acess percentage directly from object 
    def get_percentage(self):
        return self.__percentage    

    def Stu_details(self):
        print(f'{self.name} is in {self.grade}, with {self.__percentage}%') 

#object
Student1= Student('Kaif',11,94)
Student2= Student('Atif',11,93)

Student1.Stu_details() # Kaif is in 11, with 96%
Student2.Stu_details() # Atif is in 11, with 95%

# accessing private attribute using method
print(Student1.get_percentage()) # 94

print(Student1.__percentage)
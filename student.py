class Student:
     school = "Akirachix"
     def __init__(self,country,first_name,second_name,age):
        self.first_name = first_name
        self.country = country
        self.second_name = second_name
        self.age = age
     def full_name (self):
         return f"Greetings! {self.first_name} {self.second_name} How is {self.country}"
     def year_of_birth (self):  
         year=2022 - self.age
         return f"Greetings! you are born in {year}"
     def initials (self):
         return f"Greetings! your initials are {self.first_name[0]} {self.second_name[0]}"
    
#basic class example
class Person:
    def __init__(self, firstname, lastname, age, occupation):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.occupation = occupation
        
    def intro(self):
        return f"Hello, my name is {self.firstname} {self.lastname}. I am {self.age} years old and I work as {self.occupation}."
    
P1 = Person("John", "Doe", 30, "Software Engineer")
print(P1.intro())

P2 = Person("Chris", "Evans", 35, "Actor")
print(P2.intro())

P3 = Person("Emma", "Watson", 28, "Actress")
print(P3.intro())
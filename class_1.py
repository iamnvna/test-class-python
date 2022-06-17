# initiating a class
class Person:
    def __init__(self, name, age, favorite_colour, sex):  # class with attribute arguments
        self.name = name                                  # initaiting the attributes
        self.age = age
        self.favorite_colour = favorite_colour
        self.sex = sex
        

    def my_age(self):                                     # class instance method for age
        if self.age<=18:
            print(f"Wow, {self.name} your're young")      # printing based on age attribute and condition
       else:
            print(f"Ey, {self.name} you're old!")
        return
          


Theodora = Person("Theodora", 50, "brown", "female")     # passing attributes to the initialized class and saving in a variable name 
#Theodora.my_age()                                       # remove hash symbol  # code calls on the class method my_age
Thomas = Person("Thomas", 18, "brown", "male")           # passing attributes using same class yet a differOent variable and attributes
#Thomas.my_age()
#kofi = kirlin.my_age()

    

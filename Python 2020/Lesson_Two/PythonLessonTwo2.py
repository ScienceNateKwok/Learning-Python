#a dog class

class Dog:

    """A simple dog class"""
    #object constructor
    def __init__(self, name, age):

        """Intialize name and age attributes"""
        self.name = name
        self.age = age

    #method
    def sit(self):

        """Simulate a dog sitting in responseto a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):

        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    

# REPL: https://repl.it/@DamyanPeykov/OOP-methods

class Character:
# Class Object Attribute - this is not dynamic - it is static
# We can call it inside the class with self or with Character - self.class_obj_att or Character.class_obj_att
    class_obj_att = True
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Instance Methods - act on an instance data - must have self as param
    # Inside any instance method, you can use self to access any data or methods that may reside in your class.
    def sing(self,song):
        return song

    # Static Methods - related to a class in some way, but don’t need to (can't) access any class-specific data
    # No need to use self or even to instanciate the class - you can just call it directly
    # Static methods are great for utility functions, which perform a task in isolation.
    # The static methods should be self contained and use only data that is passed to them
    @staticmethod
    def example_function():
        """ This method is decorated! - NO NEED TO USE ANY CLASS-SPECIFIC DATA"""
        print('I\'m a static method - using a decorator!')

    # Class Methods - class methods know about their class. They can’t access specific instance data, but they can call other static methods.
    # Class methods don’t need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python.
    #  Class methods can manipulate the class itself, which is useful when you’re working on larger, more complex projects.
    @classmethod
    def example_function_2(cls):
        """ This method is a class method! """
        print('I\'m a class method!')
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print('Hello!')

# Instantiating a class
singer1 = Character("Tom", 42)

print(f'{singer1.name}, {singer1.age}, {singer1.sing("Blah Blah")}, {singer1.class_obj_att}')  # Tom, 42, Blah Blah, True
# When an instance method is called - the self variable is passed automatically to the class

# https://www.makeuseof.com/tag/python-instance-static-class-methods/
# There are three types of methods in Python: instance methods, static methods and class methods.
# Decorator (design pattern) is just a function - like any function, decorators perform a task. The difference here is that decorators apply logic or change the behavior of other functions. They are an excellent way to reuse code, and can help to separate logic into individual concerns.

print(singer1.example_function()) # I'm a static method - using a decorator! + None
# Static method - no need to instanciate the class - can call it directly
print(Character.example_function()) # I'm a static method - using a decorator! + None

print(singer1.example_function_2()) # I'm a class method! + Hello! + None
print(Character.example_function_2()) # I'm a class method! + Hello! + None

# It’s possible to combine multiple decorators, write your own, and apply them to classes

#In summary:

    # Instance Methods: The most common method type. Able to access data and properties unique to each instance.
    # Static Methods: Cannot access anything else in the class. Totally self-contained code.
    # Class Methods: Can access limited methods in the class. Can modify class specific details.

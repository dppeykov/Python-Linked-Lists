# REPL: https://repl.it/@DamyanPeykov/OOP

class Character:
    # Class Object Attribute - this is not dynamic - it is static
    # We can call it inside the class with self or with Character 
    class_obj_att = True
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return song

# Instantiating a class
singer1 = Character("Tom", 42)

print(f'{singer1.name}, {singer1.age}, {singer1.sing("Blah Blah")}, {singer1.class_obj_att}')

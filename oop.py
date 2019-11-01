class Caharacter:
    class_att = True
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return song

# Instantiating a class
singer1 = Caharacter("Tom", 42)

print(f'{singer1.name}, {singer1.age}, {singer1.sing("Blah Blah")}, {singer1.class_att}')

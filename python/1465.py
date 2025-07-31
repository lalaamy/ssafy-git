class Animal:
    def __init__ (self):
        pass

class Dog(Animal):
    def __init__(self):
        self.sound = "멍멍"

class Cat(Animal):
    def __init__(self):
        self.sound = "야옹"
    
class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    def __str__ (self) :
        return f"애완동물은 {self.sound} 소리를 냅니다"

pet1 = Pet()
print(pet1)
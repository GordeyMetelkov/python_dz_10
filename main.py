# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа. Внутри класса создайте экземпляр на основе
# переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return f'{self.name} {self.spec}'

class Dog(Animal):
    def __init__(self, name: str, age: int, spec='pwohw'):
        super().__init__(name, age)
        self.spec = spec

class Cat(Animal):
    def __init__(self, name: str, age: int, spec='miioow'):
        super().__init__(name, age)
        self.spec = spec

class Bird(Animal):
    def __init__(self, name: str, age: int, spec='fiiuuw'):
        super().__init__(name, age)
        self.spec = spec


class Fabric:
    def create(self, animal, *args):
        return animal(*args)

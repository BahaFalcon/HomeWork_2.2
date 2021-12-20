class Fauna:
    def __init__(self, type, age):
        self.type = type
        self.age = age

class Bird(Fauna):

    def __init__(self, fly):
        super(Bird, self).__init__(Bird, fly)
        self.fly = fly
    def can_fly(self):
            return f'I can fly'


class Fish(Fauna):
    def __init__(self, swim):
        super(Fish, self).__init__(Fish, swim)
        self.swim = swim

    @classmethod
    def can_swim(self):
        return f'True'

class Mammal(Fauna):
    def __init__(self, feed_on_milk):
        super(Mammal, self).__init__(Mammal, feed_on_milk)
        self.feed_on_milk = feed_on_milk

class Predator:
    def eat(self, food):
        self.food = food
        return f'I eat {self.food}'
class Herbivore:
    def eat(self, food):
        self.food = food
        return f'I eat {self.food}'



class Falcon(Bird, Predator):
    def __init__(self, type, age):
        super(Falcon).__init__(Falcon)
        self.type = type
        self.age = age
    def info_self(self):
        return f'{self.type}, {self.age}'

class Penguin(Bird, Fish, Herbivore):
    def __init__(self, type, age):
        super(Penguin).__init__(Penguin)
        self.type = type
        self.age = age
    def info_self(self):
        return f'{self.type}, {self.age}'
    @staticmethod
    def can_fly():
        return f'I cannot fly'

class Trout(Fish, Predator):
    def __init__(self, type, age):
        super(Trout).__init__(Trout)
        self.type = type
        self.age = age
    def info_self(self):
        return f'{self.type}, {self.age}'

class Whale(Fish, Herbivore):
    def __init__(self, type, age):
        super(Whale).__init__(Whale)
        self.type = type
        self.age = age
    def info_self(self):
        return f'{self.type}, {self.age}'



f = Falcon(type='saker', age='2 year')
print(f.info_self())
print(f.eat('bird'))
print(f.can_fly())
print('-----------------------------------')
p = Penguin(type='royal', age='1 year')
print(p.info_self())
print(p.eat('fish'))
print(Penguin.can_swim())
print(Penguin.can_fly())
print('-----------------------------------')
t = Trout(type='rainbow', age='3 year')
print(t.info_self())
print(t.eat('small fish'))
print(t.can_swim())
print('------------------------------------')
w = Whale(type='blue', age='10 year')
print(t.info_self())
print(t.eat('plankton'))
print(t.can_swim())

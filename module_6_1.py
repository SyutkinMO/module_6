# ----------- Базовые знания о наследовании классов для решения задачи -----------

class Animal:
    alive = True  # живой, далее наследуется
    fed = False  # сытый

    def __init__(self, name):
        self.name = name

    def eat(self, food):  # food - принимает объекты Plants и обращается к ним
        self.food = food
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True  # обращение к родительскому классу
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False  # обращение к родительскому классу


class Plant:
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal):  # Хищник
    def __init__(self, name):
        self.name = name


class Predator(Animal):  # Травоядное
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)  # Хищник съел цвето и погиб
print(a2.fed)  # Животное съело фрукт и насытилось

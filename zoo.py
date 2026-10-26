from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food_per_day(self):
        pass

    def describe(self):
        return f"{self.name}: {self.sound()}"


class Lion(Animal):
    def sound(self):
        return "Р-р-р"

    def food_per_day(self):
        return self.weight * 0.05


class Parrot(Animal):
    def sound(self):
        return "Привет!"

    def food_per_day(self):
        return self.weight * 0.1


class Zoo:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Можно добавлять только животных")
        self.animals.append(animal)

    def sounds(self):
        return [animal.describe() for animal in self.animals]

    def total_food(self):
        return sum(animal.food_per_day() for animal in self.animals)

    def __len__(self):
        return len(self.animals)


if __name__ == "__main__":
    zoo = Zoo()
    zoo.add(Lion("Симба", 190))
    zoo.add(Parrot("Кеша", 0.5))

    len(zoo)
    zoo.sounds()
    zoo.total_food()

    try:
        Animal("Нечто", 10)
    except TypeError:
        pass

    try:
        zoo.add("слон")
    except TypeError:
        pass

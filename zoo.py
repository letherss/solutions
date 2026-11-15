from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self) -> str:
        """Возвращает звук, издаваемый животным."""
        pass

    @abstractmethod
    def food_per_day(self) -> float:
        """Возвращает массу корма (в кг), необходимую животному в день."""
        pass

    def describe(self) -> str:
        """Возвращает описание животного в формате 'Имя: Звук'."""
        return f"{self.name}: {self.sound()}"


class Lion(Animal):
    def sound(self) -> str:
        return "Р-р-р"

    def food_per_day(self) -> float:
        return self.weight * 0.05


class Parrot(Animal):
    def sound(self) -> str:
        return "Привет!"

    def food_per_day(self) -> float:
        return self.weight * 0.10


class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal: Animal) -> None:
        """Добавить животное в зоопарк."""
        if not isinstance(animal, Animal):
            raise TypeError("В зоопарк можно добавлять только объекты типа Animal")
        self._animals.append(animal)

    def sounds(self) -> list[str]:
        """Возвращает список описаний всех животных в порядке добавления."""
        return [animal.describe() for animal in self._animals]

    def total_food(self) -> float:
        """Возвращает общее количество корма для всех животных зоопарка в день."""
        return sum(animal.food_per_day() for animal in self._animals)

    def __len__(self) -> int:
        """Возвращает общее количество животных в зоопарке."""
        return len(self._animals)


if __name__ == "__main__":
    zoo = Zoo()
    zoo.add(Lion("Симба", 190))
    zoo.add(Parrot("Кеша", 0.5))
    
    print(len(zoo))
    print(zoo.sounds())
    print(zoo.total_food())
    
    try:
        Animal("Нечто", 10)
    except TypeError as e:
        print(f"TypeError при создании Animal: {e}")
        
    try:
        zoo.add("слон")
    except TypeError as e:
        print(f"TypeError при добавлении строки: {e}")

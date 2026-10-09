import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    probability = 1.0
    for i in range(people):
        probability *= (365 - i) / 365
    return 1 - probability

def simulate_birthday(people, trials):
    if people > 365:
        return 1.0
    matches = 0
    for _ in range(trials):
        birthdays = []
        for _ in range(people):
            birthdays.append(random.randint(1, 365))
        if len(set(birthdays)) < people:
            matches += 1
    return matches / trials

if __name__ == "__main__":
    (birthday_probability(1))
    (birthday_probability(23))
    (birthday_probability(50))
    (birthday_probability(366))

    ("Люди | Точная вероятность | Симуляция")
    ("---------------------------------------")

    for people in range(5, 61, 5):
        exact = birthday_probability(people)
        simulated = simulate_birthday(people, 100000)
        print(f"{people:5} | {exact:.6f}           | {simulated:.6f}")

    for people in range(1, 366):
        if birthday_probability(people) > 0.5:
            print(f"\nВероятность превышает 0.5 при {people} людях.")
            break

    ("\nПроверка для 23 человек:")
    ("Точная вероятность:", birthday_probability(23))
    ("Симуляция (1000 экспериментов):", simulate_birthday(23, 1000))
    ("Симуляция (100000 экспериментов):", simulate_birthday(23, 100000))
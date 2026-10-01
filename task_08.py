from datetime import date

def century_message(name, age, current_year):
    year_100 = current_year + (100 - age)
    return f"{name}, тебе исполнится 100 лет в {year_100} году!"

if __name__ == "__main__":
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))

    current_year = date.today().year
    print(century_message(name, age, current_year))
def echo_number(number):
    return "Thats the number you entered " + number

if __name__ == "__main__":
    number = input("Enter number: ")
    print(echo_number(number))
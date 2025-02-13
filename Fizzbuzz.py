for number in range(1, 101):
    print(number)
    if number % 3:
        print("Fizz!")
    elif number % 5:
        print("Buzz")
    else:
        print("FizzBuzz!")
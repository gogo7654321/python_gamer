while("True"):
    print("Enter a number between 1 and 100 and i will count up to it")
    number = int(input())
    for x in range(1,101):
        print(x)
        if (x == number):
            break
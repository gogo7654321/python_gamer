
list_of_numbers = []
for x in range (0,5):
    print ("enter a number")
    num = float(input())
    list_of_numbers.append(num)

lowest_number = 10000.0
for x in list_of_numbers:
    if (x <= lowest_number):
        lowest_number = x

print ("the lowest number is", lowest_number)
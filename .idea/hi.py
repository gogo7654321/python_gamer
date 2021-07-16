print ("enter 5 numbers and i will i will multply them by the power of 2")
numbers = []
for x in range (1,6):
    num =float(input("enter a number: "))
    numbers.append(num)

for x in numbers:
    sqr= x*x
    print (sqr)
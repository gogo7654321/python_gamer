counter = 0
while(counter <= 1):
    print ("enter 4 numbers and i will give you the higest number")
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    higest_number = None
    if (a >= b):
        higest_number = a
        
    else:
        higest_number = b
        
    if (c >= higest_number): 
        higest_number = c
        
    if (d >= higest_number):
        higest_number = d
        
    print (higest_number,"is the higest number")
    counter = counter + 1

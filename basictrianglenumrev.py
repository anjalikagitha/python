

number = 10

for row in range(4, 0, -1): 
    for col in range(1, row + 1): 
        if number < 1:  
            break
        print(number, end=" ")  
        number -= 1
    print()  

rows = 4
number = 6

for row in range(rows, 0, -1): 
    if row == 1:  
        print("3")
    else:
        print(str(number) * row)  
    number -= 1  

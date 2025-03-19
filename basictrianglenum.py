n = 1

for i in range(1, 11):
    for j in range(1, i + 1):  
        if n > 10: 
            break
        print(n, end=" ") 
        n += 1
    if n > 10:  
        break
    print()  

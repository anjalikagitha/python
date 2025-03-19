n=7

for i in range(n):
  if i==0:
    print((n-1)*" "+"*")
  elif i==(n-3):
    print("* "*n)  
  elif i>=4:
    break
  elif i==2:
    print(" "*(n-1-i)+"* "+" "*(i)+"*")  
  elif i==3:
    print(" "*(n-2-i)+"* "+" "*(i+2)+" *")  

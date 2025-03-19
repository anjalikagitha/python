n=7

for i in range(n):
  if i==0:
    print((n*" *"))
  elif i==(n-3):
    print((n-4)* "  "+" *")
  elif i==2:
    print("   "*(i-1)+"* "*(n-2)+" "*(i))  
  elif i==3:
    print("     "*(i-2)+"* "*(n-4)+" "*(i))  

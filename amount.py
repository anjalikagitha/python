amount= int(input("enter the amount : "))
five_hun=amount//500
print(f"Five hundred notes(500) : {five_hun}")
rem=amount%500
hun=rem//100
print(f" Hundred notes(100) : {hun}")
rem=rem%100
fif=rem//50
print(f"Fifty notes(50) : {fif}")
rem=rem%50
ten=rem//10
print(f" ten notes(10) : {ten}")

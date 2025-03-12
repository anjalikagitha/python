a=int(input())
b=int(input())
c=int(input())
print(f"a value {a} is smaller" if a<b and a<c else "")
print(f"b value {b} is   smaller" if b<a and b<c else "")
print(f"c value {c} is smaller" if c<a and c<b else "")


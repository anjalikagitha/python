import keyword

print("Python Keywords:")
print(keyword.kwlist)
print("Total Keywords:", len(keyword.kwlist))

print("\nASCII values of A-Z:")
for i in range(65, 91):
    print(chr(i), "->", i)

print("\nASCII values of a-z:")
for i in range(97, 123):
    print(chr(i), "->", i)

print("\nCharacters for ASCII values 32-126:")
for value in range(32, 127):
    print(value, "->", chr(value))

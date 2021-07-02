# name = input("What is your name? ")
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
# square_meters:.2f reduces the length of digits of a float
print(f"{square_feet} square feet is {square_meters:.2f} square meters")
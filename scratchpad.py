number = 7
play = input("would you like to play? (Y/n) ")

while play != "n":
  user_number = int(input("Guess our number: "))
  if user_number == number:
    print("You guess correctly")
  elif abs(number - user_number) == 1:
    print("You were off by 1.")
  else:
    print("Sorry, it's wrong!")
  
  play = input("Would you like to play? (Y/n) ")
# #While Loops
# s = 0
# while s < 10:
#   s = s + 1
#   print(s)

# cats = input("Do you like cats? ")
# while cats not in ["yes","yeah","YES"]:
#   print("Try again.")
#   cats = input("Do you like cats?")
# if cats in ["yes","yeah","YES"]:
#   print("Finally, the right answer!")

# lucky_number = 3
# money = 10
# while money > 0:
#   guess = input("What's the right number")
#   guess = int(guess)
#   if guess == lucky_number:
#     money = money + 1
#   else:
#     money = money - 1
#   print("You now have ${} left.".format(money))
# if money == 0:
#   print("You're out of money.")


evens = []
while len(evens) < 3:
  num = input("Give me an even number")
  num = int(num)
  if num % 2 == 0:
    evens.append(num)
if len(evens) == 3:
  print(evens)  















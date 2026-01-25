import random
random = random.randint(1, 10)
guess = input("Guess the integer: ")
guess = int(guess)
while guess > 10 or guess < 1: #whatif the user by mistake enters number >10 or <1
    guess = input("Guess the integer between 1 and 10: ")
    guess = int(guess)
if guess < random:
    print("\nToo low!")
elif guess > random:
    print("\nToo high!")
elif random == guess:
    print("\nCorrect!")
print(f"The random integer picked was {random}.") #did this just to check whether the computer generates radom number each time or not)
secret_number = 3
guess = int(input("Guess a number: "))

# This will ask the user to guess the number until they guess it correctly
# while loop will keep executing the code block until the condition is false
while guess != secret_number:
    guess = int(input("Guess a number: "))
else:
    print("You guessed the number correctly!")

i = 2
while True:
    if i % 3 == 0:
        break
    print(i)
    i += 2
# will print 2, 4 and break on 6
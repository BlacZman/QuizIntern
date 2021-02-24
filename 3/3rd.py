numbersToBeGuess = {}
intarray = []

# Input 12 numbers
while True:
    inputarr = input("Enter an input: ")
    array = inputarr.split(" ", 12)
    if len(array) > 12:
        if array[12] == "":
            array.pop()
    try:
        if len(array) != 12:
            raise ValueError
        for item in array:
            number = int(item)
            if number < 0 or number > 9:
                raise ValueError
            intarray.append(item)
    except ValueError:
        intarray = []
        print("Error. Please enter question again.")
    else:
        break

# Numbers to be guess
for item in intarray:
    if numbersToBeGuess.get(item) == None:
        numbersToBeGuess[item] = False

# Input the guess
guessStr = []
roundanswer = ["_ _ _ _ _ _ _ _ _ _ _ _"]
correct = 0

for i in range(5):
    guess = -1
    while True:
        try:
            guess = int(input())
            if guess < 0 or guess > 9:
                raise ValueError
        except ValueError:
            print("Enter your guess again.")
        else:
            break
    
    guess = str(guess)
    if numbersToBeGuess.get(guess) != None:
        numbersToBeGuess[guess] = True
    else:
        guessStr.append(guess)
    
    # String manipulating from numbersToBeGuess keys values
    questionStr = []
    correct = 0
    for item in intarray:
        if numbersToBeGuess[item]:
            questionStr.append(item)
            correct += 1
        else:
            questionStr.append("_")
    
    roundanswer.append(" ".join(questionStr) + " " + " ".join(guessStr))

for item in roundanswer:
    print(item)
print(correct)
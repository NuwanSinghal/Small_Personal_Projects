import random

num_digits = 3
max_guesses = 10

def main():
    print("Welcome to the password game")
    print(f"I have a {num_digits}-digit number with no repeating digits in mind as the password")
    print("Here is what the responses to your guesses mean" 
          "\nPico - One digit is correct but in the wrong position"
          "\nFermi - One digit is correct and in the right position"
          "\nWrong - None of the digits are correct")

    while True:
        secretNum = getSecretNum()
        print(f"you have {max_guesses} guesses left to get it")

        numGuesses = 1
        while numGuesses < max_guesses:
            guess = ""
            while len(guess) != num_digits or not guess.isdecimal():
                print(f"guess #{numGuesses}")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print("No guesses left")
                print(f"The answer was {secretNum}")

        print("play again? (y/n)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for Playing!")

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "you got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Wrong"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == '__main__':
    main()
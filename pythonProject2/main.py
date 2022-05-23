#deductive logic game
import random
num_digits = 3
max_guesses = 10

def main():
    print(
        f"""Bagels, a deductive logic game
        
        I am thinking of a {num_digits} digit number with no repeated digits.
        Try and guess what it is. Here are some clues:
        
        When I say:     That means:
            Pico        One digit is correct but in the wrong position.
            Fermi       One digit is correct and in the right position.
            Bagels      No digit is correct.
            
        For example, if the secret number was 135 and your guess was 231,the clues would be  Fermi Pico. """
    )
    def getSecretNum():
        """Returns a string made up of the num_digits unique random digits"""
        numbers = list("0123456789") #create a list of digits 0 to 9.
        random.shuffle(numbers)   #shuffels them into random order.

        #get the first num_digits digits in the list for the secret number:
        secretNum = ""
        for i in range(num_digits):
            secretNum+= str(numbers[i])
        return secretNum

    while True: # Main loop.
            #this stores the secret number the player needs to guess.
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print(f"You have {max_guesses} guesses to get it.")

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ""
            #keep looping unit they enter a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

            def getClues(guess, secretNum):
                """Returns a strong with pico, fermi, bagels clue for a guess and secret number pair"""
                if guess == secretNum:
                    return "You got it!"

                clues = []

                for i in range(len(guess)):
                    if guess[i] == secretNum[i]:
                        # A correct digit in the correct place.
                        clues.append("Fermi")
                    elif guess[i] in secretNum:
                        # correct digit in an incorrect place.
                        clues.append("Pico")
                if len(clues) == 0:
                    return "bagels"  # there is no correct digit at all.
                else:
                    # sort the clues int alphabetical order so tier original order doesnt give another clue.
                    clues.sort()
                    # make a single string from the list of string clues.
                    return "".join(clues)

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #theyre correct, so break the loop.
            if numGuesses > max_guesses:
                print("You have ran out of guesses.")
                print("The answer was {}.".format(secretNum))

            #ask the player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
        print("thanks for playing!")



#if the program is run (instead of imported) run the game.
if __name__ == "__main__":
    main()






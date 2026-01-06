import random

def guess_the_word():
    words = ["good", "better", "best", "awesome", "nice"] #A list of words
    generate_word = random.choice(words) #Selecting a random word from the list

    letters = []
    number_of_turns = 10
    display_word = ['_'] * len(generate_word)

    print("Welcome to the word guessing game!")
    print(f"The word has {len(generate_word)} letters. You have {number_of_turns} turns to guess it.")
    print(" ".join(display_word))

    while number_of_turns > 0:
        guess_a_letter = input("Guess a letter: ").lower().strip() #The user needs to guess a letter

        if len(guess_a_letter) != 1 or not guess_a_letter.isalpha(): #Validate input
            print("Invalid input. Please enter a letter.")
            continue

        if guess_a_letter in letters:
            print(f"You guessed the letter '{guess_a_letter}'. Guess a different letter.")
            continue

        letters.append(guess_a_letter)

        if guess_a_letter in generate_word:
            print(f"The letter is in the word.")

            for i in range(len(generate_word)): #Check if the guessed letter is in the word or not
                if generate_word[i] == guess_a_letter:
                    display_word[i] = guess_a_letter #UUpdate the display to show the letters which were guessed correctly

        else:
            number_of_turns -= 1
            print(f"The letter {guess_a_letter} is not in the word.")
            print(f"You have {number_of_turns} turns left.")

        print(f" ".join(display_word)) #Display the progress

        if "_" not in display_word: #Check the winning condition
            print(f"\nCongratulations! You guessed the word '{generate_word}'.")
            break

    if number_of_turns == 0: #Check the losing condition
        print(f"\nGame over, You lost. The word was '{generate_word}'.")

if __name__ == "__main__":
    guess_the_word()
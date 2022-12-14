from replit import clear
import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#display logo
print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
picked = []
for _ in range(word_length):
    display += "_"

#main function
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess not in picked:
        picked += guess
    clear()
    if guess in picked:
        print(f"You have already guessed {guess}")
        
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #debugging code
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"You have guessed {' '.join(picked)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])

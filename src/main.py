import random
import os
import words

DICTIONARY = words.DICTIONARY

def randomWord():
    secret_word = random.choice(DICTIONARY)
    len_secret_word = len(secret_word)
    secret_word_lst = []

    # I need the word to be like a list
    for letter in secret_word:
        secret_word_lst.append(letter)

    gameEngine(secret_word_lst, len_secret_word)

def gameEngine(secret_word_lst, len_secret_word):

    tries = 10
    usr_word = []
    tried_letters = ""

    for i in range(len_secret_word):
        usr_word.append("_")

    while True:
        if tries == 0:
            print("Oh! You ran out of tries.")
            secret_word = ""
            for elem in secret_word_lst:
                secret_word += elem
            print(f"The correct answer was {secret_word}")
            break
        else:
            os.system('clear')
            print(f"Length --> {len_secret_word}")

            if tries > 1:
                print(f"You have {tries} tries left")
            else:
                print(f"You have {tries} try left")

            # Here I print the letters that the user has tried
            if tried_letters != "":
                print(tried_letters)

            # Here I convert the list to string and print that string
            usr_word_str = ""
            for elem in usr_word:
                usr_word_str += elem
            print(usr_word_str)

            try_word = str(input("--> "))

            # Aquí compararé el que posa l'usuari i la secret_word
            # He de comparar posició per posició les dues llistes
            for index, i in enumerate(secret_word_lst):
                for j in try_word:
                    if j == i:
                        # Here I use the number of position in usr_word to make it equal to j
                        usr_word[index] = j
                    else:
                        continue
            
            # If both lists are the same, the user wins and the loop breaks
            if usr_word == secret_word_lst:
                print(usr_word)
                print("Congratulations! YOU WON!")
                break
            elif try_word in secret_word_lst:
                continue
            else:
                tries -= 1
                if tried_letters == "":
                    tried_letters += try_word
                else:
                    tried_letters += f", {try_word}"

def main():
    randomWord()

if __name__ == "__main__":
    main()

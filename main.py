import random
import os
import sys
import words

class Utils:
    @staticmethod
    def clear_screen():
        try:
            os.system("clear")
        except Exception:
            os.system("cls")
        except Exception as e:
            print(f"Error clearing screen: {e}")

class Word:
    def __init__(self):
        self.DICTIONARY = words.DICTIONARY

    def get_random_word(self):
        try:
            secret_word = random.choice(self.DICTIONARY)
            len_secret_word = len(secret_word)
            secret_word_lst = []

            # I need the word to be like a list
            for letter in secret_word:
                secret_word_lst.append(letter)

            return secret_word_lst, len_secret_word
        except Exception as e:
            print(f"Error generating random word: {e}")

    @staticmethod
    def get_tries(aLen:int) -> int:
        try:
            num_tries = aLen * 1.8
            # return round(num_tries,0)
            return int(num_tries)
        except Exception as e:
            print(f"Error getting tries: {e}")

    @staticmethod
    def list_to_string(aLst:list) -> str:
        try:
            aStr = ""
            for i in aLst:
                aStr += i
            return aStr
        except Exception as e:
            print(f"Error converting list to string: {e}")

    @staticmethod
    def out_of_tries(aLst):
        try:
            print("Oh! You ran out of tries.")
            secret_word = ""
            for elem in aLst:
                secret_word += elem
            print(f"The correct answer was {secret_word}")

            sys.exit()
        except Exception as e:
            print(f"Error in out_of_tries function: {e}")
            sys.exit()

    @staticmethod
    def print_tries_left(num_tries:int):
        try:
            if num_tries > 1: print(f"You have {num_tries} tries left")
            else: print(f"You have {num_tries} try left")
        except Exception as e:
            print(f"Error printing tries left: {e}")

    @staticmethod
    def print_length_word(aLength:int):
        try:
            print(f"Length --> {aLength}")
        except Exception as e:
            print(f"Error printing the length of the word: {e}")

    @staticmethod
    def print_tried_letters(letters:str):
        try:
            # Here I print the letters that the user has tried
            if letters != "":
                print(letters)
        except Exception as e:
            print(f"Error printing tried letters: {e}")

    @staticmethod
    def get_usr_try_word() -> str:
        try:
            usr_try = str(input("\n--> "))
            return usr_try
        except Exception as e:
            print(f"Error getting the user's try word: {e}")

    @staticmethod
    def compare_usr_secret(aLst:list,aWrd:list,aTry:str):
        try:
            for index, i in enumerate(aLst):
                for j in aTry:
                    if j == i:
                        # Here I use the number of position in usr_word to make it equal to j
                        aWrd[index] = j
                    else:
                        continue
                    
            return aWrd
        except Exception as e:
            print(f"Error comparing user's input with secret word: {e}")

    @staticmethod
    def win(aStr):
        try:
            Utils.clear_screen()
            print(aStr)
            print("Congratulations! YOU WON!")
        except Exception as e:
            print(f"Error in win function: {e}")

    @staticmethod
    def not_win(num_tries,letters,aWrd):
        try:
            num_tries -= 1
            if letters == "":
                letters += aWrd
            else:
                letters += f", {aWrd}"

            return num_tries,letters
        except Exception as e:
            print(f"Error in not_win function: {e}")

if __name__ == "__main__":
    secret_word_lst, len_secret_word =  Word.get_random_word()
    tries = Word.get_tries(len_secret_word)

    usr_word = []
    tried_letters = ""

    for i in range(len_secret_word):
        usr_word.append("_")

    while True:
        if tries == 0:
            Word.out_of_tries(secret_word_lst)
        else:
            Utils.clear_screen()
            Word.print_length_word(len_secret_word)
            Word.print_tries_left(tries)
            Word.print_tried_letters(tried_letters)
            usr_word_str = Word.list_to_string(usr_word)
            print(f"\n{usr_word_str}")
            try_word = Word.get_usr_try_word()

            usr_word = Word.compare_usr_secret(secret_word_lst,usr_word,try_word)
            
            # If both lists are the same, the user wins and the loop breaks
            if usr_word == secret_word_lst:
                Word.win(Word.list_to_string(secret_word_lst))
                break
            elif try_word in secret_word_lst:
                continue
            else:
                tries, tried_letters = Word.not_win(tries,tried_letters,try_word)

    sys.exit()

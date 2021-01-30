# Write your code here
import random

print("H A N G M A N")
print("")
my_list = ['python', 'java', 'kotlin', 'javascript']
answer = my_list[random.randint(0, 3)]
answer1 = list(answer)
word = list("-" * len(answer))
lives = 8
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_input = ""
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "exit":
        break
    if menu == "play":
        print("")
        while True:
            print("".join(word))
            if "-" not in word:
                print("You guessed the word!")
                print("You survived!")
                break
            else:
                letter = input("Input a letter: ")
                if letter in letter_input:
                    print("You've already guessed this letter")
                    print("")
                    continue
                if len(letter) > 1 or letter == " ":
                    print("You should input a single letter")
                    print("")
                    continue
                if letter not in alphabet:
                    print("Please enter a lowercase English letter")
                    print("")
                    continue
                letter_input += letter
                if letter in answer1 and letter not in word:
                    for i in range(0, len(word)):
                        if letter == answer1[i]:
                            word[i] = letter
                #    elif letter in word:
                #   print("No improvements")
                #    lives -= 1
                else:
                    print("That letter doesn't appear in the word")
                    lives -= 1
            if lives == 0:
                print("You lost!")
                break
            print("")

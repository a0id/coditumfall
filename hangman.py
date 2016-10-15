import random
def wordState():
    for x in range(len(word)):
        print()
print("Welcome to hangman. Theme: greetings!")
chosenLetters = []
words = ["hello", "hey", "hi", "konichiwa"]
hangman = 0
word = words[random.randint(0,3)]
print("The word has been chosen.")
while True:
    letter = input("Enter a letter: ")
    chosenLetters.append(letter)
    if letter in word:
        print("There are "+str(word.count(letter))+" "+letter.upper()+"s in the word.")
    else:
        hangman+=1
        print("Your hangman lost a limb! He has "+str(hangman)+"/4 limbs left!")
import re
def remove_symbol(word):
    return re.sub(r'[^a-zA-Z]', '', word)
def isVowel(word):
    first_letter = word[0].lower()
    return first_letter in "aeiou"
def FirstVowelPos(word):
    for i, letter in enumerate(word):
        if isVowel(letter):
            return i
    return -1
def GetPigLatin(word):
    vowel_pos = FirstVowelPos(word)
    if vowel_pos == 0:
        return word + "yay"
    else:
        return word[vowel_pos::] + word[0:vowel_pos] + "ay"

start = input("Enter c to continue to Pig Latin translator, enter q to quit: ")
while start.lower() !='q':
    if start.lower() =='c':
        word = input("Enter a word, or enter q to quit: ")
        if word.lower() != 'q':
            print("Your word in Pig Latin is:", GetPigLatin(remove_symbol(word)))
        if word.lower() =='q':
            break


    else:
        print("Invalid entry.")
        start = input("Enter c to continue to translator, enter q to quit")

print("Thank you for using translator!")
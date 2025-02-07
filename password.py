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
def GetPigSentence(word):
    words = word.split()
    multiple_words = []
    vowels_pos = FirstVowelPos(word)
    for word in words:
        if vowels_pos == 0:
            return multiple_words.append(str(word + "ay"))
        else:
            return multiple_words.append(str(word[vowels_pos::] + word[0:vowels_pos] + "ay"))

    return ' '.join(multiple_words)

start = input("Enter j to continue to translator, enter q to quit: ")
while start !='q':
    if start =='j':
        word = input("Enter a word, or enter q to quit: ")
        if word != 'q':
            # word = input("Enter a word: ")
            print("Your word in Pig Latin is:", GetPigLatin(remove_symbol(word)))
        if word =='q':
            break
    if start == 't':
        words = input("Enter a sentence: ")
        print("Your sentence in Piglatin is:\n" + GetPigSentence(remove_symbol(words)))

    else:
        print("Invalid entry.")
        start = input("Enter j to continue to translator, enter q to quit")

print("Thank you for using translator!")
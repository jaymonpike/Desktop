import re
start = input("Enter j to continue to translator, enter q to quit: ")
while start !='q':
    if start =='j':
        # word = input("Enter a word: ")
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
        def remove_symbol(word):
            return re.sub(r'[^a-zA-Z]', '', word)

        while word != 'q':
            if word == 'q':
                break
            else:
                word = input("Enter a word: ")
            # result = remove_symbol(word)
            # if word =='q':
                # print("Thank you for using the Pig Latin translator.")
                # break
            # if word != 'q':
            print("Your word in Pig Latin is:",GetPigLatin(word))

        print("gg")
    else:
        print("Invalid entry")
        start = input("Enter j to continue to translator, or q to quit: ")



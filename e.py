import re
def remove_symbol(word):
    return re.sub(r'[^a-zA-Z]', '', word)
def isVowel(word):
    first_letter = word[0].lower()
    return first_letter in 'aeiou'
def FirstVowelPos(word):
    for i, letter in enumerate(word):
        if isVowel(letter):
            return i
    return -1
def getpigsent(text):
    sprit = text.split()
    whole_sent = []
    for word in sprit:
        vowel_pos = FirstVowelPos(word)
        if vowel_pos == 0:
            pigword = remove_symbol(word + 'yay')
        else:
            pigword = remove_symbol(word[vowel_pos::] + word[0:vowel_pos] + 'ay')
        whole_sent.append(pigword)
    return ' '.join(whole_sent)

sentence = input("enter a sentence: ")
get_sentence = getpigsent(sentence)
print(get_sentence)
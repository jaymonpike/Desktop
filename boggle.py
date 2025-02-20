import random
print("Welcome to Boggle!")
alph_dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 
                   13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
grid = [[alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)]], 
        [alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)]], 
        [alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)]], 
        [alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)]], 
        [alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)], alph_dictionary[random.randint(1,26)]]]
for r in grid:
    for c in r:
      print (c, end = " ")
    print()
def get_score(user_input):
    score = 0
    for letter in user_input:
        if letter in 'aelnorstu':
            score += 1
        elif letter in 'dg':
            score += 2
        elif letter in 'bcmp':
            score += 3
        elif letter in 'fhvwy':
            score +=4
        elif letter == 'k':
            score += 5
        elif letter in 'jx':
            score += 8
        elif letter in 'qz':
            score += 10
    return score
play = input("Enter p to play, or enter q to exit: ").lower()
total = []
while play != 'q':
    if play == 'p':
        user_word = input("Enter a word you see, or enter q to quit: ").lower()
        user_split = list(user_word)
        user_score = get_score(user_split)
        if user_word == 'q':
            break
        print("Your score: ", user_score)
        total.append(user_score)
    elif play == 'q':
        print("Have a great day!")
        break
    else:
        print("Invalid entry.")
        play = input("Enter p to play, or enter q to exit: ")
if sum(total) != 0:
    print("Total score: ", sum(total))
print("Have a great day!")

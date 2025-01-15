baseline = 0

print("Does your password contain...")
nine_char = input("at least 9 characters in length? y/n")
if nine_char == 'y' or nine_char == 'Y':
    baseline += 1
elif nine_char == 'n' or nine_char == 'N':
    baseline += 0
mix_let_numb = input("a mixture of letters and numbers? y/n")
if mix_let_numb == 'y' or mix_let_numb == 'Y':
    baseline += 1
elif mix_let_numb == 'n' or mix_let_numb == 'N':
    baseline += 0
mix_up_low = input("a mixture of uppercase and lowercase letters? y/n")
if mix_up_low == 'y' or mix_up_low == 'Y':
    baseline += 1
elif mix_up_low == 'n' or mix_up_low == 'N':
    baseline += 0
symbol = input("at least one symbol? y/n")
if symbol == 'y' or symbol == 'Y':
    baseline += 1
elif symbol == 'n' or symbol == 'N':
    baseline += 0

if baseline <=1:
    print("Your password is very weak.")
elif baseline == 2:
    print("Your password is weak.")
elif baseline == 3:
    print("Your password is strong")
elif baseline == 4:
    print("Your password is very strong.")
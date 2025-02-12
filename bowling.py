play = 0
while play != '2':
    play = input("Enter 1 to use bowling calculator, or enter 2 to quit: ")
    if play == '1':
        def GetScore(rolls):
            score = 0
            index_frame = 0
            frame = 0
            while frame != 10:
                for number in range(10):
                    if rolls[index_frame] == 10:
                        score += 10 + rolls[index_frame + 1] + rolls[index_frame + 2]
                        index_frame += 1
                        frame += 1
                        print("Your score for round", frame, "is:", {score})
                    elif rolls[index_frame] + rolls[index_frame + 1] == 10:
                        score += 10 + rolls[index_frame + 2]
                        index_frame += 2
                        frame += 1
                        print("Your score for round", frame, "is:", {score})
                    else:
                        score += rolls[index_frame] + rolls[index_frame + 1]
                        index_frame += 2
                        frame += 1
                        print("Your score for round", frame, "is:", {score})
            return score
        user_score = input("Enter your scores for each throw separated by commas: ").split(",")
        int_user_score = [int(x) for x in user_score]
        print(" Your total score is : ", GetScore(int_user_score))
    elif play == '2':
        break
    else:
        print("Invalid entry")
        play = input("Enter 1 to use bowling calculator, or enter 2 to quit: ").lower()

print("Have a nice day!")
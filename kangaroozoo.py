num = 0

while num !=2:
    answer = 0
    three_cost = 6
    adult_cost = 12
    ffp_cost = 85
    threeffp_cost = 50
    num = int(input("Welcome to the Kangaroo Zoo Cost Estimator. Choose an option: \n1. Estimate cost \n2. Quit \nEntered Choice: "))
    if num ==1:
        under_three = int(input("How many guests are 3 and under? "))
        adults = int(input("How many adults will be jumping? "))
        three_cost *= under_three
        adult_cost *= adults
        ffp = input("Would you like to purchase any Frequent Flopper Passes? y/n ")
        if ffp == 'y' or  ffp == 'Y':
            ffp_adult = int(input("How many adult Frequent Flopper passes would you like? "))
            ffp_underthree = int(input("How many Frequent Flopper Passes will be for children under 3? "))
            ffp_cost *= ffp_adult
            threeffp_cost *= ffp_underthree
        if ffp == 'n' or ffp == 'N':
            ffp_cost = 0
            threeffp_cost = 0

        subtotal = (three_cost + adult_cost + ffp_cost + threeffp_cost)
        print("Subtotal: $" + str(subtotal))
        tax = ((three_cost + adult_cost + ffp_cost + threeffp_cost) * 0.08)
        print("Tax: $" + str(tax))
        print("Total: $" + str(subtotal + tax))
        tip = int(input("Tip amount in dollars: $"))
        while tip <0:
            print("Tip cannot be negative, nice try.")
            tip = int(input("Tip amount in dollars: $"))
        print("New total: $" + str(subtotal + tax + tip),"\nThank you!\n")

    else:
        if num !=2:
            print(num, "is an invalid option.\nEnter a valid option:\n")

print("Have a nice day!\n")
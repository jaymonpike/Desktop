num = int(input("Enter a multiple of 3. Enter 0 to stop when you are confident in your score."))
correct = 0
attempts = 0
x_of_three = True

while num != 0:
  if num % 3 == 0:
    x_of_three = True
  if num % 3 != 0:
    x_of_three = False
  if x_of_three:
    correct += 1
    attempts += 1
    print(num, "is a multiple of 3.")
  else:
    correct +=0
    attempts +=1
    print(num, "is not a multiple of 3. Try again.")

  num = int(input("Enter a multiple of 3. Enter 0 to stop."))

print("Your score is: " + str(correct) + "/" + str(attempts))
if (correct/attempts) == 1:
  print("Perfect!")
elif (correct/attempts) >=0.90:
  print("Excellent work!")
elif (correct/attempts) >=0.80:
  print("Good work.")
elif (correct/attempts) >=0.61:
  print("Could use some work.")
elif (correct/attempts) <=0.60:
  print("Restart the activity please.")
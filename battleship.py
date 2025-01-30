import random
import math

x_position = random.randint(1, 10)
y_position = random.randint(1, 10)
attempts = 0
guess_x = int(input("Enter a position for the X axis: "))
guess_y = int(input("Enter a position for the Y axis: "))


while attempts != 9:
    distance = float(math.sqrt(((x_position - guess_x) ** 2) + ((y_position - guess_y) ** 2)))
    attempts +=1
    print("Miss. Shot was ", round(distance, 2), "meters away. ", str(10 - attempts), "shots remain.")
    guess_x = int(input("Enter a position for the X axis: "))
    guess_y = int(input("Enter a position for the Y axis: "))
    if x_position == guess_x and y_position == guess_y:
        attempts = 9
        print("Hit!")

print("The coordinates were: ", "(" + str(x_position) + " , " + str(y_position) + ")")
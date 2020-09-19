# Calculate the pi from uniform distribution
import math
import random

def estimate_pi(num):
    pi = 0
    circle_points = 0
    square_points = 0
    for i in range(num):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if (math.sqrt((x**2 + y**2)) <= 1):
            circle_points += 1
            square_points += 1
        else:
            square_points += 1

    pi = 4 * circle_points / square_points

    return pi

print(estimate_pi(1000000))
# What does this piece of code do?
# Answer: This script computes the sum of 11 randomly generated integers, 
# each independently sampled from the inclusive range 1 to 10. 
# A while loop runs exactly 11 times (from progress=0 to progress=10), 
# and in each iteration, a new random integer is added to a running total. 
# The final accumulated sum is then printed. 
# Note: although the ceil function is imported, it is never used.

# Import libraries
from random import randint
from math import ceil

total_rand = 0
progress = 0      


# Loop runs while progress is at most 10 → total of 11 iterations
while progress <= 10:
    progress += 1
    n = randint(1, 10)
    total_rand += n

print(total_rand)
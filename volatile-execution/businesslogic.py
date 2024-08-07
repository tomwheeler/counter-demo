# Specify that this program uses Python's pre-defined "sleep" function,
# which allows our program to pause execution for a specified duration.
from time import sleep


# Define a function that counts from 1 to a specified limit.
# It displays the current number, increments it, and then pauses
# for 1 second before continuing. This is the "business logic"
def count_to(limit):
    number = 1
    while number <= limit:
        print(number)
        number = number + 1
        sleep(1)

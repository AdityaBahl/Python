"""
this program
Write a python Program which does the following:
    1.Asks user to enter a range i.e. value of Low and High
    2.Randomly assigns a number in the given range[low to high]
    3.Asks user to guess a number in the given range.
    4.Checks if number entered by user is correct guess or not.
    5.Provides a hint to user whether number entered by him is lower or higher than actual number.
    6.Keeps asking user for number until her guesses the correct number if accepts his defeat.
"""
"""
if written: from random import random
then no need to write random.random
"""
import random
low, high = int(input('Enter Lower Limit ')), int(input('Enter Higher Limit '))
print(low, high)
secret = low+int(random.random()*(high-low+1))
"""print(secret)"""
ch = "yes"
count = 5
while ch != "no":
    user = int(input('Enter number for guess '))
    if user == secret:
        print('Correct!! You found the magic number --> ', secret)
        break
    elif user < secret:
        print('Your Number is smaller than the magic number')

    else:
        print('Your Number is greater than the magic number')
    count = count-1
    if count < 1:
        print('No chances left, You Lost!, The magical number was', secret)
        break
    print("Wanna Try Again?(yes/no)", count, "chances left!")
    ch = input()

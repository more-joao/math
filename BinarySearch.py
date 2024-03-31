from random import randint
from math import floor

numbers = []
counter = 0
loop_ended = False

while counter < 30:
    new_num = randint(1, 200)
    if new_num in numbers:
        pass
    else:
        numbers.append(new_num)
        counter += 1
numbers.sort()
print(numbers)

x = int(input("Type a number: "))
lowest, highest = 0, len(numbers) - 1
mid = floor((lowest + highest) / 2)
print(f"First mid: {mid}")

while loop_ended == False:
    if x == numbers[mid]:
        print(f"Number found. Index: {numbers.index(x)}")
        loop_ended = True
    elif x not in numbers:
        print("Number not in list.")
        loop_ended = True
    elif x < numbers[mid]:
        highest = mid - 1
        mid = floor((lowest + highest) / 2)
        print(f"Lower - Mid: {mid}")
    elif x > numbers[mid]:
        lowest = mid + 1
        mid = floor((lowest + highest) / 2)
        print(f"Higher - Mid: {mid}")
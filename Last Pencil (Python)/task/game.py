import random

num_of_pencils = input("How many pencils would you like to use:\n")
while not num_of_pencils.isnumeric():
    print('The number of pencils should be numeric')
    num_of_pencils = input()
num_of_pencils = int(num_of_pencils)

while num_of_pencils < 1:
    print("The number of pencils should be positive")
    try:
        num_of_pencils = int(input())
    except ValueError:
        print('The number of pencils should be numeric')

first = input("Who will be first (John, Jack)\n")
while first != 'John' and first != 'Jack':
    print("Choose between \'John\' and \'Jack\'")
    first = input()

while num_of_pencils > 0:
    print('|' * num_of_pencils)
    print(f"{first}'s turn:")
    if first == "John":
        pencils_taken = input()
        if pencils_taken in ('1', '2', '3'):
            pencils_taken = int(pencils_taken)
            if num_of_pencils - pencils_taken < 0:
                print("Too many pencils were taken")
                continue
            else:
                num_of_pencils -= pencils_taken
        else:
            print("Possible values '1', '2' or '3'")
            continue

    # bot choice strategy
    if first == "Jack":
        if num_of_pencils in range(4, num_of_pencils + 1, 4):
            num_of_pencils -= 3
            print(3)
        elif num_of_pencils in range(3, num_of_pencils + 1, 4):
            num_of_pencils -= 2
            print(2)
        elif num_of_pencils in range(2, num_of_pencils + 1, 4):
            num_of_pencils -= 1
            print(1)
        elif num_of_pencils == 1:
            num_of_pencils -= 1
            print(1)
        else:
            random_pencils = random.randint(1, 3)
            num_of_pencils -= random_pencils
            print(random_pencils)

    # change current player
    if first == "John":
        first = "Jack"
    else:
        first = "John"

print(f"{first} won!")

import random
opinion=True
while True:
    print("Let's start the dice_roll game:")
    print("loading.....")
    player1=print(random.randint(1, 6))
    player2=print(random.randint(1, 6))
    another_roll=input("want to roll the dice again:?")
    if another_roll=="yes":
        continue
    else:
        break

import random
import math
def take_away():
    objects = 21
    computer_turn = True
    while objects > 0:
        if computer_turn:
            for i in range(1, 4):
                if ((objects - i) % 4) == 0:
                    computer = i
            print(f"{objects} objects remain, I'll take {computer}")
            objects -= computer
            computer_turn = False
        else:
            player = 0
            player = input(f"{objects} objects remain, choose 1, 2, or, 3: ")
            while (player != "1") and (player != "2") and (player != "3"):
                print("Invalid choice, please try again")
                player = input(f"{objects} objects remain, choose 1, 2, or, 3: ")
            objects -= int(player)
            computer_turn = True


    if computer_turn:
        print("You win!")
    else:
        print("I win!")



if __name__ == "__main__":
    take_away()
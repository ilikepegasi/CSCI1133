import random
def main():
    target = random.randint(1, 10)
    guess = int(input("Enter an integer: "))
    if target > guess:
        print("Too high")
    elif target < guess:
        print("Too low")
    else:
        print("Equal")
    print(f"The target was {target}")      
        
main()
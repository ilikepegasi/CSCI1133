def main():
    dollars = int(input("Enter dollars: "))
    cents = int(input("Enter cents: "))
    dimes = 0
    nickels = 0
    pennies = 0
    quarters = cents // 25
    dimes = (cents - quarters * 25) // 10
    nickels = (cents - quarters * 25 - dimes * 10) // 5
    pennies  = cents % 5
    print(f"Quarters {quarters}, Dimes {dimes}, Nickels {nickels}, Pennies {pennies}")
if __name__ == "__main__":
    main()
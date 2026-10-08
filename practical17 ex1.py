import secrets

def roll_dice():
    print("=== Multi-Dice Rolling Simulator ===")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))

        
            if num_dice < 1:
                print("Please enter at least 1 die.")
            elif num_dice > 1000:
                print("Please enter no more than 1000 dice.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    
    rolls = [secrets.randbelow(6) + 1 for _ in range(num_dice)]

    total = sum(rolls)

    print("\nResults:")
    for i, result in enumerate(rolls, start=1):
        print(f"Die {i}: {result}")

    print(f"\nTotal score: {total}")


if __name__ == "__main__":
    roll_dice()
#Loop
    #Dice Rolling Game and Bet on Odd or Even
    #Ask: Roll the dice? (Y/N)
    #If Y: Roll the dice 
    #Ask: Place your bet Odd or Even? (O/E)
    #Show the result of the dice roll and total
    #Check if the user's bet matches the result
    #If N: Exit the game

import random
def roll_dice():
    return random.randint(1, 6), random.randint(1,6), random.randint(1,6)

def main():
    print("Welcome to the Dice Rolling Game!")
    while True:
        roll = input("Roll the dice? (Y/N): ").strip().upper()
        if roll == 'Y':
            dice1, dice2, dice3 = roll_dice()
            total = dice1 + dice2 + dice3
            bet = input("Place your bet Odd or Even? (O/E): ").strip().lower()
            if bet not in ['o', 'e']:
                print("Invalid bet. Please choose 'O'(Odd) or 'E'(Even).")
                continue
            print(f"You rolled: {dice1}, {dice2}, {dice3}. Total: {total}")
            if total % 2 == 0:
                actual_result = 'even'
            else:
                actual_result = 'odd'

            if bet == actual_result:
                print("Congratulations! You win!")
            else:
                print("Sorry, you lose.")
        elif roll == 'N':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue

   

if __name__ == "__main__":
    main()
import random 
#Generate computer's choice randomly
def get_computer_choice():
    return random.choice(['r', 'p', 's'])

#Logic to determine the winner
def who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
        return print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
         return print("You win! Congratulations!")
    else: 
        return print("You lose! Better luck next time.")
    
#Loop 
#Structure of the game
def main():
    print("Welcome to the Rock Paper Scissors Game!")
    while True:   
        user_choice = input("Enter your choice (r/p/s) or type 'quit' to quit:").strip().lower()
        #TH1: Quit
        if user_choice == 'quit':
            print("Thank you for playing! Goodbye!")
            break
        #TH2: Invalid choice
        elif user_choice not in ['r', 'p', 's']:
            print("Invalid choice.")
            continue
        #TH3: Valid choice
        computer_choice = get_computer_choice()
        choice_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}  #if chose r/p/s, print rock/paper/scissors
        user_choice = choice_dict[user_choice]
        computer_choice = choice_dict[computer_choice]
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        who_wins(user_choice, computer_choice)
        #Ask to play again
        play_again = input("Do you want to play again? (Y/N):").strip().upper()
        if play_again != 'Y':
            print("Thank you for playing! Goodbye!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()

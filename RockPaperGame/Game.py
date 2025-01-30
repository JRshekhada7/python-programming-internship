import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_round(self):
        print("\nChoose: Rock, Paper, or Scissors")
        user_choice = input("Your choice: ").lower()


        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please select Rock, Paper, or Scissors.")
            return None

        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")

    
        result = self.determine_winner(user_choice, computer_choice)
        print(result)
        print(f"Scores - You: {self.user_score} | Computer: {self.computer_score}")

    def play_game(self):
        while True:
            self.play_round()

        
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("\nThanks for playing!")
                break



if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    game = RockPaperScissorsGame()
    game.play_game()


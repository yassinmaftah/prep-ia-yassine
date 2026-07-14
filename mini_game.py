import random
import time


def display_banner():
    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)


def get_difficulty():
    print("\nChoose difficulty:")
    print("  1. Easy   (1-50,  10 attempts)")
    print("  2. Medium (1-100,  7 attempts)")
    print("  3. Hard   (1-200,  5 attempts)")

    levels = {"1": (50, 10), "2": (100, 7), "3": (200, 5)}
    while True:
        choice = input("\nEnter 1, 2 or 3: ").strip()
        if choice in levels:
            return levels[choice]
        print("Invalid choice. Please enter 1, 2 or 3.")


def get_guess(max_number: int) -> int:
    while True:
        try:
            guess = int(input(f"Your guess (1-{max_number}): "))
            if 1 <= guess <= max_number:
                return guess
            print(f"Please enter a number between 1 and {max_number}.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def give_hint(guess: int, secret: int, attempts_left: int):
    diff = abs(guess - secret)

    if diff == 0:
        return  # handled by caller

    direction = "higher" if guess < secret else "lower"

    if diff <= 5:
        warmth = "Very hot!"
    elif diff <= 15:
        warmth = "Hot!"
    elif diff <= 30:
        warmth = "Warm."
    else:
        warmth = "Cold..."

    print(f"  {warmth} Go {direction}. ({attempts_left} attempt(s) left)")


def play_round(max_number: int, max_attempts: int) -> bool:
    secret = random.randint(1, max_number)
    attempts_used = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        guess = get_guess(max_number)
        attempts_used += 1

        if guess == secret:
            elapsed = time.time()  # used symbolically; real timer set below
            print(f"\n  Correct! The number was {secret}.")
            print(f"  You got it in {attempts_used} attempt(s).")
            return True

        give_hint(guess, secret, attempts_left - 1)

    print(f"\n  Out of attempts! The number was {secret}.")
    return False


def show_score(wins: int, losses: int):
    total = wins + losses
    ratio = (wins / total * 100) if total else 0
    print(f"\n  Score: {wins}W / {losses}L  ({ratio:.0f}% win rate)")


def main():
    display_banner()
    wins = 0
    losses = 0

    while True:
        max_number, max_attempts = get_difficulty()

        start = time.time()
        won = play_round(max_number, max_attempts)
        elapsed = time.time() - start

        if won:
            wins += 1
            print(f"  Time: {elapsed:.1f}s")
        else:
            losses += 1

        show_score(wins, losses)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Bulls and Cows
- Secret: 4 distinct digits chosen from 1..9
- Player guesses until they find the secret
- Input validation rejects malformed guesses
- After each guess print "<bulls> bull(s), <cows> cow(s)"
"""

import random
import sys

def make_secret() -> str:
    # choose 4 distinct digits from 1..9
    digits = random.sample([str(d) for d in range(1, 10)], 4)
    return "".join(digits)

def validate_guess(guess: str) -> (bool, str):
    if guess.lower() == "quit":
        return True, "quit"
    if len(guess) != 4:
        return False, "Guess must be exactly 4 digits."
    if not guess.isdigit():
        return False, "Guess must contain only digits 1-9."
    if any(ch == '0' for ch in guess):
        return False, "Digits must be between 1 and 9 (no 0)."
    if len(set(guess)) != 4:
        return False, "Digits must not repeat."
    return True, ""

def score_guess(secret: str, guess: str) -> (int, int):
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    # cows = common digits minus bulls
    common = sum(min(secret.count(d), guess.count(d)) for d in set(guess))
    cows = common - bulls
    return bulls, cows

def main():
    secret = make_secret()
    # Uncomment the next line to see the secret while testing:
    # print(f"[DEBUG] secret = {secret}")
    print("Welcome to Bulls and Cows! Guess the 4-digit secret (digits 1-9, no repeats).")
    print("Type 'quit' to exit.\n")

    attempts = 0
    while True:
        attempts += 1
        guess = input(f"Guess #{attempts}: ").strip()
        valid, msg = validate_guess(guess)
        if not valid:
            print("Invalid guess:", msg)
            attempts -= 1  # don't count malformed attempts
            continue
        if msg == "quit":
            print("Goodbye!")
            sys.exit(0)

        bulls, cows = score_guess(secret, guess)
        if bulls == 4:
            print(f"Correct! You found the secret {secret} in {attempts} valid guesses. 🎉")
            break
        else:
            print(f"{bulls} bull(s), {cows} cow(s)\n")

if __name__ == "__main__":
    main()

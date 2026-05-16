#!/usr/bin/env python3
"""Mini jeu : Devine le mot (pendu simplifié)."""

import random

WORDS = [
    "python",
    "dragon",
    "clavier",
    "nuage",
    "algorithme",
    "aventure",
    "galaxie",
    "pixel",
]

MAX_ERRORS = 7


def mask_word(word: str, guessed: set[str]) -> str:
    return " ".join(letter if letter in guessed else "_" for letter in word)


def choose_word() -> str:
    return random.choice(WORDS)


def play() -> None:
    print("🎮 Bienvenue dans 'Devine le mot' !")
    print(f"Tu as droit à {MAX_ERRORS} erreurs.\n")

    secret = choose_word()
    guessed: set[str] = set()
    errors = 0

    while errors < MAX_ERRORS:
        current = mask_word(secret, guessed)
        print(f"Mot : {current}")
        print(f"Lettres proposées : {' '.join(sorted(guessed)) or '(aucune)'}")
        print(f"Erreurs : {errors}/{MAX_ERRORS}")

        attempt = input("Propose une lettre : ").strip().lower()
        if len(attempt) != 1 or not attempt.isalpha():
            print("⚠️ Entre une seule lettre (a-z).\n")
            continue

        if attempt in guessed:
            print("Tu as déjà proposé cette lettre.\n")
            continue

        guessed.add(attempt)

        if attempt in secret:
            print("✅ Bien joué !\n")
            if all(letter in guessed for letter in secret):
                print(f"🏆 Victoire ! Le mot était : {secret}")
                return
        else:
            errors += 1
            print("❌ Raté !\n")

    print(f"💥 Perdu ! Le mot était : {secret}")


if __name__ == "__main__":
    play()

import random as r

hints = ["Fermi", "Pico", "Bagels"]


def bagels_game(test: bool = False) -> None:
    print(
        """Bagels, a deductive logic game.
By Martin Ivanoski macohiho@gmail.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico\tOne digit is correct but in the wrong position.
 Fermi\tOne digit is correct and in the right position.
 Bagels\tNo digit is correct.
I have thought up a number.
 You have 10 guesses to get it."""
    )
    keep_playing = ""
    while keep_playing.lower() != "no":
        secret_number = str(r.randint(100, 999))
        if test == True:
            print(secret_number)
        for i in range(1, 11):
            number_guessed = ""
            while len(number_guessed) != 3:
                number_guessed = input(f"Guess #{i}\n> ")

            if secret_number == number_guessed:
                print("You got it!")
                break
            elif (
                secret_number[0] == number_guessed[0]
                or secret_number[1] == number_guessed[1]
                or secret_number[2] == number_guessed[2]
            ):
                print(hints[0])
            elif any((num in secret_number) for num in number_guessed):
                print(hints[1])
            else:
                print(hints[2])

            if i == 10:
                print(f"The secreate number is: {secret_number}")

        keep_playing = input("Do you want to play again? (yes or no)\n> ")

    print("Thanks for playing.")


def main() -> None:
    bagels_game()


if __name__ == "__main__":
    main()

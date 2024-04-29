import datetime as dt
import random


def date_generator():
    while True:
        yield dt.datetime(2024, random.randint(1, 12), random.randint(1, 29)).strftime(
            "%b %d"
        )


generate_date = date_generator()


def generate_dates(number_of_dates: int) -> None:
    birthday_dates = []
    paradox_dates = []
    for _ in range(number_of_dates):
        date = next(generate_date)
        if date in birthday_dates:
            paradox_dates.append(date)
        birthday_dates.append(date)
    print(", ".join(birthday_dates))
    if len(paradox_dates) > 0:
        print(
            f"\nIn this simulation, multiple people have a birthday on {'dates' if len(paradox_dates) > 1 else 'date'} {', '.join(paradox_dates) if len(paradox_dates) > 1 else paradox_dates[0]}"
        )


def birthday_paradox(number_of_dates: int) -> bool:
    dates = set()
    for _ in range(number_of_dates):
        new_date = next(generate_date)
        if new_date in dates:
            return True
        dates.add(new_date)
    return False


def birthday_paradox_simulation(
    number_of_dates: int, number_of_simulations: int
) -> None:
    print(
        f"Generating {number_of_dates} random birthdays {number_of_simulations} times..."
    )
    input("Press Enter to begin...")
    print(f"Let's run another {number_of_simulations} simulations.")
    count = 0
    for simulation in range(number_of_simulations + 1):
        if simulation % 10000 == 0:
            print(f"{simulation} simulations run...")
        count += 1 if birthday_paradox(number_of_dates) else 0

    print(
        f"""Out of {number_of_simulations} simulations of 23 people, there was a
matching birthday in that group {count} times. This means
that {number_of_dates} people have a {round((count / number_of_simulations) * 100, 2)} % chance of
having a matching birthday in their group.
That's probably more than you would think!"""
    )


def main():
    print("""Birthday Paradox, by Martin Ivanoski macohiho@gmail.com""")
    while True:
        try:
            number_of_dates = int(
                input("How many birthdays shall I generate? (Max 100)\n> ")
            )
            if number_of_dates > 0 and number_of_dates <= 100:
                break
            else:
                print("Please enter a value numeric value between 1 and 100 inclusive.")
        except:
            print("Please enter a value numeric value")
            continue
    generate_dates(number_of_dates)

    birthday_paradox_simulation(
        number_of_dates=number_of_dates, number_of_simulations=100000
    )


if __name__ == "__main__":
    main()

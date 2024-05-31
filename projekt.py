import random
import math

def number_guessing_game():
    # Pobieranie zakresu od użytkownika
    lower = int(input("Podaj dolną granicę: "))
    upper = int(input("Podaj górną granicę: "))

    # Generowanie losowej liczby w podanym zakresie
    x = random.randint(lower, upper)
    print(f"\n\tMasz {round(math.log(upper - lower + 1, 2))} szans, aby zgadnąć liczbę!\n")

    # Inicjalizacja liczby prób
    count = 0
    previous_guess = None

    # Obliczanie maksymalnej liczby prób
    max_guesses = math.log(upper - lower + 1, 2)

    while count < max_guesses:
        count += 1

        # Pobieranie liczby od użytkownika
        guess = int(input("Zgadnij liczbę: "))

        # Sprawdzanie poprawności zgadnięcia
        if guess == x:
            print(f"Gratulacje, zgadłeś za {count} razem!")
            break
        else:
            # Sprawdzanie różnicy między zgadywaną liczbą a wylosowaną liczbą
            if previous_guess is not None:
                if abs(x - guess) < abs(x - previous_guess):
                    print("Ciepło!")
                else:
                    print("Zimno!")
            else:
                if guess < x:
                    print("Zimno! (liczba jest większa)")
                else:
                    print("Zimno! (liczba jest mniejsza)")
            previous_guess = guess

    # Jeśli liczba prób została przekroczona
    if count >= max_guesses:
        print(f"\nLiczba to {x}")
        print("\tSpróbuj następnym razem!")

# Wywołanie funkcji gry
number_guessing_game()

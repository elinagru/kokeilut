import random


def heita_noppaa():
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..6."""
    return random.randint(1, 6)


def main():
    # Heitetään noppaa, kunnes tulee kuutonen, ja tulostetaan jokainen heitto
    while True:
        silmaluku = heita_noppaa()
        print(f"Heitto: {silmaluku}")
        if silmaluku == 6:
            break


if __name__ == "__main__":
    main()

import random


def heita_noppaa(tahkojen_maara):
    """Palauttaa satunnaisen silmäluvun väliltä 1..tahkojen_maara."""
    return random.randint(1, tahkojen_maara)


def main():
    # Kysytään käyttäjältä nopan tahkojen määrä
    tahkot = int(input("Anna nopan tahkojen määrä: "))

    print(f"Heitetään {tahkot}-tahkoista noppaa...")
    while True:
        silmaluku = heita_noppaa(tahkot)
        print(f"Heitto: {silmaluku}")
        if silmaluku == tahkot:
            print("Sait maksimi silmäluvun! Lopetetaan.")
            break


if __name__ == "__main__":
    main()

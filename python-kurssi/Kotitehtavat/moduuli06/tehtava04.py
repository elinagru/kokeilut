def laske_summa(luvut):
    """Palauttaa listassa olevien kokonaislukujen summan."""
    return sum(luvut)


def main():
    # Luodaan testilista
    luvut = [3, 7, 2, 8, 4]
    print(f"Lista: {luvut}")

    # Kutsutaan funktiota ja tulostetaan tulos
    summa = laske_summa(luvut)
    print(f"Listan lukujen summa on: {summa}")


if __name__ == "__main__":
    main()

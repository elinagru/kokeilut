def pienin_ja_suurin(luvut):
    """Palauttaa listan pienimmän ja suurimman arvon tuple-muodossa."""
    pienin = min(luvut)
    suurin = max(luvut)
    return pienin, suurin


def main():
    # Luodaan testilista
    luvut = [4, 9, 1, 7, 2, 10, 5]
    print(f"Lista: {luvut}")

    # Kutsutaan funktiota
    pienin, suurin = pienin_ja_suurin(luvut)
    print(f"Pienin arvo on {pienin} ja suurin arvo on {suurin}.")


if __name__ == "__main__":
    main()

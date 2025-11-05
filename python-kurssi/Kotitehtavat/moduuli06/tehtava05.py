def poista_parittomat(luvut):
    """Palauttaa uuden listan, josta on poistettu kaikki parittomat luvut."""
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:  # Tarkistetaan onko parillinen
            parilliset.append(luku)
    return parilliset


def main():
    # Luodaan testilista
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Alkuperäinen lista: {luvut}")

    # Kutsutaan funktiota ja saadaan uusi lista
    karsittu_lista = poista_parittomat(luvut)
    print(f"Karsittu lista (vain parilliset luvut): {karsittu_lista}")


if __name__ == "__main__":
    main()

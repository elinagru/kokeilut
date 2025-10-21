def main():
    luvut = []

    print("Anna lukuja (tyhjä syöte lopettaa):")

    while True:
        syote = input("Anna luku: ")
        if syote == "":
            break  # tyhjä syöte lopettaa ohjelman
        try:
            luku = float(syote)  # sallitaan myös desimaalit
            luvut.append(luku)
        except ValueError:
            print("Anna vain numeroita!")

    if len(luvut) == 0:
        print("Et antanut yhtään lukua.")
    else:
        # Järjestetään luvut suurimmasta pienimpään
        luvut.sort(reverse=True)

        # Otetaan viisi suurinta (tai vähemmän, jos lukuja on alle 5)
        viisi_suurinta = luvut[:5]

        print("\nViisi suurinta lukua suurimmasta pienimpään:")
        for luku in viisi_suurinta:
            print(luku)

if __name__ == "__main__":
    main()
    
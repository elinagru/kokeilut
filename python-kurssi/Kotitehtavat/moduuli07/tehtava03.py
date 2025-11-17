# Tehtävä 3: Lentoasemien tallennus ja haku sanakirjalla

lentoasemat = {}

while True:
    print()
    print("Valitse toiminto:")
    print("1) Syötä uusi lentoasema")
    print("2) Hae lentoasema")
    print("3) Lopeta")
    valinta = input("Valintasi (1-3): ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoasema:", lentoasemat[icao])
        else:
            print("Tällä ICAO-koodilla ei löytynyt lentoasemaa.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")

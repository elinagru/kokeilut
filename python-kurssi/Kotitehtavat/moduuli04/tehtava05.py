OIKEA_TUNNUS = "python"
OIKEA_SALASANA = "rules"

yritykset = 0
while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        print("Tervetuloa")
        break

    print("Väärä tunnus tai salasana.")
    yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")

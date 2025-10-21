def main():
    try:
        luku = int(input("Anna kokonaisluku: "))
    except ValueError:
        print("Virheellinen syöte! Anna kokonaisluku.")
        return

    if luku < 2:
        print(f"{luku} ei ole alkuluku (alkuluvut ovat suurempia kuin 1).")
        return

    on_alkuluku = True  # oletetaan että luku on alkuluku

    for i in range(2, int(luku ** 0.5) + 1):  # riittää tarkistaa neliöjuureen asti
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{luku} on alkuluku!")
    else:
        print(f"{luku} ei ole alkuluku.")

if __name__ == "__main__":
    main()

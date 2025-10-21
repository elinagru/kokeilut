def main():
    kaupungit = []

    print("Anna viisi kaupungin nimeä:")

    # Kysytään viisi kaupungin nimeä
    for i in range(5):
        nimi = input(f"Anna {i+1}. kaupungin nimi: ")
        kaupungit.append(nimi)

    print("\nSyöttämäsi kaupungit:")
    for kaupunki in kaupungit:
        print(kaupunki)


if __name__ == "__main__":
    main()

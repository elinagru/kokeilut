def gallonat_litroiksi(gallonat):
    """Muuntaa gallonan määrän litroiksi. 1 gallona = 3.785 litraa."""
    return gallonat * 3.785


def main():
    while True:
        try:
            gallonat = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))
        except ValueError:
            print("Virheellinen syöte, anna numeroarvo.")
            continue

        if gallonat < 0:
            print("Ohjelma lopetetaan.")
            break

        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat:.2f} gallonaa = {litrat:.2f} litraa\n")


if __name__ == "__main__":
    main()

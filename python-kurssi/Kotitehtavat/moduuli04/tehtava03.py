luvut = []

while True:
    s = input("Anna luku (tyhjä rivi lopettaa): ")
    if s == "":
        break
    try:
        n = float(s)
        luvut.append(n)
    except ValueError:
        print("Ei ollut luku, yritä uudelleen.")

if luvut:
    print(f"Pienin: {min(luvut)}")
    print(f"Suurin: {max(luvut)}")
else:
    print("Yhtään lukua ei annettu.")

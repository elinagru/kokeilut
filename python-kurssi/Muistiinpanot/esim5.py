pituus = int(input("Anna pituutesi:"))
paino = float(input("Anna paino:"))

#muuttuja jossa lasku suoritetaan
bni = paino / (pituus / 100) ** 2

print("pituus-paino-indeksisi on", bni)
print(f"pituus-paino-indeksisi on {bni:2f} ")


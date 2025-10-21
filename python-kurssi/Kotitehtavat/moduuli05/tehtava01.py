import random
def main ():
    while True:
        try:
            n = int(input("Kuinka monta arpakuutiota heitetään? "))
            if n <= 0:
                print ("Anna positiivinen kokonaisluku.")
                continue
            break
        except ValueError:
            print("Anna kokonaisluku numeroin.")

    summa = 0
    for _ in range(n):
        silmaluku = random.randint(1, 6)
        summa += silmaluku
    print (f"Silmälukujen summa: {summa}")

if __name__ == "__main__":
    main()

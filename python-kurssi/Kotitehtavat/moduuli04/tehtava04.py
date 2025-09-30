import random

salaisuus = random.randint(1, 10)

while True:
    s = input("Arvaa luku väliltä 1–10: ")
    try:
        arvaus = int(s)
    except ValueError:
        print("Anna kokonaisluku.")
        continue

    if arvaus < salaisuus:
        print("Liian pieni arvaus")
    elif arvaus > salaisuus:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break

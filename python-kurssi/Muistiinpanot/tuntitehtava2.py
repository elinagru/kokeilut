nimi = input("Kerro nimesi: ")

if nimi != "Matti":
    annokset = int(input("Montako keittoannosta? "))
    print(f"Kokonaishinta on {annokset * 5.9}")
    print(f"Seuraava, kiitos!")

else:
    print("Seuraava kiitos!")


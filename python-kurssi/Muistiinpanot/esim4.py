#Muuntaminen, tapa 1
ika_str = input("kuinka vanha olet? ")
ika = int(ika_str)

print("Ai, eli olet syntynyt", 2025-ika)

#Muuntaminen, tapa 2
ika = int(input("kuinka vanha olet? "))

print("Ai, olet syntynyt", str(2025-ika) + ".")

#Muotoiltu tuloste
print(f"Ai, eli olet syntynt ")
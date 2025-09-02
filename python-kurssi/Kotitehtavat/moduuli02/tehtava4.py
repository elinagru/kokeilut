a = int(input("Anna enimmäinen kokonaisluku: "))
b = int(input("Anna toinen kokonaisluku: "))
c = int(input("Anna kolmas kokonaisluku: "))

summa = a + b + c
tulo = a * b * c
keskiarvo = summa / 3

print("Summa on", summa)
print("Tulo on", tulo)
print("Keskiarvo on", f"{keskiarvo:.2f}")
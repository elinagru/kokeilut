sukupuoli = input("Anna biologinen sukupuolei (nainen/mies): ").lower()
arvo = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if 117 <= arvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    elif arvo < 117:
        priint("Hemoglobiiniarvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if 134 <= arvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    elif arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on korkea.")

else:
    print("Virheellinen sukupuoli.")

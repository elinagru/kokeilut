MIN_PITUUS = 37.0

raw = input("Anna kuhan pituus (cm): ")
try:
    pituus = float (raw)
    if pituus <= 0:
        print("Pituuden on oltava positiivinen luku.")
    elif pituus < MIN_PITUUS:
        puuttuu = MIN_PITUUS - pituus
        print(f"Kuha on alamittainen. Laske se takaisin järveen.")
        print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
    else:
        print("Kuha on mittakala. Saat pitää sen.")
except ValueError:
    print("Virheellinen syöte. Anna pituus numeroina (esim. 36.5).")
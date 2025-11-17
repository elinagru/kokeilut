# Tehtävä 1: Kuukauden numero -> vuodenaika

# Indeksi 0 vastaa tammikuuta, 1 helmikuuta, ... 11 joulukuuta
vuodenajat = (
    "talvi",  # 1: tammikuu
    "talvi",  # 2: helmikuu
    "kevät",  # 3: maaliskuu
    "kevät",  # 4: huhtikuu
    "kevät",  # 5: toukokuu
    "kesä",   # 6: kesäkuu
    "kesä",   # 7: heinäkuu
    "kesä",   # 8: elokuu
    "syksy",  # 9: syyskuu
    "syksy",  # 10: lokakuu
    "syksy",  # 11: marraskuu
    "talvi"   # 12: joulukuu (ensimmäinen talvikuukausi)
)

kk = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kk <= 12:
    vuodenaika = vuodenajat[kk - 1]
    print("Vuodenaika:", vuodenaika)
else:
    print("Virheellinen kuukauden numero.")

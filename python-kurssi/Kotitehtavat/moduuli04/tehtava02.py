# 1 tuuma = 2.54 cm
while True:
    s = input("Anna tuumamäärä (negatiivinen lopettaa): ")
    try :
        tuumat = float(s)
    except ValueError:
        print ("Anna numero.")
        continue
    if tuumat < 0:
        print ("Ohjelma lopetettu.")
        break
    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa = {cm:.2f} cm")


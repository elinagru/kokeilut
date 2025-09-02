#Muunnokset
LEIVISKA_NAULA = 20
NAULA_LUOTI = 32
LUOTI_GRAMMA = 13.3

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luodit_yht = leiviskat * LEIVISKA_NAULA * NAULA_LUOTI + naulat * NAULA_LUOTI + luodit
grammat_yht = luodit_yht * LUOTI_GRAMMA

kilot = int(grammat_yht // 1000)
grammat_jaljella = grammat_yht - kilot * 1000

print("Massa nykymittojen mukaan: ")
print(kilot, "kilogrammaa ja ", f"{grammat_jaljella:.2f}", "gramaa.")
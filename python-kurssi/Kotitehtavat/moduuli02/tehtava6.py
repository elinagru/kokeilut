import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
koodi3 = str(a) + str(b) + str(c)
print("Kolminumeroinen koodi: ", koodi3)

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
d4 = random.randint(1, 6)
koodi4 = str(d1) + str(d2) + str(d3) + str(d4)
print("Nelinumeroinen koodi: ", koodi4)
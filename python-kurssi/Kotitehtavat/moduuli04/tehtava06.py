import random
import math

s = input("Kuinka monta pistettä arvotaan? ")
try:
    N = int(s)
    if N <= 0:
        raise ValueError
except ValueError:
    print("Anna positiivinen kokonaisluku.")
    raise SystemExit

n_sisalla = 0
i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1.0:
        n_sisalla += 1
    i += 1

pi_arvio = 4 * n_sisalla / N
print(f"π likimäärin ≈ {pi_arvio:.6f}")
print(f"(Virhe {abs(math.pi - pi_arvio):.6f})")

import random

N = int(input("Anna arvottavien pisteiden määrä: "))

sisalla = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        sisalla += 1

    i += 1

pi_approx = 4 * sisalla / N
print(f"Piin likiarvo: {pi_approx}")
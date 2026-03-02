import random

salainen = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1..10: "))

    if arvaus < salainen:
        print("Liian pieni arvaus")
    elif arvaus > salainen:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break

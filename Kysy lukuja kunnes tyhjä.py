pienin = None
suurin = None

while True:
    s = input("Anna luku (tyhjä lopettaa): ").strip()
    if s == "":
        break

    luku = float(s)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

if pienin is None:
    print("Et syöttänyt yhtään lukua.")
else:
    print(f"Pienin: {pienin}")
    print(f"Suurin: {suurin}")

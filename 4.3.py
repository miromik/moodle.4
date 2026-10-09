luvut = []
while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luvut.append(float(syote))

if len(luvut) > 0:
    print("Pienin:", min(luvut))
    print("Suurin:", max(luvut))
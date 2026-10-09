yritykset = 0
pasy = False

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        pasy = True
        break
    else:
        yritykset += 1

if not pasy:
    print("Pääsy evätty")
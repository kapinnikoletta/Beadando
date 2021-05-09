import random

def szamlalo():
    pontszam = int(501)
    db = 9 # Nyerni lehet 9 nyillal: 6 db T20, majd pl. T20, T19 és D12
    print(f"Ahhoz, hogy nyerjen ennyi dobásra van szüksége: {int(db)}")
    print(f"""Az ön pontszáma jelenleg {round(pontszam)}. Adja meg tervezett dobását!
        Jelölések: T = tripla, D = dupla, S = szimpla, a betűk után pedig a tervezett dobás értéke áll.
        Például: T20 vagy D15 vagy S10.""")
    while True:
        if pontszam < 0:
            print("Túl alacsonyra ment a pontszámításban, Ön vesztett!")
            break
        elif pontszam == 0:
            print("Ön nyert! Gratulálunk!")
            break
        else:
            print()
            elso = pontszam // 60
            masodik = (pontszam - (pontszam//60 * 60)) // 57
            harmadik = ((pontszam - (pontszam//60 * 60)) // 57 * 57) // 54
            negyedik = (((pontszam - (pontszam//60 * 60)) // 57 * 57) // 54 * 54) // 51
            db = elso + masodik + harmadik + negyedik
            dobas = str(input("Adja meg a tervezett dobását: "))
            if dobas[0] == "T":
                dobasmasik = "D"+dobas[1:]
                dobasharmadik = "S"+dobas[1:]
            elif dobas[0] == "D":
                dobasmasik = "T" + dobas[1:]
                dobasharmadik = "S" + dobas[1:]
            elif dobas[0] == "S":
                dobasmasik = "T" + dobas[1:]
                dobasharmadik = "D" + dobas[1:]
            randomszamok = [] #itt tárolom a dobást, ami teljesen véletlen, akár hibás dobás (pl. fal)
            for i in range(0,61):
                randomszamok.append(i)
            kimenetek = [dobas,random.choice(randomszamok),dobasmasik,dobasharmadik]
            # a lehetséges kimenetek, ami vagy maga a dobás, vagy egy teljesen véletlen szám 0 és 60 között
            # vagy 15-15%-kal T helyett D vagy S, D helyett T vagy S, S helyett T vagy D
            valasztas = random.choices(kimenetek,weights=(50,20,15,15))
            # itt adom meg, hogy a kimeneteknek mik a valószínűségei

            try:
                pontszam -= valasztas[0]
            except TypeError:
                if valasztas[0][0] == "T":
                    pontszam -= int(str(valasztas[0][1:])) * 3
                if valasztas[0][0] == "D":
                    pontszam -= int(str(valasztas[0][1:])) * 2
                if valasztas[0][0] == "S":
                    pontszam -= int(str(valasztas[0][1:])) * 1
            print(f"A valós dobása {valasztas[0]} lett.")
            print(f"Az ön pontszáma jelenleg {round(pontszam,2)}.")
            print(f"Ahhoz, hogy nyerjen ennyi dobásra van szüksége: {int(db)}")

szamlalo()
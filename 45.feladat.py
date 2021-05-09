def adoszamEllenorzes():
    try:
        adoszam = input("Adjon meg egy adószámot!: ")
        hossz = 13
        lista = adoszam.split("-")
        kotjel1 = adoszam[8]
        kotjel2 = adoszam[10]
        torzs = int(lista[0])
        afaJelleg = lista[1]
        illetekes = lista[2]
        illetekes = str(illetekes)
        stat1 = adoszam[:1]
        elvalaszto = "-"
        x = []
        if hossz:
            if kotjel1 and kotjel2 == elvalaszto:
                if 10000010 <= torzs <= 10299999:
                    x.append("Vállalatok, szövetkezetek, pénzintézetek és egyéb szervek")
                elif 15300010 <= torzs <= 15699999:
                    x.append("Önálló és bankszámlával rendelkező, részben önálló költségvetési szervek")
                elif 20930010 <= torzs <= 20999999:
                    x.append("Belföldi társaságok, magánszemélyek társaságai")
                elif 16000010 <= torzs <= 16999999:
                    x.append("Önálló bankszámlával nem rendelkező, részben önálló költségvetési szervek.")
                elif 19000010 <= torzs <= 19999999 or 30000010 <= int(torzs) <= 30100009:
                    x.append("Költségvetési rend szerint gazdálkodó egyéb jogi személyek")
                elif 40000010 <= torzs <= 59999999:
                    x.append("Egyéni vállalkozók (kisiparosok, magánkereskedők, szerződéses ipar és kereskedelmi szolgáltatók)")
                elif 70000010 <= torzs <= 74999999:
                    x.append("Általános forgalmi adó fizetésére kötelezett magánszemélyek")
                else:
                    x.append("A törzsszám alapján nem található információ az adószámról.")
                if str(afaJelleg) == "1":
                    x.append("Alanyi adómentes vagy adómentes tevékenységet végző (ÁFA körbe nem tartozó)")
                elif str(afaJelleg) == "2":
                    x.append("Általános szabályok szerint adózó (Áfa körbe tartozó)")
                elif str(afaJelleg) == "3":
                    x.append("Egyszerűsített vállalkozói adózás alá tartozó (EVA körbe tartozó)")
                elif str(afaJelleg) == "4":
                    x.append("ÁFA körbe tartozó csoport adóalanyiságot választó")
                elif str(afaJelleg) == "5":
                    x.append("ÁFA körbe csoport közös adószámának jelzése")
                elif afaJelleg == 0 or 5 < afaJelleg <= 9:
                    x.append("Nem található információ a beírt adószámról.")
                if illetekes == "02" or illetekes == "22":
                    x.append("Baranya")
                elif illetekes == "03" or illetekes == "23":
                    x.append("Bács-Kiskun")
                elif illetekes == "04" or illetekes == "24":
                    x.append("Békés")
                elif illetekes == "05" or illetekes == "25":
                    x.append("Borsod-Abaúj-Zemplén")
                elif illetekes == "06" or illetekes == "26":
                    x.append("Csongrád-Csanád")
                elif illetekes == "07" or illetekes == "27":
                    x.append("Fejér")
                elif illetekes == "08" or illetekes == "28":
                    x.append("Győr-Moson-Sopron")
                elif illetekes == "09" or illetekes == "29":
                    x.append("Hajdú-Bihar")
                elif illetekes == "10" or illetekes == "30":
                    x.append("Heves")
                elif illetekes == "11" or illetekes == "31":
                    x.append("Komárom-Esztergom")
                elif illetekes == "12" or illetekes == "32":
                    x.append("Nógrád")
                elif illetekes == "13" or illetekes == "33":
                    x.append("Pest")
                elif illetekes == "14" or illetekes == "34":
                    x.append("Somogy")
                elif illetekes == "15" or illetekes == "35":
                    x.append("Szabolcs-Szatmár-Bereg")
                elif illetekes == "16" or illetekes == "36":
                    x.append("Jász-Nagykun-Szolnok")
                elif illetekes == "17" or illetekes == "37":
                    x.append("Tolna")
                elif illetekes == "18" or illetekes == "38":
                    x.append("Vas")
                elif illetekes == "19" or illetekes == "39":
                    x.append("Veszprém")
                elif illetekes == "20" or illetekes == "40":
                    x.append("Zala")
                elif illetekes == "41":
                    x.append("Észak-Budapest")
                elif illetekes == "42":
                    x.append("Kelet-Budapest")
                elif illetekes == "43":
                    x.append("Dél-Budapest")
                elif illetekes == "44":
                    x.append("Kiemelt Adózók Adóigazgatósága")
                elif illetekes == "51":
                    x.append("Kiemelt Ügyek Adóigazgatósága")
                else:
                    x.append("Nem található területi adóhatóságról információ.")
        if len(adoszam) != hossz:
            x.append("Az adószám hossza nem megfelelő!")
            return x
        return x
    except IndexError:
        x = "Az adószám nem megfelelő!"
        return x
    except ValueError:
        x = "Az adószám nem megfelelő!"
        return x
print(adoszamEllenorzes())

# Példák:
# 123-2-42
# 16345678.4-35
# 16345678-4.35
# 10254531-4-26
# 65478543-3-41
# 17432153-5-30
# 25353745-2-44
# 10722316-2-41
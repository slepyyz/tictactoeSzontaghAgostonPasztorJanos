import random

palya = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jatek_megy = 1
lepesek_szama = 0
nyertes = "nincs"

def kiiras():
    print(palya[0])
    print(palya[1])
    print(palya[2])

def bekeres():
    global palya, lepesek_szama
    print("\n--- Te jössz! ---")
    
    te_keresel = 1
    while te_keresel == 1:
        sor = int(input("Sor (0, 1, 2): "))
        oszlop = int(input("Oszlop (0, 1, 2): "))
        
        if sor < 0:
            print("Hiba: 0-nál kisebb számot adtál.")
        elif sor > 2:
            print("Hiba: 2-nél nagyobb számot adtál.")
        elif oszlop < 0:
            print("Hiba: 0-nál kisebb számot adtál.")
        elif oszlop > 2:
            print("Hiba: 2-nél nagyobb számot adtál.")
        else:
            if palya[sor][oszlop] == "-":
                palya[sor][oszlop] = "X"
                lepesek_szama = lepesek_szama + 1
                te_keresel = 0 
            else:
                print("Hiba: Ez a hely már foglalt!")

def geplepes():
    global palya, lepesek_szama
    print("\n--- A gép jön ---")
    
    gep_keres = 1
    while gep_keres == 1:
        gs = random.randint(0, 2)
        go = random.randint(0, 2)
        
        if palya[gs][go] == "-":
            palya[gs][go] = "O"
            lepesek_szama = lepesek_szama + 1
            gep_keres = 0

def ellenorzes():
    nyertes = "nincs"
    #  ELLENŐRZÉS NYERTÉL-E? 
    # Sorok
    if palya[0][0] == "X" and palya[0][1] == "X" and palya[0][2] == "X": nyertes = "TE"
    if palya[1][0] == "X" and palya[1][1] == "X" and palya[1][2] == "X": nyertes = "TE"
    if palya[2][0] == "X" and palya[2][1] == "X" and palya[2][2] == "X": nyertes = "TE"
    # Oszlopok
    if palya[0][0] == "X" and palya[1][0] == "X" and palya[2][0] == "X": nyertes = "TE"
    if palya[0][1] == "X" and palya[1][1] == "X" and palya[2][1] == "X": nyertes = "TE"
    if palya[0][2] == "X" and palya[1][2] == "X" and palya[2][2] == "X": nyertes = "TE"
    # Átlók
    if palya[0][0] == "X" and palya[1][1] == "X" and palya[2][2] == "X": nyertes = "TE"
    if palya[0][2] == "X" and palya[1][1] == "X" and palya[2][0] == "X": nyertes = "TE"
    
    #  ELLENŐRZÉS: NYERT-E A GÉP? 
    if palya[0][0] == "O" and palya[0][1] == "O" and palya[0][2] == "O": nyertes = "GEP"
    if palya[1][0] == "O" and palya[1][1] == "O" and palya[1][2] == "O": nyertes = "GEP"
    if palya[2][0] == "O" and palya[2][1] == "O" and palya[2][2] == "O": nyertes = "GEP"
    if palya[0][0] == "O" and palya[1][0] == "O" and palya[2][0] == "O": nyertes = "GEP"
    if palya[0][1] == "O" and palya[1][1] == "O" and palya[2][1] == "O": nyertes = "GEP"
    if palya[0][2] == "O" and palya[1][2] == "O" and palya[2][2] == "O": nyertes = "GEP"
    if palya[0][0] == "O" and palya[1][1] == "O" and palya[2][2] == "O": nyertes = "GEP"
    if palya[0][2] == "O" and palya[1][1] == "O" and palya[2][0] == "O": nyertes = "GEP"
    
    return nyertes

def jatek_futtat():
    """A teljes játék futtatása, visszatér az eredménnyel"""
    global jatek_megy, lepesek_szama, nyertes
    
    print("AMŐBA JÁTÉK (X = Te, O = Gép)")
    print("SZABÁLYOK:")
    print("---------------------------------")
    print("HA AZT AKROD HOGY LEÁLLJON A PROGRAM, NE IRJ BE EZEKET: 0,1,2")
    print("HA AZT AKAROD HOGY LEÁLLJON A PROGRAM, ÜSS EGY ENTERT!")
    print("SIMA 'SPACE' SE HASZNÁLJ MERT LEÁLL A PROGRAM!")
    print("Csak 0, 1 vagy 2 számokat írj be!")
    print("SEMMILYEN SPECIÁLIS KARAKTERT NE HASZNÁLJ!")
    print("HA BETŰT ÍRSZ, A PROGRAM LEÁLL!")
    print("---------------------------------")

    kiiras()

    while jatek_megy == 1:
        
        # =================== TE KÖRÖD ===================
        bekeres()

        kiiras()

        nyertes = ellenorzes()

        if nyertes == "TE":
            print("\nGRATULÁLOK! NYERTÉL!")
            jatek_megy = 0
            return "TE"

        if jatek_megy == 1:
            if lepesek_szama == 9:
                print("\nDÖNTETLEN! Betelt a tábla.")
                jatek_megy = 0
                return "DONTETLEN"

        # =================== GÉP KÖRE ===================
        if jatek_megy == 1:
            geplepes()
            
            kiiras()

            nyertes = ellenorzes()

            if nyertes == "GEP":
                print("\nVESZTETTÉL! A gép nyert.")
                jatek_megy = 0
                return "GEP"
                
        if jatek_megy == 1:
            if lepesek_szama == 9:
                print("\nDÖNTETLEN! Betelt a tábla.")
                jatek_megy = 0
                return "DONTETLEN"

import feladatok

print("=" * 30)
print("         AMŐBA JÁTÉK ")
print("=" * 30)

ujra_jatszik = True

while ujra_jatszik:
    eredmeny = feladatok.jatek_futtat()
    
    print("\n" + "=" * 30)
    if eredmeny == "TE":
        print(" GYŐZELEM! Te nyertél!")
    elif eredmeny == "GEP":
        print(" A gép nyert! Próbáld újra!")
    elif eredmeny == "DONTETLEN":
        print(" Döntetlen! Jó játék volt!")
    
   
    valasz = input("\nSzeretnél újra játszani? (i/n): ").lower()
    if valasz != 'i':
        ujra_jatszik = False
    else:
        feladatok.reset_jatek()
        print("\n" + "=" * 30)
        print("         ÚJ JÁTÉK ")
        print("=" * 30)

print("Köszönjük a játékot!")
print("=" * 30)

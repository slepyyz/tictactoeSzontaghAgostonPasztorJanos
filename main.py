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
    
   
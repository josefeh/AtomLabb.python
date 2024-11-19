"""Ett program som låter användaren att mata in olika värden releterade till Aritmetisk/Geometrisk summa,
men programmet kontrollerar även felmatning, som ger avslut. Slutligen avgör programmet vilken summa som är störst
eller om dem är lika. """

#Skapar en funktion med formler för de olika summorna.
def aritmetisk_summa(a1,d,n): # a1 utgör första talen, d differansen, n för n:te talet.
    ari_summa =(a1+d*(n-1) + a1)*n/2  # ari_summa för aritmetsiksumma
    return ari_summa

def geometrisk_summa(g1,q,n): # g1 utgör första tal i geometrisk summa, q kvot, n för n:te talet.
    try:
      gn = g1 * q ** (n - 1)
      geo_summa = g1 * (q ** n - 1) / (q - 1)
    
    except ZeroDivisionError:     # Man kan ju liksom inte glömma att divion med 0 är ett matematiskt brott!
        print("Du kan inte dela med 0, Øllan!")
        exit() 
    return geo_summa

# Skapar inmatning och felundersökning
def läs_heltal():
    #Matar in alla nödvändiga inmatningar på en gång
    try:
        print("Data för den aritmetiska summan:")
        a1=float(input("Skriv in startvärdet (a1): "))
        d=float(input("Skriv in differans (d): "))
        print()
        print("Data för den geometriska summan:")
        g1=float(input("Skriv in startvärdet (g1): "))
        q=float(input("Skriv in kvoten (q): "))
        print()
        print("Antal termer i summorna: ")
        
    
    # Kontrollerar att inget ogiltigt skrivs, om det görs avslutas programmet
    except ValueError:
        print("Det där var inget flyttal! Starta om programmet och försök igen.")
        exit()
    try:
        n=int(input("Skriv in antal element i följden (n): ")) #Skapar eget felmeddelande för n
    except ValueError:
        print("Det där var inget heltal. Starta om programmet och försök igen.")
        exit()

    return a1,d,g1,q,n  #Retunerar våra inmatning

a1,d,g1,q,n = läs_heltal()     #Tilldelar alla våra värden precis som dem inmatas

ari_summa = aritmetisk_summa(a1,d,n)    #Definerar ari_summa så den kan användas till jämförelse
geo_summa = geometrisk_summa(g1,q,n)    #Definerar geo_summa så den kan användas till jämförelse


#Slutligen så jämför vi
if ari_summa > geo_summa:
    print("Din aritmetiska summa är störst!")
elif ari_summa < geo_summa:
    print("Din Geometriska summa är störst")
else:                                          #Else då det egentligen finns något mer att säga.
    print("Båda är lika stora!")    

print("Din aritmetiska summa är: ", ari_summa ,"\nDin geometriska summa är: ", geo_summa)  # man kan undra det man fick såklart!
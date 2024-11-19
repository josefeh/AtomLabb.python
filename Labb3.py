"""Ett program som låter användaren att mata in olika värden releterade till Aritmetisk/Geometrisk summa 
där den importerade modulen används för felkontrollering. Slutligen avgör programmet vilken summa som är störst
eller om dem är lika. """

import läs_heltal

def aritmetisk_summa (a1,d,n): 
    """Beräknar summan av den aritmetisk serie"""
    ari_summa =(a1 + d * (n-1) + a1) * n/2 
    return ari_summa

def geometrisk_summa(g1,q,n):
   """Beräknar summan av den geometriska serien"""
   while True:
    try:
      gn = g1 * q ** (n - 1)
      geo_summa = g1 * (q ** n - 1) / (q - 1)
      return geo_summa
    except ZeroDivisionError:     
        print("Du kan inte dela med 0!")
        q = float(input("Ange en ny kvot (q), den får inte vara 1: ")) 
       
     
def main():
  a1 = läs_heltal.float_input("Skriv in värdet på a1:") 
  d = läs_heltal.float_input("Skriv in värdet på d: ")
  n = läs_heltal.int_input("Skriv in värdet på n: ")
  
  while n <= 0:
    print("n måste vara större än noll.")
    n = läs_heltal.int_input("Skriv in värdet på n: ")

  ari_summa = aritmetisk_summa(a1,d,n)
  
  g1 = läs_heltal.float_input("Skriv in värdet på g1: ")
  q = läs_heltal.float_input("Skriv in värdet på q: ")

  while q <= 0:
    q = läs_heltal.float_input("Skriv in värdet på q: ")
  
  geo_summa = geometrisk_summa(g1,q,n)
  
  #Slutligen så jämför vi den aritmetiska summan med den geometriska summan
  
  if ari_summa > geo_summa:
    print("Din aritmetiska summa är störst!")
  elif ari_summa < geo_summa:
    print("Din Geometriska summa är störst")
  else:                                          
    print("Båda är lika stora!")    
    
main()
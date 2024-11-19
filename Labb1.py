def Aretmetisk_summa (a_n, d, n): #a_1 är det första talet i talföljden, d är differansen och n är n-te talet
  a_n = a_1 + d * (n-1)
  S_n1 = n * ((a_1 + a_n) / 2) #Aritmetisk summa beräknas enligt följande formel
  return S_n1 #Returnerar Aritmetisk summa

a_1 = 5
d = 2
n = 3

def Geometrisk_summa (g_1, q, n): #g_1 är det första talet i talföljden, q är kvoten och n är n-te talet
  g_n = g_1 * q^(n-1)
  S_n2 = g_1 * ((q**(n) - 1) / (q-1)) #Geometrisk summa beräknas enligt följande formel
  return S_n2 

g_1 = 5
q = 2
n = 3

print("Den aritmetiska summan är:", Aretmetisk_summa(a_1, d, n))
print("Den geometrisk summan är:", Geometrisk_summa (g_1, q, n))
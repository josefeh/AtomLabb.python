"""Modul som behandlar felinmatningar i både float och int"""

def int_input(ledtext):             # funktion för int inmatning definieras 
   while True:                      # En loop skapas för att felinmating ska kunnar hanteras flear gånger om fel skrivs
    try:
        inmatning = int(input(ledtext))
        return inmatning
    except ValueError:
        print("Endast siffror är giltiga för personnummer.")


def float_input(ledtext):       # Bara upprepning som funktionen ovan, men float istället: vi drar till main
    while True:
        try:
            inmatning=float(input(ledtext))
            return inmatning
        except ValueError:
            print("Det där var inget giltigt floattal. Försök igen.")

def bokstäver_input(ledtext):
    while True:
        bokstäver = input(ledtext).strip()
        if bokstäver.isalpha() and bokstäver:
            break
        print("Skriv endast bokstäver.")
    return bokstäver

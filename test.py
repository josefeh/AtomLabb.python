"""Ett program där användaren får träna på det periodiska systemet genom att
antigen träna på atomnummer, atombeckningar, atomnamn eller visa alla atomer"""

import random

class Atom:
    """En klass för att representera en atom"""

    def __init__(self, symbol, atom_nummer, namn, atom_massa):
        self.symbol = symbol
        self.atom_nummer = atom_nummer
        self.namn = namn
        self.atom_massa = atom_massa

    def __str__(self):
        """Skriver ut värdena som en sträng"""
        return f"Nummer: ({self.atom_nummer}) Symbol: ({self.symbol}) Namn: ({self.namn}) Massa: ({self.atom_massa})"
    
    def __lt__(self, other):
        """Jämför atomnummer för sortering av listan"""
        return self.atom_nummer < other.atom_nummer

def läs_in_fil_och_fyll_ut(atom_lista):
    """Funktion för att läsa in från fil och fylla listan med Atom-objekt"""
    with open('avikt.txt', 'r', encoding='utf-8') as file:
        for line in file: #loopar igenom varje rad i filen
            
            delar = line.strip().split() #delar är en lista där varje element är atomens egenskaper. Split delar upp en sträng i delar. Split rensar blanksteg i början och slutet av en sträng.
            symbol = delar[0]
            atom_nummer = int(delar[1])
            namn = delar[2]
            atom_massa = float(delar[3])
            
            atom_lista.append(Atom(symbol, atom_nummer, namn, atom_massa)) #Fyller på listan med ett nytt atom objekt och sparar.

def visa_atomer(atom_lista):
    for atom in atom_lista:
        print(atom)

def sortera_atom_nummer(atom_lista):
      atom_lista.sort()  # Använder __lt__ operatorn i Atom-klassen för att sortera baserat på atomnummer.

def träna_atom_nummer(atom_lista):
    """Träningsfunktion för atomnummer"""

    while True:
        random_nummer = random.randint(0, len(atom_lista) - 1)
        
        for i in range(3):
            anvandar_svar = input("Vad är atomnummret för " + atom_lista[random_nummer].namn + "? Skriv q för att gå tillbaka till menyn\n")

            if anvandar_svar == 'q':
                return
            
            elif int(anvandar_svar) == atom_lista[random_nummer].atom_nummer:

                print("Rätt svar!\n")
                break
            else:
                print("Fel svar! Försök igen\n")
                
                if i == 2:
                    print("Rätta svaret va: " + str(atom_lista[random_nummer].atom_nummer))


def main():
    atomer = []
    läs_in_fil_och_fyll_ut(atomer)
    sortera_atom_nummer(atomer)
    while True:
        print()
        print("Välkommen till ett Träningsprogram för det Periodiska systemet! Välj vad du vill träna på nedan: ")
        print()
        print("1. Visa alla atomer")
        print("2. Träna på atomnummer")
        print("3. Träna på atombeteckningar")
        print("4. Träna på atomnamn")
        print("5. Sluta")
        print()

        meny_val = input("Vad vill du göra? ")

        if meny_val == "1":
            visa_atomer(atomer)
        
        elif meny_val == "2":
            träna_atom_nummer(atomer)

        elif meny_val == "3":
            continue

        elif meny_val == "4":
            continue

        elif meny_val == "5":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

main()
"""Ett program där användaren får träna på det periodiska systemet genom att
antigen träna på atomnummer, atombeckningar, atomnamn eller visa alla atomer"""

import random #modul för att generera slumpmässiga tal

class Atom:
    """En klass för att representera en atom"""

    def __init__(self, symbol, atom_nummer, namn, atom_massa):
        """Atom-instans för atomens olika attribut"""
        self.symbol = symbol
        self.atom_nummer = atom_nummer
        self.namn = namn
        self.atom_massa = atom_massa

    def __str__(self):
        """Skriver ut värdena som en sträng"""
        return f"Nummer: ({self.atom_nummer}) Symbol: ({self.symbol}) Namn: ({self.namn}) Massa: ({self.atom_massa})"
    
    def __lt__(self, other):
        """Jämför två atomer baserat på atomnummer för att sortera listan"""
        return self.atom_nummer < other.atom_nummer


def läs_in_fil_och_fyll_ut(atom_lista):
    """Funktion för att läsa in från filen och fylla listan med Atom-objekt"""
    with open('avikt.txt', 'r', encoding='utf-8') as file:
        for line in file: #loopar igenom varje rad i filen
            
            delar = line.strip().split() #delar är en lista där varje element är atomens egenskaper. Split delar upp en sträng i delar. Strip rensar blanksteg i början och slutet av en sträng.
            symbol = delar[0]
            atom_nummer = int(delar[1])
            namn = delar[2]
            atom_massa = float(delar[3])
            
            atom_lista.append(Atom(symbol, atom_nummer, namn, atom_massa)) #Fyller på listan med ett nytt atom objekt och sparar.


def visa_atomer(atom_lista):
    """Funktion för att visa alla atomer i listan"""
    for atom in atom_lista:
        print(atom)


def sortera_atom_nummer(atom_lista):
    """Använder __lt__ operatorn i Atom-klassen för att sortera listan baserat på atomnummer."""
    atom_lista.sort() #Sorterar listan baserat på atomnummer mha 


def träna_atom_nummer(atom_lista):
    """Träningsfunktion för atomnummer"""
    
    while True:
        random_nummer = random.randint(0, len(atom_lista) - 1)

        for i in range(3):
            
            while True:  # Loop för att kontrollera rätt inmatning
                anvandar_svar = input("Vad är atomnummret för " + atom_lista[random_nummer].namn + "? Skriv 'q' för att gå tillbaka till menyn.\n")
                
                if anvandar_svar.lower() == 'q':
                    return
                
                if not anvandar_svar.isdigit():  # Kontrollera om inmatningen är ett heltal
                    print("Du kan bara in mata in siffror, inget annat!")
                else:
                    break  # Avbryt while-loopen om inmatningen är giltig.
            
            if int(anvandar_svar) == atom_lista[random_nummer].atom_nummer:
                print("Rätt svar!\n")
                break

            else:
                print("Fel svar! Försök igen\n")
                
                if i == 2:
                    print("Rätta svaret var: " + str(atom_lista[random_nummer].atom_nummer))


def träna_atom_beteckningar(atom_lista):
    """Träningsfunktion för atombeteckningar"""

    while True:
        random_beteckning = random.randint(0, len(atom_lista) - 1)
        
        for i in range(3):

            while True:
                anvandar_svar_1 = input("Vad har " + str(atom_lista[random_beteckning].namn) + " för symbol" "? Skriv q för att gå tillbaka till menyn\n")

                if anvandar_svar_1.lower() == 'q':
                    return
                
                if not anvandar_svar_1.isalpha():
                    print("Du kan bara mata in bokstäver, inget annat!")
                else:
                    break
                
            if str(anvandar_svar_1) == atom_lista[random_beteckning].symbol.lower():
                print("Rätt svar!\n")
                break
            else:
                print("Fel svar! Försök igen\n")
                    
                if i == 2:
                    print("Rätta svaret va: " + str(atom_lista[random_beteckning].symbol))


def träna_atom_namn(atom_lista):
    """Träningsfunktion för atomnamn"""

    while True:
        random_beteckning = random.randint(0, len(atom_lista) - 1)
        
        for i in range(3):

            while True:
                anvandar_svar_2 = input("Vad har atomnummer " + str(atom_lista[random_beteckning].atom_nummer) + " för namn" "? Skriv q för att gå tillbaka till menyn\n")

                if anvandar_svar_2.lower() == 'q':
                    return
                
                if not anvandar_svar_2.isalpha():
                    print("Du kan bara mata in bokstäver, inget annat!")
                else:
                    break

            if str(anvandar_svar_2.lower()) == atom_lista[random_beteckning].namn.lower():
                print("Rätt svar!\n")
                break
            else:
                print("Fel svar! Försök igen\n")
                    
                if i == 2:
                    print("Rätta svaret va: " + str(atom_lista[random_beteckning].namn))


def main():
    atomer = []
    läs_in_fil_och_fyll_ut(atomer)
    sortera_atom_nummer(atomer)
    
    while True:
        print("\n1. Visa alla atomer")
        print("2. Träna på atomnummer")
        print("3. Träna på atombeteckningar")
        print("4. Träna på atomnamn")
        print("5. Sluta\n")

        meny_val = input("Vad vill du göra? \n")

        if meny_val == "1":
            print("\nHär är en lista av alla atomer i det periodiska systemet: \n")
            visa_atomer(atomer)
        
        elif meny_val == "2":
            träna_atom_nummer(atomer)

        elif meny_val == "3":
            träna_atom_beteckningar(atomer)
        
        elif meny_val == "4":
            träna_atom_namn(atomer)

        elif meny_val == "5":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

main()
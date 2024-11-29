"""Ett program där användaren får träna på det periodiska systemet genom att
antigen träna på atomnummer, atombeckningar, atomnamn eller visa alla atomer"""

import random # modul för att generera slumpmässiga tal

class Atom:
    """En klass för att representera en atom"""

    def __init__(self, symbol, atom_nr, namn, massa):
        """Atom-instans för atomens olika attribut"""
        self.symbol = symbol
        self.atom_nr = atom_nr
        self.namn = namn
        self.massa = massa

    def __str__(self):
        """Skriver ut värdena som en sträng"""
        return f"Nummer: ({self.atom_nr}) Symbol: ({self.symbol}) Namn: ({self.namn}) Massa: ({self.massa})"
    
    def __lt__(self, other):
        """Jämför två atomer baserat på atomnummer för att sortera listan"""
        return self.atom_nr < other.atom_nr


def ladda_upp(atom_lista):
    """Funktion för att läsa in från filen och fylla listan med Atom-objekt"""
    with open('avikt.txt', 'r', encoding='utf-8') as file:
        for line in file: # Loopar igenom varje rad i filen
            
            delar = line.strip().split() # Dela upp raden i olika delar. Split delar upp en sträng i delar. Strip rensar blanksteg i början och slutet av en sträng.
            symbol = delar[0]
            atom_nr = int(delar[1])
            namn = delar[2]
            massa = float(delar[3])
            
            atom_lista.append(Atom(symbol, atom_nr, namn, massa)) # Fyller på listan med ett nytt atom objekt och sparar

def visa_atomer(atom_lista):
    """Funktion för att visa alla atomer i listan"""
    for atom in atom_lista:
        print(atom)


def sortera_atom_nr(atom_lista):
    """Använder __lt__ operatorn i Atom-klassen för att sortera listan baserat på atomnummer."""
    atom_lista.sort() # Sorterar listan baserat på atomnummer med lt operatorn


def träna_atom_nr(atom_lista):
    """Träningsfunktion för atomnummer"""
    
    while True:
        slumpat_index = random.randint(0, len(atom_lista) - 1) # Väljer ett slumpmässigt tal från listan

        for försök in range(3): # Ger användaren tre försök
            
            while True:  # Loop för att kontrollera rätt inmatning
                svar_1 = input (f"Vad är atomnummret för {atom_lista[slumpat_index].namn} ? Skriv 'q' för att gå tillbaka till menyn.\n")
                
                if svar_1.lower() == 'q': # Om användaren skriver 'q', avsluta träningen och återgå till menyn
                    return
                
                if not svar_1.isdigit():  # Kontrollera om inmatningen är ett heltal
                    print("Du kan bara mata in siffror, inget annat!")
                else:
                    break  # Avbryt while-loopen om inmatningen är giltig.
            
            if int(svar_1) == atom_lista[slumpat_index].atom_nr:
                print("Rätt svar!\n")
                break

            else:
                print("Fel svar! Försök igen\n")
                
                if försök == 2: # Om användaren har gjort 3 fel, visa rätt svar
                    print(f"Rätta svaret var: {atom_lista[slumpat_index].atom_nr}")


def träna_beteckning(atom_lista):
    """Träningsfunktion för atombeteckningar"""

    while True: # Loop för att kontrollera rätt inmatning
        slumpat_index = random.randint(0, len(atom_lista) - 1)
        
        for försök in range(3): # Ger användaren tre försök

            while True:
                svar_2 = input(f"Vad har {atom_lista[slumpat_index].namn} för symbol? Skriv q för att gå tillbaka till menyn\n")

                if svar_2.lower() == 'q': # Om användaren skriver 'q', avsluta träningen och återgå till menyn
                    return
                
                if not svar_2.isalpha(): # Kontrollera om inmatningen är ett heltal
                    print("Du kan bara mata in bokstäver, inget annat!")
                else:
                    break # Avbryt while-loopen om inmatningen är giltig.
                
            if svar_2 == atom_lista[slumpat_index].symbol:
                print("Rätt svar!\n")
                break

            else:
                print("Fel svar! Försök igen\n")
                    
                if försök == 2: # Om användaren har gjort 3 fel, visa rätt svar
                    print(f"Rätta svaret var: {atom_lista[slumpat_index].symbol}")


def träna_namn(atom_lista):
    """Träningsfunktion för atomnamn"""

    while True: # Loop för att kontrollera rätt inmatning
        slumpat_index = random.randint(0, len(atom_lista) - 1)
        
        for försök in range(3): # Ger användaren tre försök

            while True:
                svar_3 = input(f"Vad har atomnummer {(atom_lista[slumpat_index].atom_nr)} för namn ? Skriv q för att gå tillbaka till menyn. \n")

                if svar_3.lower() == 'q': # Om användaren skriver 'q', avsluta träningen och återgå till menyn
                    return
                
                if not svar_3.isalpha(): # Kontrollera om inmatningen är ett heltal
                    print("Du kan bara mata in bokstäver, inget annat!")
                else:
                    break # Avbryt while-loopen om inmatningen är giltig.

            if str(svar_3.lower()) == atom_lista[slumpat_index].namn.lower():
                print("Rätt svar!\n")
                break
            else:
                print("Fel svar! Försök igen\n")
                    
                if försök == 2: # Om användaren har gjort 3 fel, visa rätt svar
                    print(f"Rätta svaret var: {atom_lista[slumpat_index].namn}")


def main():
    """Main funktion för att köra all kod och funktioner, menyvalet finns även med. """
    
    atomer = [] # Skapa en tom lista för atomer

    ladda_upp(atomer) # Läs in atomer från filen
    sortera_atom_nr(atomer) # Sortera atomnerna efter atomnummer
    
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
            träna_atom_nr(atomer)

        elif meny_val == "3":
            träna_beteckning(atomer)
        
        elif meny_val == "4":
            träna_namn(atomer)

        elif meny_val == "5":
            print("Avslutar programmet.")
            break # Avsluta programmet
        else:
            print("Ogiltigt val. Försök igen.")

main() # Kör main funktionen
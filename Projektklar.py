"""P-uppgift 178 Periodiska systemet
Ett program där användaren får träna på det periodiska systemet genom att
antigen träna på atomnummer, atomsymboler, atomnamn eller visa alla atomer"""

import random 

class Atom:
    """En klass för att representera en atom in det periodiska systemet"""

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

ATOM_DATA_FIL = 'avikt.txt' 

def ladda_upp(atom_lista, filnamn = ATOM_DATA_FIL):
    """Funktion för att läsa in från filen och fylla listan med Atom-objekt"""
    with open(filnamn, 'r', encoding='utf-8') as file:
        for line in file: 
            
            delar = line.strip().split() # Rensar och delar upp radens data
            symbol = delar[0]
            atom_nr = int(delar[1])
            namn = delar[2]
            massa = float(delar[3])
            
            atom_lista.append(Atom(symbol, atom_nr, namn, massa))

def visa_atomer(atom_lista):
    """Funktion för att visa alla atomer i listan"""
    for atom in atom_lista:
        print(atom)


def sortera_atom_nr(atom_lista):
    """Använder __lt__ operatorn i Atom-klassen för att sortera listan baserat på atomnummer."""
    atom_lista.sort() 


def träna_atom_nr(atom_lista):
    """Träningsfunktion för atomnummer. Interagerar med användaren för att gissa rätt nummer."""
    
    while True:
        slumpat_index = random.randint(0, len(atom_lista) - 1) # Väljer ett slumpmässigt tal från listan

        for försök in range(3): 
            
            while True:  
                nummer_svar = input(f"Vad är atomnummret för {atom_lista[slumpat_index].namn} ? Skriv 'q' eller 'Q' för att gå tillbaka till menyn.\n")
                
                if nummer_svar.lower() == 'q': 
                    return
                
                if not nummer_svar.isdigit():
                    print("Fel inmatning! Du får bara skriva heltal")
                else:
                    break
            
            if int(nummer_svar) == atom_lista[slumpat_index].atom_nr:
                print("Rätt svar!\n")
                break

            else:
                print("Fel svar! Försök igen\n")
                
                if försök == 2: 
                    print(f"Rätta svaret var: {atom_lista[slumpat_index].atom_nr}")


def träna_symbol(atom_lista):
    """Träningsfunktion för atombeteckningar. Interagerar med användaren för att gissa rätt symbol."""

    while True: 
        slumpat_index = random.randint(0, len(atom_lista) - 1)
        
        for försök in range(3): 

            while True:
                symbol_svar = input(f"Vad har {atom_lista[slumpat_index].namn} för symbol? Skriv 'q' eller 'Q' för att gå tillbaka till menyn\n")

                if symbol_svar.lower() == 'q': 
                    return
                
                if not symbol_svar.isalpha(): 
                    print("Du kan bara mata in bokstäver, inget annat!")
                else:
                    break 
                
            if symbol_svar == atom_lista[slumpat_index].symbol:
                print("Rätt svar!\n")
                break

            else:
                print("Fel svar! Försök igen\n")
                    
                if försök == 2: 
                    print(f"Rätta svaret var: {atom_lista[slumpat_index].symbol}")


def träna_namn(atom_lista):
    """Träningsfunktion för atomnamn. Interagerar med användaren för att gissa rätt namn."""

    while True: 
        slumpat_index = random.randint(0, len(atom_lista) - 1)
        
        for försök in range(3): 

            while True:
                namn_svar = input(f"Vad har atomnummer {(atom_lista[slumpat_index].atom_nr)} för namn ? Skriv 'q' eller 'Q' för att gå tillbaka till menyn. \n")

                if namn_svar.lower() == 'q': 
                    return
                
                if not namn_svar.isalpha(): 
                    print("Du kan bara mata in bokstäver, inget annat!")
                else:
                    break 

            if namn_svar.lower() == atom_lista[slumpat_index].namn.lower():
                print("Rätt svar!\n")
                break
            else:
                print("Fel svar! Försök igen\n")
                    
                if försök == 2: 
                    print(f"Rätta svaret var: {atom_lista[slumpat_index].namn}")


def main():
    """Main funktion för att köra all kod och funktioner, där menyvalet finns även med. """
    
    atomer = [] 

    ladda_upp(atomer) # Kör funktionen som läser in atomer från filen
    sortera_atom_nr(atomer) # Kör funktionen som sorterar atomnerna efter atomnummer
    
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
            träna_symbol(atomer)
        
        elif meny_val == "4":
            träna_namn(atomer)

        elif meny_val == "5":
            print("Avslutar programmet. Ha det bra!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

main() # Anropar main funktionen så den körs
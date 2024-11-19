"""Ett programm där avändaren kan skapa olika studenter och deras person
nummer. Felhantering finns och använder ska kunna mata in mha inputs. """

import läs_heltal # Importerar en modul som kontrollerar heltal

class Student: 
    """"En class skapar som en mall för objekten och dess attribut"""
    def __init__(self,förnamn,efternamn,personnummer):
        """ """
        self.förnamn= förnamn
        self.efternamn = efternamn
        self.personnummer= personnummer
    def __str__(self):
        return "Namn: "+self.förnamn +" "+ self.efternamn+": "+"Personnummer: "+ str(self.personnummer)
def Studenter():
    """En funktion där vi kan mata in och lägga till studenter"""
    studentlista = []  
    
    for _ in range(3):  # Fråga efter tre studenter
      # Validera förnamn
        while True:
            förnamn = input("Skriv studentens förnamn: ").strip()  # .strip() Tar bort mellanslag så att den inte anges ogiltig
            if förnamn.isalpha():   #Kontrollerar att det endast används bokstäver. Om inte skrivs texten nedan.        
                break
            print("Ogiltigt förnamn. Vänligen ange endast bokstäver.")
        
        # Validera efternamn
        while True:
            efternamn = input("Skriv studentens efternamn: ").strip() 
            if efternamn.isalpha():
                break
            print("Ogiltigt efternamn. Vänligen ange endast bokstäver.")
        
        personnummer = läs_heltal.int_input("Studentens personnummer: ")
        studentlista.append(Student(förnamn, efternamn, personnummer))  # Studenterna sparas och tillges deras attribut mha klassen.

    for person in studentlista:  # Alla stundenternas attribut radas upp.
        print(person)       

Studenter()
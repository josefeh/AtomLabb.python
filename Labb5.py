"""Ett programm där avändaren kan skapa olika studenter och deras person
nummer. Felhantering finns och använder ska kunna mata in mha inputs. Användaren ska även kunna
 söka efter studenter """

import felsökning

class Student:
    """En klass för att representera en student"""
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnummer: {self.personnummer}"


class School:
    """En klass som representerar en skola med studenter"""
    def __init__(self):
        self.students = []  # En lista som lagrar alla studentobjekt

    def lägg_till_student(self, student):
        """Lägger till en student i listan av studenter"""
        self.students.append(student)
        print(f"\nStudenten {student.förnamn} {student.efternamn} är tillagd!\n")

    def sök_student(self, sök_namn):
        """Söker efter en student baserat på förnamn"""
        hittad = False
        for student in self.students:
            if student.förnamn.lower() == sök_namn.lower():  # Gör sökningen skiftlägesokänslig
                print(f"\nDen studenten läser på KTH:\n{student}")
                hittad = True
                break
        if not hittad:
            print(f"\nIngen student med namnet {sök_namn} hittades.\n")

def skapa_studenter():
    """En funktion där vi kan mata in och lägga till studenter"""
    school = School()  # Skapa ett objekt av typen School

    antal_student = felsökning.int_input("Ange antal studenter du vill skapa: ")

    for _ in range(antal_student):
        # Validera förnamn
        förnamn=felsökning.bokstäver_input("skriv förnamn: ")
        efternamn=felsökning.bokstäver_input("skriv efternamn: ")
        
        # Personnummer
        personnummer = felsökning.int_input("Studentens personnummer: ")

        # Skapa studentobjekt
        student = Student(förnamn, efternamn, personnummer)
        school.lägg_till_student(student)

    return school  # Returnera school-objektet med alla studenter

def main():
    """Huvudprogrammet"""
    school= skapa_studenter()  # Skapa studenter och tilldela dem till ett School-objekt

    while True:
        # Låt användaren söka efter en student
        sök = input("Vilken student vill du söka efter? (Skriv 'sluta' för att avsluta): ").strip()
        if sök.lower() == "sluta":
            break
        school.sök_student(sök)

# Kör huvudprogrammet
main()
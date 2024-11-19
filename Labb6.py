"""Ett programm där avändaren kan skapa olika studenter och deras person
nummer, eller välja att läsa elever i en fil. Felhantering finns och använder ska kunna mata in mha inputs. Användaren ska även kunna
 söka efter studenter """

import felsökning 
"""Importerar en modul som utför felsökning""" 

class Student:
    """En klass för att representera en student"""
    
    def __init__(self, förnamn, efternamn, personnummer):
        """Defintion för dem olika attributen som behövs för student"""

        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __str__(self):
        """Funktion för att kunna skriva ut värdena som en sträng"""

        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnummer}"

class School:
    """En klass som representerar en skola med studenter"""
    def __init__(self):
        self.students = []  # En lista som sparar alla studentobjekt

    def lägg_till_student(self, student):
        """Lägger till en student i listan av studenter"""

        self.students.append(student)
        print(f"\nNamn: {student.förnamn} {student.efternamn} Personnummer: {student.personnummer}\n")

    def sök_student(self, sök_namn):
        """Söker efter en student baserat på förnamn"""

        hittad = False  # Definierar hittad som falskt för att senare se när vi får en student
    
        for student in self.students:  # Söker igenom alla studenter 
            if student.förnamn.lower() == sök_namn.lower():
                print(f"\nDen studenten läser på skolan:\n{student}")  # Utskrift av student
                hittad = True
                break
        if not hittad:  # Om student ej hittas
            print(f"\nIngen student med namnet {sök_namn} hittades.\n")
    
    def visa_alla_studenter(self):
        """Skriver ut alla studenter som finns i skolan"""
        print("Dessa studenter är skrivna på KTH:")
        for student in self.students:
            print(student)

    def läs_studenter_från_fil(self, filnamn):
        """Läser studentuppgifter från en fil"""
        while True:
   
            try:
                with open(filnamn, 'r', encoding='utf-8') as file:
                    content = file.read()
                    content_list = content.split("\n")
        
                    i = 0
                    while True:
                        
                        personnummer, efternamn, förnamn = content_list[i], content_list[i+1], content_list[i+2]
                        student = Student(förnamn, efternamn, personnummer)
                        self.lägg_till_student(student)
                        i += 3
                    
                        if i == len(content_list):
                            break
                break #ta bort?    
                       
            except FileNotFoundError:
                print(f"\nDen filen fanns inte: {filnamn}\n")
                filnamn = input("Skriv in ett nytt filnamn: ")
    
       
def skapa_studenter_manuellt(school):
    """Manuell inmatning av studenter"""
    antal_student = felsökning.int_input("Ange antal studenter du vill skapa: ")

    for i in range(antal_student):
        förnamn = felsökning.bokstäver_input("Skriv förnamn: ")
        efternamn = felsökning.bokstäver_input("Skriv efternamn: ")
        personnummer = felsökning.int_input("Studentens personnummer: ")

        student = Student(förnamn, efternamn, personnummer)
        school.lägg_till_student(student)

def main():
    school = School()

    # Fråga användaren om de vill skapa studenter manuellt eller läsa från fil
    val = input("Vill du mata in studenter manuellt eller läsa från fil? (Skriv 'manuellt' eller 'fil'): ").strip().lower()

    if val == 'manuellt':
        skapa_studenter_manuellt(school)
    elif val == 'fil':
        filnamn = input("Vad heter filen med alla studenter? ").strip()
        school.läs_studenter_från_fil(filnamn)
    else:
        print("Felaktigt val, avslutar programmet.")
        return
    school.visa_alla_studenter() #Visa alla studenter
    
    #Låter användaren söka efter studenter
    while True:
        sök = input("Vilken student vill du söka efter? (Skriv 'sluta' för att avsluta): ").strip()
        if sök.lower() == "sluta":
            break
        school.sök_student(sök)

main()

"c:/Users/josef/DD1310 Programmeringsteknik HT24/Labb6.py"
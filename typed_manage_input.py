'''
Author: Arvin Mardukh  Kurskod: DD1310
Välkommen till denna modul som innehåller två funktioner.
Den ena funktionen kontrollerar att användarens inmatning
är ett flyttal. Om detta inte är fallet försöker den konvertera
inmatningen till ett flyttal. Går det inte så tvingar den
användaren att skriva in ny inmatning. Andra funktionen
utför samma sak fast för heltal.
'''

import re


def input_float(objekt):
    """Funktionen ser till att angivna värdet är flyttal
       och om möjligt ändrar det till flyttal,
       samt tvingar dig att skriva om icke-flyttal
     """
    while type(objekt) != float:
        # Loop bildas tills objekt blir flyttal.
        try:
            objekt = float(input(objekt))
        except ValueError:
            print('Angivna värdet är inte ett flytttal, försök igen!')
    return objekt


def input_int(objekt):
    """Funktionen ser till att angivna värdet är heltal
       och om möjligt ändrar det till heltal,
       samt tvingar dig att skriva om icke-heltal
       :type objekt: object
     """
    while type(objekt) != int:
        # Loop bildas tills objekt blir heltal.
        try:
            objekt = int(input(objekt))
        except ValueError:
            print('Angivna värdet är inte ett heltal, försök igen!')
    return objekt


def validate_name(text):
    """
    Funktionen kontrollerar att både för- och efternamn matas in av användaren.
    Parametern är texten som skrivs när användaren frågas om namn.
    """
    while True:
        try:
            name = input(text).title().strip()  # Gör första bokstaven stor och tar bort blankslag

            # Kontrollera att namnet innehåller minst ett mellanslag och endast giltiga bokstäver
            if re.fullmatch(r"[A-Za-zÅÄÖåäö]+ [A-Za-zÅÄÖåäö]+", name):
                return name
            else:
                print('Fel! Ange ett giltigt namn enligt formatet: Förnamn Efternamn\nFörsök igen!')

        except ValueError:
            print('Du skrev fel, försök igen!\n')


def validate_phonenumber(text):
    """
    Funktionen kontrollerar att användaren skriver in telefonummer
       med heltal och rätt antal siffor.
       parametern är texten som skrivs när användaren frågas om telefonnummer.
       """
    while True:
        try:
            phonenumber = int(input(text))
            if len(str(phonenumber)) < 11:  # Kontrollerar att telefonnumret innehåller 11 siffor.
                print('För få siffror, telefonnummer innehåller 11 siffror. Försök igen!\n')
            elif len(str(phonenumber)) > 11:
                print('För många siffror telefonnummer innehåller 11 siffror. Försök igen\n')
            else:
                int(phonenumber)  # Gör om inmatningen till heltal.
                return phonenumber

        except ValueError:  # Kontrollerar att telefonnumret endast innehåller heltal.
            print('Telefonnumret ska skrivas med heltalssiffror. Försök igen!\n')

def validate_email(text):
    """
    Funktionen kontrollerar att email är skrivet med korrekt format.
    """
    while True:
        try:
            email = input(text).strip().lower()  # Tar bort onödiga mellanslag och gör om till små bokstäver
            if re.fullmatch(r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+", email):
                return email
            else:
                print('Fel! Skriv enligt formatet: exempel@domän.xx\nFörsök igen!\n')
        except ValueError:
            print('Du skrev fel, försök igen!\n')


def validate_address(text):
    """
    Funktionen kontrollerar att adressen är skriven i korrekt format.
    Format: Gata (första bokstaven stor, resten små) följt av ett mellanslag och siffror.
    """
    while True:
        try:
            address = input(text).strip()
            if re.fullmatch(r"[A-Za-zÅÄÖåäö]+ \d+", address):
                address = address.title()  # Första bokstaven stor, resten små
                return address
            else:
                print('Fel! Skriv enligt formatet: Gatan 123\nFörsök igen!\n')
        except ValueError:
            print('Du skrev fel, försök igen!\n')



def validate_search(phonebook):
    """Funktionen validerar sökandet av ett email, nummer eller namn.
       Om denna uppgift finns i listorna som innehåller kontaktuppgifterna
       så returneras indexet för den inmatade uppgiften. Parametrarna är listorna
       som innehåller emails, nummer, förnamn och efternamn för telfonregistret.
       """
    while True:  # Loopen pågår tills användaren skriver in email, nummer eller namn som finns i telefonregistret.
        try:
            search = input('Skriv namn, telefonnummer eller email på person du vill hitta: ')
            search = search.strip()  # Tar bort blankslag i början och slut.
            if search.__contains__(' '):  # Om inmatning innehåller blankslag söker vi efter namn i telefonregistret.
                search = search.title()  # Gör om så varje ord börjar med stor bokstav.
                split_first_and_last_name = search.split()
                first_name = split_first_and_last_name[0]
                last_name = split_first_and_last_name[1]
                # Separerar inmatning till för och efternamn.

                if first_name in first_name_ls and last_name in last_name_ls and \
                   first_name_ls.index(first_name) == last_name_ls.index(last_name):
                    name_index = first_name_ls.index(first_name)
                    # Undersöker om det inmatade är ett existerande förnamn och efternamn
                    # och att dessa tillhör samma kontakt.
                    return name_index  # Returnerar index för namnet.

                else:  # Ifall inmatningen inte är ett existerande namn.
                    print('Namnet finns inte på telefonregistret. Försök igen! \n')

            elif search in phonenumber_ls:  # Undersöker om inmatningen är ett existernade telefonnummer.
                phonenumber_index = phonenumber_ls.index(search)
                return phonenumber_index  # Returnerar index för telefonnumret.

            elif search in email_ls:  # Undersöker om inmatningen är ett existerande email.
                email_index = email_ls.index(search)
                return email_index  # Returnerar index för emailet.

            else:  # Ifall inmatningen inte är ett existerande namn, nummer eller mail.
                print('Denna kontaktuppgift finns inte. Försök igen! \n')

        except ValueError:
            print('Denna kontaktuppgift finns inte. Försök igen! \n')



def validate_search(text, first_name_ls, last_name_ls, phonenumber_ls, email_ls):
    """
    Funktionen söker efter en student via namn, telefonnummer eller email.
    Returnerar index för matchad student.
    """
    while True:
        search = input(text).strip()

        # Sök via namn (för- och efternamn)
        if ' ' in search:
            split_name = search.split()
            if len(split_name) == 2:
                first_name, last_name = split_name
                if first_name in first_name_ls and last_name in last_name_ls:
                    index = first_name_ls.index(first_name)
                    if last_name_ls[index] == last_name:  # Dubbelkoll att efternamnet matchar
                        return index
            print('Namnet finns inte. Försök igen!\n')

        # Sök via telefonnummer
        elif search.isdigit():  # Kollar om inmatningen bara är siffror
            search = str(search)  # Säkerställer att både `search` och listans värden är strängar
            if search in map(str, phonenumber_ls):
                return list(map(str, phonenumber_ls)).index(search)
            print('Telefonnumret finns inte. Försök igen!\n')

        # Sök via e-post
        elif search in email_ls:
            return email_ls.index(search)

        else:
            print('Denna kontaktuppgift finns inte. Försök igen!\n')












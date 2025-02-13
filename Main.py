from Phonebook_class import Student, School
from typed_manage_input import (
    validate_name,
    validate_phonenumber,
    validate_email,
    validate_search,
    validate_address
)


def main():
    school = School()

    while True:
        print("\n--- STUDENTREGISTER ---")
        print("1. Lägg till student")
        print("2. Sök student")
        print("3. Visa alla studenter")
        print("4. Avsluta")

        val = input("Välj alternativ: ").strip()

        if val == '1':
            # Validera input
            name = validate_name("Namn (Förnamn Efternamn): ")
            first_name, last_name = name.split()
            phonenumber = validate_phonenumber("Telefonnummer (11 siffror): ")
            email = validate_email("Email: ")
            address = validate_address("Adress: ")

            # Skapa student och lägg till i skolan
            student = Student(
                first_name,
                last_name,
                phonenumber,
                email,
                address
            )
            school.add_student(student)
            print("\nStudent tillagd!")

        elif val == '2':
            if not school.students:
                print("Inga studenter registrerade.")
                continue

            # Sök efter student via valideringsfunktion
            index = validate_search(
                "Sök (namn, telefonnummer eller email): ",
                school.first_names,
                school.last_names,
                school.phonenumbers,
                school.emails
            )
            student = school.students[index]
            print("\nHITTAD STUDENT:")
            print(student)

        elif val == '3':
            students = school.get_all_students()
            if not students:
                print("Inga studenter registrerade.")
            else:
                print("\nALLA STUDENTER:")
                for student in students:
                    print(student)

        elif val == '4':
            print("Avslutar...")
            break

        else:
            print("Ogiltigt val. Försök igen.")


if __name__ == "__main__":
    main()
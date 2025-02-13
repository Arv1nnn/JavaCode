class Student:
    """Klass för att lagra och hantera studenters kontaktuppgifter."""

    def __init__(self, first_name, last_name, phonenumber, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phonenumber = phonenumber
        self.email = email
        self.address = address

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} | "
            f"Telefon: {self.phonenumber} | "
            f"Email: {self.email} | "
            f"Adress: {self.address}"
        )


class School:
    """Klass för att hantera en lista med studenter."""

    def __init__(self):
        self.students = []
        self.first_names = []
        self.last_names = []
        self.phonenumbers = []
        self.emails = []
        self.addresses = []

    def add_student(self, student):
        """Lägger till en student och uppdaterar globala listor."""
        self.students.append(student)
        self.first_names.append(student.first_name)
        self.last_names.append(student.last_name)
        self.phonenumbers.append(student.phonenumber)
        self.emails.append(student.email)
        self.addresses.append(student.address)

    def get_all_students(self):
        """Returnerar alla studenter."""
        return self.students
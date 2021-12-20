from datetime import date
class Contact:
    def __init__(self, id, first_name, last_name, birth_date, profession) -> None:
        self.ID = id
        self.first_name = first_name
        self.last_name = last_name
        self.b_date = birth_date
        self.profession = profession
    def get_information(self):
        print(f"ID - {self.ID} Full name - {self.first_name} {self.last_name} Birth Date - {self.b_date} Profession - {self.profession}")

c = Contact(id=1, first_name='John', last_name='Dow', birth_date=date(day=21, month=4, year=1996), profession='Python developer')
d = Contact(id=2, first_name='Nick', last_name='Jones', birth_date=date(day=11, month=3, year=1991), profession='JS developer')
c.get_information()
d.get_information()
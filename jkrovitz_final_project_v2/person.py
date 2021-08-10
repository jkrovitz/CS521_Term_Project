class Person:
    """
    A representation of a person
    Attributes:
        Firstname(string)
        Lastname(String)
    """

    def __init__(self, person_id, firstname, lastname):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname

    def show_full_name(self):
        return str(self.person_id) + ' ' + self.firstname + ' ' + self.lastname

    @classmethod
    def get_user_input(cls):
        while 1:
            try:
                person_id = int(input('Enter person_id: '))
                firstname = input('Enter first name: ')
                lastname = input('Enter last name: ')
                return cls(person_id, firstname, lastname)
            except ValueError as e:
                print('Invalid input!')
                continue


# creating a person object and returning their full name
person3 = Person.get_user_input()
print(person3.show_full_name())

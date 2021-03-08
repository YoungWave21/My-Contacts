import random


class Contacts:
    def __init__(self):
        self.list = [
            {"Name": "James Bond", "Number": random.randint(pow(10, 9), pow(10, 10)), "Email": "jamesbond@gmail.com"},
            {"Name": "John Doe", "Number": random.randint(pow(10, 9), pow(10, 10)), "Email": "doeJohn@gmail.com"},
            {"Name": "Donald Trump", "Number": random.randint(pow(10, 9), pow(10, 10)), "Email": "MAGATrump@gmail.com"}
        ]

    def new_contact(self):
        self.list.append({"Name": input("Name: "), "Number": input("Number: "), "Email": input("Email: ")})

    def remove_contact(self):
        name = input("Type the Name of the contact you would like to delete:")
        selected_index = self.select(name)
        if selected_index is not None:
            self.list.pop(selected_index)
        else:
            print("Contact unrecognised")

    def display_all(self):
        for i in range(len(self.list)):
            print(f'{i + 1}.')
            print(f"   Name: {self.list[i]['Name']}")
            print(f"   Number: {self.list[i]['Number']}")
            print(f"   Email: {self.list[i]['Email']}")

    def select(self, name):
        for i in range(len(self.list)):
            if name == self.list[i]["Name"]:
                return i

    def edit(self):
        name = input("Type the Name of the contact you would like to edit: ")
        selected_index = self.select(name)
        if selected_index is not None:
            self.list.pop(selected_index)
        else:
            print("Contact unrecognised")
        self.new_contact()

    def search(self):
        name = input(f'Type the Name you would like to search: ')
        index = self.select(name)
        if index is not None:
            print("Match found!")
            print(f"   Name: {self.list[index]['Name']}")
            print(f"   Number: {self.list[index]['Number']}")
            print(f"   Email: {self.list[index]['Email']}")
        else:
            print("Contact unrecognised")


def main():
    people = Contacts()
    while True:
        print("______________________________")
        print("Main Menu:")
        print("1.Display Contact Names")
        print("2.Search for Contact")
        print("3.Edit Contact")
        print("4.New Contact")
        print("5.Remove Contact")
        print("6.Exit")
        print("______________________________")
        choice = input("Your choice: ")
        if choice.isnumeric() and 0 < int(choice) < 7:
            options = {
                1: people.display_all,
                2: people.search,
                3: people.edit,
                4: people.new_contact,
                5: people.remove_contact,
                6: exit,
            }
            options[int(choice)]()
        else:
            print("The option you have selected does not exist!")


main()

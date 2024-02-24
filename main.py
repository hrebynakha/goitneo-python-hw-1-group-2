"""
The Python bot helper
"""

from datetime import datetime
from datetime import timedelta
from collections import defaultdict

users_list = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Same Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Cat Ivan", "birthday": datetime(2022, 2, 25)},
    {"name": "Cat Kus", "birthday": datetime(2022, 2, 27)},
    {"name": "Cat Kokos", "birthday": datetime(2022, 2, 27)},
    {"name": "Dog Ivan", "birthday": datetime(2022, 2, 27)},
    {"name": "Dog Kus", "birthday": datetime(2022, 2, 26)},
    {"name": "Dog Kokos", "birthday": datetime(2022, 2, 27)},
    {"name": "Tig  Van", "birthday": datetime(2022, 2, 28)},
    {"name": "Tig  Ivan", "birthday": datetime(2022, 3, 1)},
    {"name": "Tig  Kus", "birthday": datetime(2022, 3, 2)},
    {"name": "Tig  Kokos", "birthday": datetime(2022, 3, 3)},
    {"name": "Tig  Fan", "birthday": datetime(2022, 3, 4)},
    {"name": "Panda  Fan", "birthday": datetime(2022, 3, 4)},
    {"name": "Panda  Kus", "birthday": datetime(2022, 3, 5)},
    {"name": "Panda  Kokos", "birthday": datetime(2022, 3, 6)},
    {"name": "Panda  Ivan", "birthday": datetime(2022, 3, 7)},
    {"name": "Panda  Cat", "birthday": datetime(2022, 3, 7)},
    {"name": "Panda  Dog", "birthday": datetime(2022, 3, 8)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
]


def get_birthdays_per_week(users):
    """Return names of users that you need to greet with birstday"""
    days_of_birthday = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year.weekday() in range(5, 7):
                days_to_append = 7 % birthday_this_year.weekday()
                birthday_this_year = birthday_this_year + timedelta(days=days_to_append)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            day_of_week = birthday_this_year.strftime("%A")
            days_of_birthday[day_of_week] += [name]

    for day, users_to_greet in days_of_birthday.items():
        print(f"{day}:", end=" ")
        print(*users_to_greet, sep=", ")


def parse_input(user_input):
    """Parse user inputed commands"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """Add contacts to contact ditictionary"""
    name, phone = args
    if name in contacts:
        return f"Warning: already exist. {change_contact(args, contacts)}"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Update contact in contacts ditictionary"""
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact updated."
    return f"Contact with name {name} not found. You can add it by command add <name> <number>"


def show_phone(name, contacts):
    """Show phone by name"""
    name = name[0]
    if name in contacts.keys():
        return contacts[name]
    return f"Contact with name {name} not found."


def show_all(contacts):
    """Show all conatacts"""
    info = ""
    for name, phone in contacts.items():
        info += f"{name}: {phone}\n"
    return info.removesuffix("\n")


def main():
    """Main function"""
    # get_birthdays_per_week(users_list)
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            print("Invalid input!")
            continue
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

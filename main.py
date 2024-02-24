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

def main():
    """Main function"""
    get_birthdays_per_week(users_list)


if __name__ == "__main__":
    main()

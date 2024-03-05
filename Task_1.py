from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # data preparation
    birthday_dict = defaultdict(list)

    # retrieval of the current date
    today = datetime.today().date()

    # sorting users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date() 

        # date type converting (sets the year of birth to the current year)
        birthday_this_year = birthday.replace(year = today.year)

        # evaluating the date for this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        # comparision with the current date
        delta_days = (birthday_this_year - today).days

        # determining the day of the week
        if delta_days <7:
            day_of_week = (today + timedelta(days = delta_days)).strftime("%A")
            
            # check the weekends
            if delta_days >= 0:
                if day_of_week in ["Saturday", "Sunday"]:
                    day_of_week = "Monday"

    # storing the result
    birthday_dict[day_of_week].append(name)           

    # print result
    for day, names in birthday_dict:
        print(f"{day}: {', '.join(names)}")


# Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)}
]

get_birthdays_per_week(users)
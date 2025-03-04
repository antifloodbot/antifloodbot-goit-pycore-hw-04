import datetime

def get_upcoming_birthdays(users):

    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        birth_date = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birth_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() in [5, 6]:
                birthday_this_year += datetime.timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
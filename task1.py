import datetime

def get_days_from_today(date_str: str) -> int:

    try:
        given_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError as e:
        raise ValueError("Невірний формат дати. Використовуйте формат 'РРРР-ММ-ДД'") from e

    today = datetime.date.today()
    days_difference = (today - given_date).days
    return days_difference
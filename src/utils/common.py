from datetime import date

from src.constants import TESTING


def get_today_date():
    if not TESTING:
        return date.today()
    else:
        return date(2020, 1, 1)

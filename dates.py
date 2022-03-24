from datetime import datetime, timedelta
from pytz import timezone
import constants


def get_leaves_to_be_added_last_month(values: list):
    last_and_first_days_of_previous_month = get_last_and_first_days_of_previous_month()
    last_day_of_previous_month = last_and_first_days_of_previous_month[0]
    first_day_of_previous_month = last_and_first_days_of_previous_month[1]

    first_day_of_previous_month_string = first_day_of_previous_month.strftime(constants.DATE_FORMAT)

    print(last_day_of_previous_month)
    print(first_day_of_previous_month_string)

    for value in values:
        if value[0] == first_day_of_previous_month_string:
            print(f'Leaves to be added: {value[1]}')
            return int(value[1])

    return 0


def get_last_and_first_days_of_previous_month():
    # This needs to be commented out when running the module on cloud
    first_day_of_current_month = datetime.strptime('2022-04-01', constants.DATE_FORMAT)
    first_day_of_current_month = first_day_of_current_month.replace(hour=8, minute=0, second=0)

    # Instead, this has to uncommented
    # first_day_of_current_month = datetime.now(timezone('Asia/Kolkata'))

    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
    first_day_of_previous_month = last_day_of_previous_month.replace(day=1, hour=0, minute=0, second=0)

    print(last_day_of_previous_month)
    print(first_day_of_previous_month)

    return [last_day_of_previous_month, first_day_of_previous_month]

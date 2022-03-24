import constants
from database import database_connection
from dates import get_last_and_first_days_of_previous_month, get_leaves_to_be_added_last_month
from writers import Writer
from spreadsheets import month_end_sheet, calendar_details_sheet


def main(data, context):
    db_rows = database_connection.return_word_count_last_month(get_last_and_first_days_of_previous_month())
    Writer.instantiate_from_db_list(db_rows)
    print(Writer.all_writers)

    spreadsheet_values = Writer.return_month_end_spreadsheet_values()
    month_end_sheet.clear_values(constants.MONTH_END_SHEET_RANGE)
    month_end_sheet.update_values(constants.MONTH_END_SHEET_RANGE, spreadsheet_values)
    Writer.create_surplus_cards()

    leave_rows = calendar_details_sheet.get_values(constants.LEAVE_ADDITION_SHEET_RANGE)
    leave_count = get_leaves_to_be_added_last_month(leave_rows)
    Writer.update_leaves(leave_count)

    # Database needs to be updated for additional leaves
    # leave_values = Writer.return_leaves_db_list()
    # database_connection.update_leaves(leave_values)


if __name__ == '__main__':
    main('', '')

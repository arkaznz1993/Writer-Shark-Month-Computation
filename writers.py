import requests

import constants


class Writer:
    all_writers = []
    surplus_deficit_writers = []

    def __init__(self, trello_id, name, sum_word_count, sum_target, daily_word_count, leaves):
        self.trello_id = trello_id
        self.name = name
        self.sum_word_count = int(sum_word_count)
        self.sum_target = int(sum_target)
        self.difference = self.sum_word_count - self.sum_target
        self.daily_word_count = int(daily_word_count)
        self.leaves = int(leaves)
        self.card_id = None

        if abs(self.difference) < self.daily_word_count:
            Writer.surplus_deficit_writers.append(self)

        Writer.all_writers.append(self)

    def __repr__(self):
        return f"Writer('{self.trello_id}', '{self.name}', '{self.sum_target}', '{self.sum_word_count}', " \
               f"'{self.daily_word_count}', '{self.leaves}') "

    @staticmethod
    def instantiate_from_db_list(rows):
        for row in rows:
            Writer(row[0], row[1], row[2], row[3], row[4], row[5])

    @staticmethod
    def return_month_end_spreadsheet_values():
        values = []
        for writer in Writer.all_writers:
            if writer.sum_target > 0 or writer.sum_word_count > 0:
                values.append([writer.name, writer.sum_word_count, writer.sum_target, writer.daily_word_count,
                               writer.difference])

        return values

    @staticmethod
    def update_leaves(leave_count):
        for writer in Writer.all_writers:
            writer.leaves += leave_count

    @staticmethod
    def return_leaves_db_list():
        values = []
        for writer in Writer.all_writers:
            values.append([writer.leaves, writer.trello_id])

        return values

    @staticmethod
    def create_surplus_cards():
        for writer in Writer.surplus_deficit_writers:
            params = constants.PARAMS.copy()
            params['name'] = writer.name
            params['idMembers'] = [writer.trello_id]
            response = requests.request(
                "POST",
                constants.CREATE_CARD_URL,
                headers=constants.HEADERS,
                params=params
            )

            writer.card_id = response.json()['id']

        for writer in Writer.surplus_deficit_writers:
            url = f'https://api.trello.com/1/cards/{writer.card_id}/customField/{constants.SURPLUS_CUSTOM_FIELD_ID}/item'
            params = constants.PARAMS.copy()
            params['value'] = {"number": str(writer.difference)}
            response = requests.request(
                "PUT",
                url,
                headers=constants.HEADERS,
                json=params
            )

            print(response.text)

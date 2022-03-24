import os
import mysql.connector
from mysql.connector.constants import ClientFlag

# Instance name - flash-hour-338103:asia-south1:test-sql-server

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': '35.200.140.194',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': os.environ.get('SSL_CA'),
    'ssl_cert': os.environ.get('SSL_CERT'),
    'ssl_key': os.environ.get('SSL_KEY'),
    'database': os.environ.get('DB_NAME'),
}


SELECT_WORD_COUNT_TARGET_LAST_MONTH = 'SELECT Writers.TrelloId, Writers.Name, SUM(WeeklyTarget.WordCount), ' \
                                      'SUM(WeeklyTarget.Target), Writers.DailyWordCount, Writers.Leaves ' \
                                      'FROM Writers JOIN WeeklyTarget ON Writers.TrelloId = WeeklyTarget.TrelloId ' \
                                      'WHERE WeeklyTarget.WeekStart < %s ' \
                                      'AND WeeklyTarget.WeekStart >= %s ' \
                                      "AND Writers.WriterStatus = 'Current' " \
                                      'GROUP BY Writers.TrelloId;'

UPDATE_LEAVES = 'UPDATE Writers ' \
                'SET Leaves = %s ' \
                'WHERE TrelloId = %s;'


class DatabaseConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def return_word_count_last_month(self, values: list):
        self.cursor.execute(SELECT_WORD_COUNT_TARGET_LAST_MONTH, values)
        return self.cursor.fetchall()

    def update_leaves(self, values: list):
        self.cursor.executemany(UPDATE_LEAVES, values)
        self.connection.commit()


database_connection = DatabaseConnector()

from sqlite3 import Error
import sqlite3, traceback

class Database:

    def __init__(self, file: str, show=False):
        self.file = file
        self.connection = self.get_connection()
        self.show = show

    def log_error(self, error_message, full_error):
        print(f'{self.file}.db : {error_message}')
        print(full_error, "\n")

    def get_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(f'database/{self.file}.db')
        except Error as e:
            self.log_error(e, traceback.format_exc())
        return connection

    def execute(self, query, args=()):
        if self.show:
            print(f'{self.file}.db \t |', query)
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            result = cursor.execute(query, args)
            connection.commit()
            if "SELECT" in query:
                cols = []
                for column in result.description:
                    cols.append(column[0])
                raw_rows = result.fetchall()
                rows = []
                for row in raw_rows:
                    rows.append(dict(zip(cols, row)))
                return rows
            connection.close()
        except Error as e:
            connection.close()
            if "CREATE" not in query:
                self.log_error(e, traceback.format_exc())
        
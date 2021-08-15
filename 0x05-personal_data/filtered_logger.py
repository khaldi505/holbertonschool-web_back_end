#!/usr/bin/env python3
"""
filter_datum returns the log message:
"""
from typing import List
import logging
import re
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")
PERSONAL_DATA_DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME")
PERSONAL_DATA_DB_PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD")
PERSONAL_DATA_DB_USERNAME = os.getenv("PERSONAL_DATA_DB_USERNAME")
PERSONAL_DATA_DB_HOST = os.getenv("PERSONAL_DATA_DB_HOST")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        todo
        """
        logging.basicConfig(format=self.FORMAT, level=logging.INFO)
        return (self.filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
            ))

    def filter_datum(self,
                     fields: List[str],
                     redaction: str,
                     message: str,
                     separator: str
                     ) -> str:
        """
        a function that hides all the personal,
        sensitve informations.
        """
        for field in fields:
            message = re.sub("{}=(.*?){}".format(field, separator),
                             field + "=" + redaction + separator,  message)
        return message


def get_logger() -> logging.Logger:

    """
        get some logging done
    """
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    logger.propagate = False
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
        get sql db
    """
    connection = mysql.connector.connect(
                                    user=PERSONAL_DATA_DB_USERNAME,
                                    password=PERSONAL_DATA_DB_PASSWORD,
                                    host=PERSONAL_DATA_DB_HOST,
                                    database=PERSONAL_DATA_DB_NAME
                                    )
    return connection


def main():
    """
        main
    """

    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("select * from users")
    record = cursor.fetchall()
    for row in record:
        for coloumn in row:
            print(coloumn)

    cursor.close()
    connection.close()

    return


if __name__ == '__main__':
    main()

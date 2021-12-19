import sys
import mysql.connector
from mysql.connector import Error
from loguru import logger
from datetime import date
from datetime import datetime

from src.settings_getter import get_settings_in_dict


def initialize_logger():
    LOG_FILE_EXTENSION = ".log"
    SETTINGS = get_settings_in_dict()
    logger.add(
        sys.stderr,
        colorize=True,
        format="{time} {level} {message}",
        filter="my_module",
        level="INFO",
    )
    day = date.today()
    log_filename = day.strftime("%b-%d-%Y") + LOG_FILE_EXTENSION
    logger.add(SETTINGS["LOG_DIRECTORY"] + log_filename)


def insert_log_to_db(message):
    try:
        # get connection info
        db_info = get_settings_in_dict()["DB_INFO"]
        login, passwd, host, database, table = (
            db_info["login"],
            db_info["passwd"],
            db_info["host"],
            db_info["database"],
            db_info["table"],
        )
        # perform connection
        connection = mysql.connector.connect(
            host=host, database=database, user=login, password=passwd
        )
        if connection.is_connected():
            logger.debug(f"Connected to {database} in {host}")
            db_info = connection.get_server_info()
            logger.debug(f"MySQL server version is: {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logger.debug(f"connected to db: {record}")
            # insert log
            today = date.today()
            timestamp = f"{today.year}-{today.month}-{today.day} {datetime.now().strftime('%H:%M:%S')}"
            insert_query = f"insert into {table} (timestamp, log) values ('{timestamp}', '{message}');"
            cursor.execute(insert_query)
            connection.commit()
            logger.debug(
                f"{cursor.rowcount} Record inserted successfully into {table} table"
            )

    except Error as err:
        logger.error(
            "Error while establishing connection or inserting data: " + str(err)
        )
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logger.debug("MySQL connection is closed")


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()

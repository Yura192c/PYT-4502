import psycopg2
import os
import json
from typing import Union



class DatabaseManager:
    def __init__(self, room_file, students_file) -> None:
        """Initialize the DatabaseManager.

        Args:
            room_file (str): The path to the JSON file containing room data.
            students_file (str): The path to the JSON file containing students data.
        """
        self.host = os.environ['POSTGRES_HOST']
        self.port = os.environ['POSTGRES_PORT']
        self.database = os.environ['POSTGRES_DB']
        self.user = os.environ['POSTGRES_USER']
        self.password = os.environ['POSTGRES_PASSWORD']
        self.conn = None

        self.room_file = room_file
        self.students_file = students_file

    def connect(self):
        ''' 
        Create connection to database
        '''
        try:
            self.conn = psycopg2.connect(host=self.host,
                                         port=self.port,
                                         database=self.database,
                                         user=self.user,
                                         password=self.password)
            return True
        except Exception as e:
            print("Error connecting to database:", e)
            self.disconnect()
            return False

    def disconnect(self) -> None:
        """Disconnect from the database."""
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def execute_query(self, query, vars=None) -> Union[list, None]:
        """Execute a SQL query.

        Args:
            query (str): The SQL query to execute.
            vars (tuple, optional): The variables to substitute into the query.

        Returns:
            list: A list of tuples containing the query results.
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query, vars)
            return cur.fetchall()

        except Exception as e:
            return None

        finally:
            cur.close()

    def create_tables(self) -> None:
        """Create database tables if they do not exist."""
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS room (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255)
            )
        """)
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                birthday DATE,
                sex CHAR(1),
                room_id INTEGER REFERENCES room(id)
            )
        """)

    # TODO это неадекват
    def insert_data_from_json(self) -> None:
        """Insert data from JSON files into the database."""
        with open(f'{self.room_file}', 'r') as file:
            rooms_data = json.load(file)
            for room in rooms_data:
                self.execute_query(
                    "INSERT INTO room (id, name) VALUES (%s, %s)", (room['id'], room['name']))

        with open(f'{self.students_file}', 'r') as file:
            students_data = json.load(file)
            for student in students_data:
                self.execute_query("INSERT INTO students (id, name, birthday, sex, room_id) VALUES (%s, %s, %s, %s, %s)",
                                   (student['id'], student['name'], student['birthday'], student['sex'], student['room']))

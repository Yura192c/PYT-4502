import unittest
import psycopg2
from unittest.mock import patch, MagicMock
from database.db_manager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManager(
            room_file='data/rooms.json', students_file='data/students.json')
        self.db_manager.conn = MagicMock()

    def test_connect_success(self):
        self.assertTrue(self.db_manager.connect())

    @patch('psycopg2.connect')
    def test_connect_failure(self, mock_connect):
        mock_connect.side_effect = psycopg2.Error
        self.assertFalse(self.db_manager.connect())

    def test_disconnect(self):
        self.db_manager.disconnect()
        self.db_manager.conn.commit.assert_called_once()
        self.db_manager.conn.close.assert_called_once()

    @patch('json.load')
    @patch.object(DatabaseManager, 'execute_query')
    def test_insert_data_from_json(self, mock_execute_query, mock_json_load):
        mock_json_load.side_effect = [
            [{'id': 1, 'name': 'Room 1'}, {
                'id': 2, 'name': 'Room 2'}],  # Data for rooms
            [{'id': 1, 'name': 'Student 1', 'birthday': '1990-01-01',
                'sex': 'M', 'room': 1}]  # Data for students
        ]
        self.db_manager.insert_data_from_json()
        mock_execute_query.assert_any_call(
            "INSERT INTO room (id, name) VALUES (%s, %s)", (1, 'Room 1'))
        mock_execute_query.assert_any_call(
            "INSERT INTO room (id, name) VALUES (%s, %s)", (2, 'Room 2'))
        mock_execute_query.assert_any_call("INSERT INTO students (id, name, birthday, sex, room_id) VALUES (%s, %s, %s, %s, %s)",
                                           (1, 'Student 1', '1990-01-01', 'M', 1))

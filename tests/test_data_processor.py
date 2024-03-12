import unittest
from unittest.mock import MagicMock
from database.data_processor import DataProcessor
import datetime


class TestDataProcessor(unittest.TestCase):

    def test_process_room_list_data(self):
        rows = [(1, 'Room 1', 5), (2, 'Room 2', 3)]
        expected_result = [
            {'id': 1, 'room_name': 'Room 1', 'student_count': 5},
            {'id': 2, 'room_name': 'Room 2', 'student_count': 3}
        ]

        result = DataProcessor.process_room_list_data(rows)
        self.assertEqual(result, expected_result)

    def test_process_rooms_avg_lowest_age_data(self):
        rows = [(661, 'Room #661', 10.667), (913, 'Room #913', 18.333),]
        expected_result = [{'id': 661, 'name': 'Room #661', 'avg_age': 10.667}, {
            'id': 913, 'name': 'Room #913', 'avg_age': 18.333}]

        result = DataProcessor.process_rooms_avg_lowest_age_data(rows)
        self.assertEqual(result, expected_result)

    def test_process_room_avg_biggest_age_data(self):
        rows = [(712, datetime.timedelta(days=42161)),
                (875, datetime.timedelta(days=42100))]
        expected_result = [{
            "id": 712,
            "age_difference": "42161 days, 0:00:00"
        },
            {
            "id": 875,
            "age_difference": "42100 days, 0:00:00"
        },]

        result = DataProcessor.process_room_avg_biggest_age_data(rows)
        self.assertEqual(result, expected_result)

    def test_process_rooms_opposite_sexes_data(self):
        rows = [(1, 'Room 1'), (2, 'Room 2')]
        expected_result = [
            {'id': 1, 'room_name': 'Room 1'},
            {'id': 2, 'room_name': 'Room 2'}
        ]

        result = DataProcessor.process_rooms_opposite_sexes_data(rows)
        self.assertEqual(result, expected_result)

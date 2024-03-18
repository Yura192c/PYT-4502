import unittest
from unittest.mock import patch, MagicMock
import os
from database.output_manager import OutputManager


class TestOutputManager(unittest.TestCase):
    @patch('builtins.open')
    def test_save_to_json(self, mock_open):
        data = [{'id': 1, 'name': 'Room A', 'details': 'Some details'},
                {'id': 2, 'name': 'Room B'}]
        filename = 'test_data'

        OutputManager.save_to_json(data, filename)

        mock_open.assert_called_once_with(f'{filename}.json', 'w')

        mock_file = MagicMock()
        mock_open.return_value = mock_file

    def test_save_to_xml(self):
        data = [{'id': 1, 'name': 'Room A', 'details': 'Some details'},
                {'id': 2, 'name': 'Room B'}]
        filename = 'test_data'

        OutputManager.save_to_xml(data=data, filename=filename)
        with open(f'{filename}.xml', 'r') as f:
            actual_xml = f.read()
        expected_xml = """<rooms><room id="1"><name>Room A</name><details>Some details</details></room><room id="2"><name>Room B</name></room></rooms>"""

        self.assertEqual(actual_xml, expected_xml)
        os.remove(f'{filename}.xml')

    def test_save_to_json_invalid_data_type(self):
        with self.assertRaises(TypeError) as context:
            data = "This is a string, not a list"
            filename = 'test_data'
            OutputManager.save_to_json(data, filename)

    def test_save_to_xml_invalid_data_type(self):
        with self.assertRaises(TypeError):
            data = "This is a string, not a list"
            filename = 'test_data'
            OutputManager.save_to_xml(data, filename)

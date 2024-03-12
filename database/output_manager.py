import json
import xml.etree.ElementTree as ET


class OutputManager:
    """A utility class to manage output formats.

    This class provides static methods for saving data to JSON and XML formats.

    Attributes:
        None
    """

    @staticmethod
    def save_to_json(data: list, filename: str) -> None:
        """Save data to a JSON file.

        Args:
            data (dict): The data to be saved.
            filename (str): The name of the JSON file to save.

        Returns:
            None
        """

        if not isinstance(data, list):
            raise TypeError('Data must be a list.')

        with open(f'{filename}.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def save_to_xml(data: list, filename: str) -> None:
        """Save data to an XML file.

        Args:
            data (list): The data to be saved.
            filename (str): The name of the XML file to save.

        Returns:
            None
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        root = ET.Element("rooms")
        for room in data:
            room_element = ET.Element("room", attrib={"id": str(room['id'])})
            for key, value in room.items():
                if key not in ('id',):
                    element = ET.Element(key)
                    element.text = str(value)
                    room_element.append(element)
            root.append(room_element)
        tree = ET.ElementTree(root)
        tree.write(f"{filename}.xml")

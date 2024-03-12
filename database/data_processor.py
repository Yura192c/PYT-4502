class DataProcessor:
    @staticmethod
    def process_room_list_data(rows) -> list:
        """Process data for room list.

        Args:
            rows (list): List of tuples representing room data from the database query.

        Returns:
            list: List of dictionaries containing processed room data.
        """
        room_list = []
        for row in rows:
            room_list.append({
                'id': row[0],
                'room_name': row[1],
                'student_count': row[2]
            })
        return room_list

    @staticmethod
    def process_rooms_avg_lowest_age_data(rows) -> list:
        """Process data for rooms with lowest average age.

        Args:
            rows (list): List of tuples representing room data from the database query.

        Returns:
            list: List of dictionaries containing processed room data with average age.
        """
        room_list = []
        for row in rows:
            room_list.append({
                'id': row[0],
                'name': row[1],
                'avg_age': float(row[2])
            })
        return room_list

    @staticmethod
    def process_room_avg_biggest_age_data(rows) -> list:
        """Process data for rooms with biggest age difference.

        Args:
            rows (list): List of tuples representing room data from the database query.

        Returns:
            list: List of dictionaries containing processed room data with age difference.
        """
        room_list = []
        for row in rows:
            room_list.append({
                'id': row[0],
                'age_difference': str(row[1])
            })
        return room_list

    @staticmethod
    def process_rooms_opposite_sexes_data(rows) -> list:
        """Process data for rooms with students of opposite sexes.

        Args:
            rows (list): List of tuples representing room data from the database query.

        Returns:
            list: List of dictionaries containing processed room data with opposite sexes.
        """
        room_list = []
        for row in rows:
            room_list.append({
                'id': row[0],
                'room_name': str(row[1])
            })
        return room_list

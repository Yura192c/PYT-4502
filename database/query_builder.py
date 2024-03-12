class QueryBuilder:
    @staticmethod
    def build_room_list_query() -> str:
        return """
            SELECT room.id, room.name AS room_name, COUNT(students.id) AS student_count
            FROM room
            LEFT JOIN students ON room.id = students.room_id
            GROUP BY room.id, room.name
            ORDER BY room.id;
        """

    @staticmethod
    def build_rooms_avg_lowest_age_query() -> str:
        return """
            SELECT room.id, room.name AS room_name, ROUND(AVG(EXTRACT(YEAR FROM AGE(NOW(), students.birthday))), 3) AS avg_age
            FROM room
            LEFT JOIN students ON room.id = students.room_id
            GROUP BY room.id, room.name
            ORDER BY avg_age
            LIMIT 5;
        """

    @staticmethod
    def build_rooms_avg_biggest_age_query() -> str:
        return """
        SELECT room_id, age(MAX(birthday), MIN(birthday)) AS age_difference
        FROM students
        GROUP BY room_id
        ORDER BY age_difference DESC
        LIMIT 5;
        """

    @staticmethod
    def build_rooms_opposite_sexes_query() -> str:
        return """
        SELECT DISTINCT s.room_id, r.name AS room_name
        FROM students s
        INNER JOIN room r ON s.room_id = r.id
        GROUP BY s.room_id, r.name
        HAVING COUNT(DISTINCT s.sex) > 1;
        """

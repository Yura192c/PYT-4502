from arg_parser import ArgumentParser
from database.db_manager import DatabaseManager
from database.query_builder import QueryBuilder
from database.data_processor import DataProcessor
from database.output_manager import OutputManager


if __name__ == "__main__":
    args = ArgumentParser.parse_args()

    db_manager = DatabaseManager(
        room_file=args.room, students_file=args.students)
    if db_manager.connect():
        try:
            db_manager.create_tables()
            db_manager.insert_data_from_json()

            query = None
            match args.fetch:
                case 'room_list':
                    query = QueryBuilder.build_room_list_query()
                case 'rooms_avg_lowest_age':
                    query = QueryBuilder.build_rooms_avg_lowest_age_query()
                case 'rooms_avg_biggest_age':
                    query = QueryBuilder.build_rooms_avg_biggest_age_query()
                case 'rooms_opposite_sexes':
                    query = QueryBuilder.build_rooms_opposite_sexes_query()
                case _:
                    query = ''

            if query:
                rows = db_manager.execute_query(query)
                if rows:
                    if args.fetch == 'room_list':
                        room_list = DataProcessor.process_room_list_data(rows)
                    match args.fetch:
                        case 'room_list':
                            room_list = DataProcessor.process_room_list_data(
                                rows)
                        case 'rooms_avg_lowest_age':
                            room_list = DataProcessor.process_rooms_avg_lowest_age_data(
                                rows)
                        case 'rooms_avg_biggest_age':
                            room_list = DataProcessor.process_room_avg_biggest_age_data(
                                rows)
                        case 'rooms_opposite_sexes':
                            room_list = DataProcessor.process_rooms_opposite_sexes_data(
                                rows)
                        case _:
                            room_list = []

            match args.format:
                case 'json':
                    OutputManager.save_to_json(room_list, args.output_filename)
                case 'xml':
                    OutputManager.save_to_xml(room_list, args.output_filename)

        finally:
            db_manager.disconnect()

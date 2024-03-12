import argparse

FORMAT_CHOICES = ['room_list', 'rooms_avg_lowest_age',
                  'rooms_avg_biggest_age', 'rooms_opposite_sexes']


class ArgumentParser:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description='Fetch data from PostgreSQL.')

        parser.add_argument('--format', choices=['json', 'xml'],
                            default='json', help='Output format (json or xml)')
        parser.add_argument(
            '--fetch', choices=FORMAT_CHOICES, help='Database queries')
        parser.add_argument('--output_filename', type=str, default='data',
                            help="Name of ouput file")
        parser.add_argument('--room',
                            help='Path to file room.json')
        parser.add_argument('--students',
                            help='Path to file students.json')

        return parser.parse_args()

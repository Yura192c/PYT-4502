# Python Task#1
Script uses docker to run Postgresql, so to run it you must have docker and docker-compose installed locally 



### Run script
* Start PosgreSQL
```sh
docker-compose up
```

* Connection to databse
```sh
psql -h localhost -p 5432 -U admin -d innodb
```

* Start script
```sh
python main.py
```

* Default parameters:
```sh
  -h, --help            show this help message and exit
  --format {json,xml}   Output format (json or xml)
  --fetch {room_list,rooms_avg_lowest_age,rooms_avg_biggest_age,rooms_opposite_sexes}
                        Database queries
  --output_filename OUTPUT_FILENAME
                        Name of ouput file
  --room ROOM           Path to file room.json
  --students STUDENTS   Path to file students.json
```

Example script commands
```sh
python main.py --fetch room_list --room data/rooms.json --students data/students.json --format xml

python main.py --fetch rooms_avg_lowest_age --room data/rooms.json --students data/students.json --format xml

python main.py --fetch rooms_avg_biggest_age --room data/rooms.json --students data/students.json --format xml

python main.py --fetch rooms_opposite_sexes --room data/rooms.json --students data/students.json --format xml

```

 After using the script, run

```shell
docker-compose down -v
```

to stop Postgresql container
*** Note ***

docker-compose for upping PostgreSQL database with pgAdmin
```
docker-compose up
```

Connection to databse
```
psql -h localhost -p 5432 -U admin -d innodb
```

Script commands
```
python main.py --fetch room_list --room data/rooms.json --students data/students.json --format xml

python main.py --fetch rooms_avg_lowest_age --room data/rooms.json --students data/students.json --format xml

python main.py --fetch rooms_avg_biggest_age --room data/rooms.json --students data/students.json --format xml

python main.py --fetch rooms_opposite_sexes --room data/rooms.json --students data/students.json --format xml

```
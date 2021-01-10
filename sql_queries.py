# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays; "
user_table_drop     = "DROP TABLE IF EXISTS users;"
song_table_drop     = "DROP TABLE IF EXISTS songs;"
artist_table_drop   = "DROP TABLE IF EXISTS artists;"
time_table_drop     = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
 songplay_id serial not null primary key,
 start_time time not null,
 user_id varchar not null,
 level varchar not null,
 song_id varchar not null,
 artist_id varchar not null,
 session_id int not null,
 location varchar ,
 user_agent varchar 
 )
""")

user_table_create = ("""
 CREATE TABLE IF NOT EXISTS users (
  user_id varchar not null  primary key,
  first_name varchar ,
  last_name varchar not null,
  gender varchar not null,
  level varchar not null
 )
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
 song_id varchar not null  primary key,
 title varchar not null,
 artist_id varchar not null,
 year int not null,
 duration float not null
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
 artist_id varchar not null  primary key,
 name varchar not null,
 location varchar,
 latitude float not null,
 longitude float not null
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
 start_time time not null  primary key,
 hour int not null,
 day varchar not null,
 week int not null, 
 month int not null,
 year int not null,
 weekday varchar not null
)
""")

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO songs (song_id,title,artist_id,year,duration)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT(song_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users( user_id,first_name, last_name, gender,level)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT(user_id) DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id,title,artist_id,year,duration)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists( artist_id,name,location,latitude,longitude)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT(artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time,hour,day,week,month,year,weekday)
VALUES (%s,%s,%s,%s,%s,%s,%s)
""")

songplay_table_insert = ("""
INSERT INTO songplays (start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")
# FIND SONGS

song_select = ("""
SELECT s.song_id,a.artist_id
FROM artists a
INNER JOIN songs s ON a.artist_id = s.artist_id
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
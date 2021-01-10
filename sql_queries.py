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
 user_id varchar(25) not null,
 level varchar(10) not null,
 song_id varchar(20) not null,
 artist_id varchar(20) not null,
 session_id int not null,
 location varchar(300) ,
 user_agent varchar(300),
 CONSTRAINT  fk_start_time FOREIGN KEY(start_time) REFERENCES time(start_time), 
 CONSTRAINT  fk_user_id FOREIGN    KEY(user_id)    REFERENCES users(user_id), 
 CONSTRAINT  fk_artist_id FOREIGN  KEY(artist_id)  REFERENCES artists(artist_id)
 );
""")

user_table_create = ("""
 CREATE TABLE IF NOT EXISTS users (
  user_id varchar(20) not null  primary key,
  first_name varchar(30) ,
  last_name varchar(30) not null,
  gender varchar(5) not null,
  level varchar(10) not null
 )
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
 song_id varchar(20) not null  primary key,
 title varchar(100) not null,
 artist_id varchar(20) not null,
 year int not null,
 duration float not null
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
 artist_id varchar(20) not null  primary key,
 name varchar(150) not null,
 location varchar(300),
 latitude float not null,
 longitude float not null
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
 start_time time not null  primary key,
 hour int not null,
 day varchar(20) not null,
 week int not null, 
 month int not null,
 year int not null,
 weekday varchar(20) not null
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
ON CONFLICT(user_id) DO UPDATE SET level = EXCLUDED.level;
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

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
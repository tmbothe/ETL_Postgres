# Project: Data Modeling and ETL with Postgres and Python
## Project Description

A compagny that has been collecting songs' data and users activity wants an efficient model to store and analyze the data. The data currently resides in folders in JSON format.
This project consists of creating a database and build an ETL pipeline to store the data.
This will help the analytics to analyze and derive insights from data.

## Data description
There are two sources of dataset, the **Song Dataset** and the **Log Dataset** . 
### The Song Dataset
This is a collection of JSON data that store songs data. The files are partitioned by the three letters of of each song's track ID. These are two examples:
 - **song_data/A/B/C/TRABCEI128F424C983.json**
 - **song_data/A/A/B/TRAABJL12903CDCF1A.json**
 
 Each file is structured as:
 
 {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

### Log Dataset

The second dataset is a set of JSON log files generated by an event similator base of songs dataset above. These files simulate activity logs partitioned by year and month as we can see below:

- **log_data/2018/11/2018-11-12-events.json**
- **log_data/2018/11/2018-11-13-events.json**

## Choice of Data Model

For this project, we will building a star model with fact and dimension tables. This schema is analytic focus as all dimensions tables are one join away from that fact tables that easier queries retrieval. Here is tables description:

**Fact Table**

    1 - songplays - records in log data associated with song plays i.e. records with page NextSong
         songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
         
**Dimension Tables**

    2 - users - users in the app
         user_id, first_name, last_name, gender, level 
    3 - songs - songs in music database
         song_id, title, artist_id, year, duration
    4- artists - artists in music database
        artist_id, name, location, latitude, longitude
    5- time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday
        
 ![image](https://github.com/tmbothe/ETL_Postgres/blob/main/images/datamodel.PNG)




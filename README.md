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

## Choice of Data Model

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


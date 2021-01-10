import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    This function processes songs files, extract and load in artist table and song table.
    all duplicates rows are removed.
    The data are first loaded in a pandas dataframe, then process and inserted in postgres tables. 
    
    """
    # open song file
    df = pd.read_json(filepath,lines=True) 
      
    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']].drop_duplicates(subset=['song_id']).values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude','artist_longitude']].drop_duplicates(subset=['artist_id']).values[0].tolist()
    
    if len(artist_data[0])>0:
        cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
     This function processes log file and populates the tables below:
     - time
     - user
     - songplay
     The data are first loaded in a pandas dataframe, then process and inserted in postgres tables. 
    """
    # open log file
    df =  pd.read_json(filepath,lines=True) 

    # filter by NextSong action
    df['dtime']=pd.to_datetime(df.ts).dt.time

    # convert timestamp column to datetime
    t = pd.DataFrame(pd.to_datetime(df.ts))
    t['timestamp'] = t.ts.dt.time
    t['hour']  = t.ts.dt.hour
    t['day']   = t.ts.dt.day
    t['week']  = t.ts.dt.week
    t['month'] = t.ts.dt.month
    t['year']  = t.ts.dt.year
    t['weekday'] = t.ts.dt.weekday
    
    # insert time data records
    #time_data = t.v
    #column_labels = 
    time_df = t.iloc[:,1:].drop_duplicates(subset=['timestamp'],keep=False)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']].drop_duplicates(subset=['userId'])
    
    # remove all rows with null userId
    user_df = user_df[user_df['userId'].notna()]
    
    # insert user records
    for i, row in user_df.iterrows():
        if len(str(row.userId))>0:
            cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        
        start_time = row.dtime
        # insert songplay record
        songplay_data = (start_time,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    This function read files from the folder and process line by line.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))
    
    #print(f"The function is {func} the path is {filepath},the current is {cur}=====>")

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
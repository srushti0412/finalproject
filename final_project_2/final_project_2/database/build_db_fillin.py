import pathlib
import sqlite3
import pandas as pd

path = pathlib.Path().cwd() # use pathlib to get current working directory

def create_db(db_name, filename, table_name):
    file_path = path / filename # create a path to the data file

    con = sqlite3.connect(f'../website/{db_name}') # create a connection to the database
    cursor = con.cursor() # create a cursor

    winequality_red = pd.read_csv(file_path) # read in the data 
    # insert the data into the specified table 
    winequality_red.to_sql(table_name,con,index=False, if_exists='replace')
    # execute a select statement as f-string and print results to verify insertion
    rows = cursor.execute(f"SELECT * FROM {table_name} LIMIT 15").fetchall()
    print(rows)
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()

if __name__=="__main__":
    db_name = "winequality_red.db"
    filename = "winequality_red.csv"
    table_name = "winequality_red"
    create_db(db_name, filename, table_name)

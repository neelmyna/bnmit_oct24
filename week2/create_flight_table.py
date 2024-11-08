import sqlite3

def connect_db():
    conn = sqlite3.connect('flights_db.db')
    return conn

def create_table_flights():
    query = 'create table IF NOT EXISTS flights(id integer primary key AUTOINCREMENT, airline varchar(30) not null, source varchar(30) not null, destination varchar(30) not null, duration float, fare int)'
    conn = connect_db()
    conn.execute(query)
    conn.close()

create_table_flights()
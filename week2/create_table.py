import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def create_table():
    query = 'create table phones(id int primary key auto_increment, make varchar(30) not null, model varchar(30) not null, price float, ram tinyint, memory smallint);'
    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        my_cursor.execute(query)
        print('Table created')
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while creating the table')
    except:
        print('database disconnection failed')

create_table()

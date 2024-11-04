import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def insert_row():
    query = """insert into phones(make, model, price, ram, memory) values('samsung', 's25 pro', 153000, 12, 1024)"""

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        my_cursor.execute(query)
        connection.commit()
        print('Row inserted')
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while inserting the row')
    except:
        print('database disconnection failed')

insert_row()

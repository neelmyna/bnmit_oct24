import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def list_all_rows():
    query = 'select * from phones'

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query)
        if numberOfRows == 0:
            print('No rows were retrieved from phones')
        else:
            rows = my_cursor.fetchall()
            print('ID   MAKE      MODEL          PRICE     RAM-SIZE  MEMORY')
            print('-' * 56)
            for row in rows:
                print('%-4d %-9s %-14s %-9.1f %-9d %d'%(row[0], row[1], row[2], row[3], row[4], row[5]))
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

list_all_rows()
import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def search_row():
    query = 'select * from phones where id = %s'
    id = int(input('Enter Id to search the phone: '))

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query, id)
        if numberOfRows == 0:
            print(f'phone with Id={id} was not found')
        else:
            row = my_cursor.fetchone()
            print('ID   MAKE      MODEL          PRICE     RAM-SIZE  MEMORY')
            print('-' * 56)
            print('%-4d %-9s %-14s %-9.1f %-9d %d'%(row[0], row[1], row[2], row[3], row[4], row[5]))
        my_cursor.close()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

search_row()
# the search_row function will run
import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def delete_row():
    query = 'delete from phones where id = %s'
    id = int(input('Enter Id to delete the phone: '))

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query, id)
        if numberOfRows == 0:
            print(f'phone with Id={id} was not found')
        else:
            print(f'phone with Id={id} was deleted')
        my_cursor.close()
        connection.commit()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

delete_row()
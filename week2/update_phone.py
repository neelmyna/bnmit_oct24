import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def update_row():
    query = 'update phones set price = %s where id = %s'
    phone_id = int(input('Enter Id of the phone to be updated: '))
    new_price = float(input('Enter new price of the phone: '))
    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        numberOfRows = my_cursor.execute(query, (new_price, phone_id))
        if numberOfRows == 0:
            print(f'phone with Id={phone_id} was not found')
        else:
            print(f'phone with Id={phone_id} was updated')
        my_cursor.close()
        connection.commit()
        disconnect_db(connection)
    except pymysql.err.DatabaseError as e:
        print(e)
        print('Some error occured while reading the rows')
    except:
        print('database disconnection failed')

update_row()
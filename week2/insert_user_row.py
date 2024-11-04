import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

def read_user_data():
    make = input('Enter the phone company name: ')
    model = input('Enter the phone model name: ')
    price = float(input('Enter the phone price: '))
    ram = int(input('Enter the phone RAM size: '))
    memory = int(input('Enter the phone Disk size: '))
    return (make, model, price, ram, memory)

def insert_row():
    query = """insert into phones(make, model, price, ram, memory) values(%s, %s, %s, %s, %s)"""

    try:
        connection = connect_db()
        my_cursor = connection.cursor()
        phone = read_user_data()
        my_cursor.execute(query, phone)
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

import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db1', port=3306, charset='utf8')
    print('database connected')
    return connection    

def disconnect_db(connection):
    connection.close()
    print('database disconnected')

connection = connect_db()
disconnect_db(connection)

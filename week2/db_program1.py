import pymysql

connection = pymysql.Connect(host='localhost', user='root', password='Root123', database='Nithin_db', port=3306, charset='utf8')

print('database connected')
connection.close()
print('database disconnected')
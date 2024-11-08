
# connecting to the DB using pymysql module
import sys
import pymysql

class DbOperationException(Exception):
    pass

class GameDataOperations:
    def connectDb(self):
        conn = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root123',
            db='nithin_db', charset='utf8')
        print('Database connected successfully')
        return conn

    def disConnectDb(self, connection):
        connection.close()
        print('Database disconnected')

    def createTable(self):
        createTableQuery = 'create table IF NOT EXISTS games(id int primary key auto_increment, name varchar(50) not null, price int, constraint new check(price % 100 = 0), mininum_players int default(1), maximum_players int default(11), description varchar(1000));'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(createTableQuery)
            if returnValue != 0:
                raise DbOperationException
            print('Return value = ', returnValue)
            connection.commit()    
        except DbOperationException:
            print('Error while creating the table ABC')
        except pymysql.err.OperationalError:
            print('Error while creating the table XYZ')
        except:
            print('Error in connecting to the database')
        finally:
            cursor.close()
            self.disConnectDb(connection)
            
    def createDb(self):
        createDbQuery = 'create database IF NOT EXISTS bnmit_db'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(createDbQuery)
            cursor.close()
        except:
            print('Error in connecting to the database')

    def readGameData(self, operation):
        name = input('Enter name of the Game: ')
        price = int(input('Enter Price of the Game (per head): '))
        minPlayers = int(input('Enter minimum number of players: '))
        maxPlayers = int(input('Enter maximum number of players: '))
        if operation == 'insert':
            print('Enter Description of the Game, Use Ctrl+Z to stop: ')
            sys.stdin.flush()
            description = sys.stdin.read()
            description = description.replace('\n', ' ').strip()
            return (name, price, minPlayers, maxPlayers, description)
        id = int(input('Enter Id of the Game to update: '))
        return (name, price, minPlayers, maxPlayers, id)

    def createGame(self):
        insertQuery = 'insert into games(name, price, mininum_players, maximum_players, description) values(%s, %s, %s, %s, %s)'
        gameObject = self.readGameData('insert')
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(insertQuery, gameObject)
            print('Return Value = ', returnValue)
            if returnValue != 1:
                raise DbOperationException
            connection.commit()
            print('Row inserted successfully')
            cursor.close()
            self.disConnectDb(connection)
        except DbOperationException:
            print('Error while inserting a row')
        except pymysql.err.OperationalError:
            print('Row Insert failed')
        except pymysql.err.ProgrammingError:
            print('Invalid insert command given')
        except Exception as e:
            print(e)
            print('Some Unknown Error occured')

    def updateGame(self):
        updateQuery = 'update games set name = %s, price = %s, mininum_players = %s, maximum_players = %s where id = %s'
        gameObject = self.readGameData('update')
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(updateQuery, gameObject)
            connection.commit()
            if returnValue != 1:
                print(f'Game with id = {gameObject[4]} not found')
            else:
                print('Row update successful')
            cursor.close()
            self.disConnectDb(connection)
        except:
            print('Row Update failed')

    def deleteGame(self):
        id = int(input('Enter Id of the Game to be deleted: '))
        updateQuery = f'delete from games where id = {id}'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            returnValue = cursor.execute(updateQuery)
            connection.commit()
            if returnValue != 1:
                print(f'Game with id = {id} not found')
            else:
                print('Row delete successful')
            cursor.close()
            self.disConnectDb(connection)
        except:
            print('Row Delete failed')

    def searchGame(self):
        id = int(input('Enter Id of the Game to be searched: '))
        searchQuery = f'select * from games where id = {id}'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            numberOfRows = cursor.execute(searchQuery)
            if numberOfRows == 0:
                print(f'Game with id = {id} not found')
            else:
                row = cursor.fetchone()
                print('Game Details is: \n', str(row))
            #connection.commit()
            cursor.close()
            self.disConnectDb(connection)
        except pymysql.err.DataError:
            print('Row Search failed')

    def listGames(self):
        query = f'select * from games'
        try:
            connection = self.connectDb()
            cursor = connection.cursor()
            numberOfRows = cursor.execute(query)
            connection.commit()
            rows = cursor.fetchall()
            if rows is None:
                print(f'Game with id = {id} not found')
            else:
                for row in rows:
                    print('Game Details is: \n', str(row))
            cursor.close()
            self.disConnectDb(connection)
        except pymysql.err.DataError:
            print('Row Listing failed')

class Menu:
    def __init__(self, gameOperations):
        self.gameOperations = gameOperations

    def exitProgram(self):
        exit('End of the program')

    def invalidInput(self):
        print('Invalid choice entered')

    def getMenu(self):
        menu = {
            1 : self.gameOperations.createGame,
            2 : self.gameOperations.searchGame,
            3 : self.gameOperations.updateGame,
            4 : self.gameOperations.deleteGame,
            5 : self.gameOperations.listGames,
            6 : self.gameOperations.createTable,
            7 : self.exitProgram
        }
        return menu

    def runMenu(self):
        menu = self.getMenu()
        while True:
            print('\n 1:Create 2:Search 3:Update 4:Delete 5:ListAll 6:CreateTable 7:Exit \n Your choice: ')
            choice = int(input())
            menu.get(choice, self.invalidInput)()

def startApp():
    operations = GameDataOperations()
    menu = Menu(operations)
    menu.runMenu()

startApp()
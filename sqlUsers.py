import psycopg2

class SqlUsers:

    def add(user):
        try:
            connect = psycopg2.connect(database = "recipesPage",
                             host = "localhost",
                             user = "postgres",
                             password = "1234",
                             port = "5432"
                            )
            cursor = connect.cursor()
            addQuery = """INSERT INTO TABLE users (userId SERIAL PRIMARY KEY, userName TEXT NOT NULL, mail TEXT NOT NULL, pin TEXT NOT NULL)"""
            cursor.execute(addQuery, user.name, user.mail, user.mail, user.pin)
        except:
            print('Ocorreu um erro')
        finally:
            cursor.close()
            connect.close()

    def login(userName, userPassword):
        try:
            connect = psycopg2.connect(database = "recipesPage",
                             host = "localhost",
                             user = "postgres",
                             password = "1234",
                             port = "5432"
                            )
            cursor = connect.cursor()
            
            
            loginQuery = """SELECT * FROM users WHERE userName = %s """
            cursor.execute(loginQuery, (userName,))
            permission = False
            actualUser = cursor.fetchall()
            
            userTuple = actualUser[0]

            if actualUser:
                if userTuple[3] == userPassword:
                    permission = True
                    userInfo = permission, userTuple[0], userTuple[1]
                    return userInfo
                else: 
                    permission = False
                    print('Credenciais erradas')
                    return permission
            else:
                print('Credenciais erradas')
        except:
            print("")
        finally:
            cursor.close()
            connect.close()


# class User:
#     def __init__(self, userId,userName,mail,pin ):
#         self.userId = userId
#         self.username = userName
#         self.mail=mail
#         self.pin = pin


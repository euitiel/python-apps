import psycopg2


class SqlRecipes:
   

    def add(recipe):
        try:
            connect = psycopg2.connect(database = "recipesPage",
                             host = "localhost",
                             user = "postgres",
                             password = "1234",
                             port = "5432"
                            )
            cursor = connect.cursor()
            addQuery = """INSERT INTO recipes (
                        name,
                        imageId,
                        ingredients,
                        description,
                        instructions,
                        userId) VALUES (%s, %s, %s, %s, %s, %s);"""
            cursor.execute (addQuery,(
                            recipe.name,
                            recipe.imageId,
                            recipe.ingredients,
                            recipe.description,
                            recipe.instructions,
                            recipe.userId) )
            connect.commit()
            
        except: 
            print('Erro ao adicionar')
        finally: 
            cursor.close()
            connect.close()


    def delete(recipe):
        try:
            connect = psycopg2.connect(database = "recipesPage",
                         host = "localhost",
                         user = "postgres",
                         password = "1234",
                         port = "5432"
                         )
            deleteQuery = "DELETE FROM recipes WHERE name = %s"
            cursor = connect.cursor()
            cursor.execute (deleteQuery, (recipe.name))
            connect.commit()
        except:
            print('Erro ao deletar')
        finally:
            cursor.close()
            connect.close()

    def select(id):
        try:
            connect = psycopg2.connect(database = "recipesPage",
                             host = "localhost",
                             user = "postgres",
                             password = "1234",
                             port = "5432"
                            )
            cursor = connect.cursor()
            selectQuery = "SELECT * FROM recipes WHERE recipeid = %s"
            cursor.execute(selectQuery, (id,))
            return cursor.fetchall()
        except ValueError as e:
            print('Erro ao buscar receitas',e)
        finally: 
            cursor.close()
            connect.close()

# class Recipe:
#     def __init__(self, name, imageId, ingredients, description, instructions, userId):
#         self.name = name
#         self.imageId = imageId
#         self.ingredients = ingredients
#         self.description = description
#         self.instructions = instructions
#         self.userId = userId

# receita = Recipe('Panqueca',1, 'ovos, farinha, leite e fermento', 'panqueca estilo americana','misture os ingredientes e asse em uma frigideira',1)
# print(SqlRecipes.select(receita))




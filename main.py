import flet as ft
from flet import *
from sqlRecipe import SqlRecipes
from sqlUsers import SqlUsers

def main (page: ft.Page):
    page.scroll='auto'
    page.bgcolor = '#0000'
    
    recipeid = 8
    result = SqlRecipes.select((recipeid))
    
    listResults = result[0]
    recipeName = listResults[1]
    discriptionText = listResults[4]
    ingredientsText = listResults[3]
    instructionsText = listResults[5]
    permission = False
    loggedUserId = ""
    loggedUserName = "Login"

    def login(e):
        nonlocal permission, loggedUserId, loggedUserName
        username = usernameField.value
        password = passwordField.value
        userInfo = SqlUsers.login(username, password)
        permission = userInfo[0]
        loggedUserId = userInfo[1]
        loggedUserName = userInfo[2]
        loginButton.text = loggedUserName
        loginButton.update()
        passwordField.value = ""
        usernameField.value = ""
        logoutButton.visible = True
        logoutButton.update()
        closeLogin(e)

    def closeLogin(e): 
        alert.open = False 
        page.update()
    
    alert = AlertDialog(#modal
        title= Text('Login'),
        content= ft.Column(
            controls=[
                Text('Login'),
                usernameField := ft.TextField(label="Nome de usuário"),
                passwordField := ft.TextField(label= "Senha", password = True),
                ft.ElevatedButton(text= "Login", on_click = login),
                ft.ElevatedButton(text="Cancelar", on_click= closeLogin),            
                ]
        )
                 
    )

    def openLogin(e):
        nonlocal permission, loggedUserId, loggedUserName
        if permission == False:
            page.dialog = alert
            alert.open = True
            page.update()
        else:
           ...

    def logOut(e):
        nonlocal permission, loggedUserId, loggedUserName
        permission = False
        loggedUserId = ""
        loginButton.text = 'Login'
        logoutButton.visible = False
        logoutButton.update()
        loginButton.update()

    def changeMainImage(e): 
        for elem in options.controls:
            if elem == e.control:
                elem.opacity=1
                mainImage.src = elem.image_src
            else: elem.opacity =0.5
        mainImage.update()
        options.update()

    header = ft.Container(
        padding=20,
        bgcolor = '#ffffff',
        content = ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                
                ft.Image( #imagem de logo, trocar depois
                    col={'xs':6, 'md':3},
                    src='https://i.pinimg.com/736x/3d/63/0e/3d630e7c96d574c2cf8d8f164b50c493.jpg',
                    width=200,
                    height=200,
                ),
                ft.Column(
                    col={'xs':6, 'md':3},
                    controls=[
                        loginButton :=ft.ElevatedButton(
                    width=150,
                    text = loggedUserName,
                    on_click= openLogin,
                    style = ft.ButtonStyle(
                        padding=ft.padding.all(5),
                    
                    )    
                ),
                    logoutButton :=ft.ElevatedButton(
                    width=150,
                    text= "Sair",
                    on_click = logOut,
                    visible=False,
                    style = ft.ButtonStyle(
                        padding=ft.padding.all(5),
                        ),
                )                                    
                        
                    ]
                )
            ]
        )
    )
    recipeImages = ft.Container(
        col={'xs':12, 'md':6},
        bgcolor='#ffffff',
        padding=ft.padding.all(30),
        aspect_ratio=9/12,
        content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[

                

                mainImage:=ft.Image( 
                    src='https://www.comidaereceitas.com.br/wp-content/uploads/2021/11/golden-corn-syrup-drizzling-onto-pancakes-780x520.jpg',
                ),
                options:=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://www.comidaereceitas.com.br/wp-content/uploads/2021/11/golden-corn-syrup-drizzling-onto-pancakes-780x520.jpg',
                            width=100,
                            height=100,
                            opacity=1,
                            on_click= changeMainImage
                        ),
                        ft.Container(
                            image_src='https://nutritotal.com.br/publico-geral/wp-content/uploads/2021/02/receita-da-panqueca-americana-2.jpg',
                            width=100,
                            height=100,
                            opacity=0.5,
                            on_click= changeMainImage
                        ),
                        ft.Container(
                            image_src='https://www.receitas-do-mundo.com/wp-content/uploads/2019/01/receita-de-panqueca-americana.jpg',
                            width=100,
                            height=100,
                            opacity=0.5,
                            on_click= changeMainImage
                        ),
                    ]
                )
            ]
        )
    )
    recipeDetails = ft.Container(
        col={'xs':12, 'md':6},
        padding=ft.padding.all(30),
        bgcolor='#a2a2a2',
        aspect_ratio=9/12,
        content=ft.Column(
            controls=[
                ft.Text(
                    value=recipeName,
                    color='#ffffff',
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Descrição:',
                    size=24
                ),
                ft.Text(
                    value= discriptionText
                ),
                ft.Text(
                    value='Ingredientes:',
                    size=24,
                ),
                ft.Text(
                    value=ingredientsText
                ),
                ft.Text(
                    value='Modo de preparo:',
                    size=24
                ),
                ft.Text(
                    value=instructionsText
                ),
            ]
        )
    )

    layout = ft.Container(
        #alignment=ft.MainAxisAlignment.CENTER,
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color='#ffbf00'),
        content = ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                header,
                recipeImages,
                recipeDetails,
            ]

        )

    )



    page.add(layout)
    page.update()
if __name__ =='__main__':
    ft.app (target = main)
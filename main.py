from flet import *

def hello(e):
    print("button work")
    if e.control.text=="login":
        print("open page to log in")
    elif e.control.text=="create account":
        print("open page to create account")
    elif e.control.text=="contact us":
        print("open page to contact support")

def icon_click(e):
    print("icon cliked")

def click_item(e):
    print("list tile item clicked")
    if e.control.subtitle.value=="les conceptes de base":
        print("hello les conceptes de base")
    elif e.control.subtitle.value=="les operations courantes":
        print("hello les operations courantes")
    elif e.control.subtitle.value=="les travaux d'inventaire":
        print("hello les travaux d'inventaire")
    
        
           

def main(page:Page):
    page.window.width=450
    page.window.left=750

    page.appbar=AppBar(
        center_title=True,
        title=Text("programation app",size=12),
        leading=Icon(icons.PALETTE),#ajout d'icon
        leading_width=40, # ajout espace a gauche element de app bar cad icon
        bgcolor=colors.AMBER,
        actions=[
            IconButton(icons.AD_UNITS,on_click=icon_click),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="login",on_click=hello),
                    PopupMenuItem(text="create account",on_click=hello),
                    PopupMenuItem(text="contact us",on_click=hello),
                ]
            )
        ]
        
    )

    page.add(
        ListTile(
            title=Text("Comptabilite",size=12),
            leading=Icon(icons.PLAY_LESSON),
            subtitle=Text("les conceptes de base",size=12),
            on_click=click_item
        ),
        ListTile(
            title=Text("Comptabilite",size=12),
            leading=Icon(icons.PLAY_LESSON),
            subtitle=Text("les operations courantes",size=12),
            on_click=click_item
        ),
        ListTile(
            title=Text("Comptabilite",size=12),
            leading=Icon(icons.PLAY_LESSON),
            subtitle=Text("les travaux d'inventaire",size=12),
            on_click=click_item
        )
    )
    page.update()

app(main)
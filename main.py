from flet import *

def hello(e):
    print("button work")
    if e.control.text=="item 1":
        print("item 1 clicked")
    elif e.control.text=="item 2":
        print("item  2 clicked")
    elif e.control.text=="item 3":
        print("item 3 clicked")

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
        title=Text("programation app"),
        leading=Icon(icons.PALETTE),#ajout d'icon
        leading_width=40, # ajout espace a gauche element de app bar cad icon
        bgcolor=colors.AMBER,
        actions=[
            IconButton(icons.AD_UNITS,on_click=icon_click),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="item 1",on_click=hello),
                    PopupMenuItem(text="item 2",on_click=hello),
                    PopupMenuItem(text="item 3",on_click=hello),
                ]
            )
        ]
        
    )

    page.add(
        ListTile(
            title=Text("Comptabilite"),
            leading=Icon(icons.PLAY_LESSON),
            subtitle=Text("les conceptes de base"),
            on_click=click_item
        ),
        ListTile(
            title=Text("Comptabilite"),
            leading=Icon(icons.PLAY_LESSON),
            subtitle=Text("les operations courantes"),
            on_click=click_item
        ),
        ListTile(
            title=Text("Comptabilite"),
            leading=Icon(icons.PLAY_LESSON),
            subtitle=Text("les travaux d'inventaire"),
            on_click=click_item
        )
    )
    page.update()

app(main)
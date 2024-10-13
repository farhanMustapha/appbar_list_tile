from flet import *

def hello(e):
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
        print("upgrade to get acces")
    elif e.control.subtitle.value=="les operations courantes":
        print("hello les operations courantes")
    elif e.control.subtitle.value=="les travaux d'inventaire":
        print("hello les travaux d'inventaire")
    
    

def main(page:Page):
    page.window.width=450
    page.window.left=750
    #page.window.title_bar_hidden=True

    def login_page(e):
        page.clean()
        pw_input=TextField(label="pass word",password=True)
        email_input=TextField(label="Email")
        btn_login=ElevatedButton("login")
        page.add(
            pw_input,
            email_input,btn_login
        )
        page.update()

    def create_account_page(e):
        page.clean()
        fullName_input=TextField(label="Full Name  ")
        email_input=TextField(label="Email")
        pw_input=TextField(label="pass word",password=True)
        pw_confirm_input=TextField(label="pass word",password=True)
        btn_create_acc=ElevatedButton("Create ")
        page.add(
            fullName_input,
            email_input,pw_input,pw_confirm_input,btn_create_acc
        )
        page.update()

    def contact_us_page(e):
        def send_msg(e):
            if msg_input.value=="":
                print("please entrer ta message")
            else:
                print("votre message envoyer avec succes")

        def open_wtsup(e):
            page.launch_url("https://wa.me/212668773310")

        page.clean()
        msg_input=TextField(label="message",multiline=True,min_lines=5)
        btn_send=ElevatedButton("send",on_click=send_msg)
        btn_wtsup=ElevatedButton("wtsup",icon=icons.FACEBOOK,on_click=open_wtsup)
        row_btn=Row(
            controls=[
                btn_send,btn_wtsup
            ]
        )
        page.add(
            msg_input,
            row_btn
        )
        page.update()

    page.appbar=AppBar(
        center_title=True,
        title=Text("programation app",size=12),
        leading=Icon(icons.HOME),#ajout d'icon
        leading_width=40, # ajout espace a gauche element de app bar cad icon
        bgcolor=colors.AMBER,
        actions=[
            #IconButton(icons.AD_UNITS,on_click=icon_click),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="login",on_click=login_page),
                    PopupMenuItem(text="create account",on_click=create_account_page),
                    PopupMenuItem(text="contact us",on_click=contact_us_page),
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
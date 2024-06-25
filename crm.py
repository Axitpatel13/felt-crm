import flet as ft

def main(page: ft.Page):
    page.title = "Simple CRM App"    
    answer = ft.Column()
    def add_btn(e):
        answer.controls.append(ft.Text(f"Name: {name.value},\nEmail: {email.value}"))
        with open("output.txt", "a") as file:
            file.write(f"Name: {name.value}, Email: {email.value}\n")
        answer.controls.append(ft.Text("The name and email have been entered successfully!", color=ft.colors.GREEN))    
        name.value = ""
        email.value = ""
        page.update()
    name = ft.TextField(label="Enter Name: ", autofocus=True)
    email = ft.TextField(label="Enter Email: ")
    page.add(
        name,
        email,
        ft.Row(
            [
                ft.ElevatedButton("Add Customer", on_click=add_btn)
            ]
        ),
        answer
    )
ft.app(target=main)

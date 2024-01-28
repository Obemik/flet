import flet as ft

def main(page: ft.Page):
    page.add(

        ft.Text(
            "Michael Perepechai",
            size=50,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN_700,
            weight=ft.FontWeight.BOLD,
            italic=True,
        ),
    )

    c1 = ft.Container(
        ft.Text("Student", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.BLUE,
    )
    c2 = ft.Container(
        ft.Text("ITSTEP", size=50),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.YELLOW,
    )
    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Switch", on_click=animate),
    )
    page.add(
        ft.Row(
            [
                ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK),
                ft.Icon(name=ft.icons.EMOJI_PEOPLE_OUTLINED, color=ft.colors.BLUE),
            ]
        )
    )

ft.app(target=main)
class BasePage:
    base_url = "https://example.com"
    path = "/"

    def open(self):
        return f"Открываю {self.base_url}{self.path}"

page = BasePage()
print(page.open())

class LoginPage(BasePage):
    path = "/login"
login = LoginPage()
print(login.open())

class ProfilePage(BasePage):
    path = "/profile"

    def open(self):
        result = super().open()
        return f"нужна авторизация {result}"

pages = [LoginPage(), ProfilePage()]
for p in pages:
    print(p.open())


























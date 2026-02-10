# presenters/login_presenter.py
from services.auth_service import AuthService
from ui.login_view import LoginView

class LoginPresenter:
    def __init__(self, view: LoginView, auth: AuthService, on_success):
        self.view = view
        self.auth = auth
        self.on_success = on_success
        self.view.loginRequested.connect(self.handle_login)

    def handle_login(self, username: str, password: str):
        result = self.auth.login(username, password)
        if result.ok:
            #self.view.show_info(result.message)
            self.on_success(username)
        else:
            self.view.show_error(result.message)
            self.view.clear_password()

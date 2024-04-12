class ServerUserDatabase:
    def __init__(self, name: str = None, is_run_keyboard: bool = None, is_run_mouse: bool = None):
        self.user = {"name": name, 'is_run_keyboard': is_run_keyboard, 'is_run_mouse': is_run_mouse}

    def get_user(self):
        return self.user

    def update_user(self, name: str = None, is_run_keyboard: bool = None, is_run_mouse: bool = None):
        if is_run_keyboard:
            self.user['is_run_keyboard'] = is_run_keyboard
        if is_run_mouse:
            self.user['is_run_mouse'] = is_run_mouse
        if name:
            self.user['name'] = name

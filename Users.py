from abc import ABC, abstractmethod


class User(ABC):
    """
    Abstract class for users.
    name: user name.
    password: password fot the user
    """

    @abstractmethod
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    def __str__(self):
        return f"name: {self.name} password: {self.password} "

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def set_password(self, password: str):
        self.password = password


class Admin(User):
    """
    Class for admin.
    """
    def __init__(self, name: str, password: str):
        super().__init__(name, password)


class Guest(User):
    """
    Class for guest (no admin users).
    """
    def __init__(self, name :str, password: str):
        super().__init__(name, password)


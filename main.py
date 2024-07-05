class NotValidUsernameError(Exception):
    pass

class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            value = value + "___"
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_long_enough = len(value) >= 8
        is_upper_char = len([char for char in value if char.isupper()]) > 0
        is_digit = len([char for char in value if char.isdigit()]) > 0

        if not is_long_enough or not is_upper_char or not is_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


password = input()
while True:
    try:
        profile_with_invalid_password = Profile('My', password)
        break
    except ValueError as er:
        print(str(er))
        input()


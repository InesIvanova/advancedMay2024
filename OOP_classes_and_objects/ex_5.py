class Smartphone:
    """This is smartphone class"""
    def __init__(self, app_memory: float) -> None:
        """
        this is the initializer
        """
        self.memory = app_memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, memory: float) -> str:
        """
        If phone is on and there is enough memory left,
        we will install, if the phone is not in we should display
         message to turn it on, if there is no memory
         display appropriate message
        """
        if self.memory >= memory and self.is_on:
            self.apps.append(app)
            self.memory -= memory
            return f"Installing {app}"
        elif  self.memory >= memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def __str__(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


s = Smartphone(100)

# print(s.__dict__)
print(Smartphone.power.__doc__)

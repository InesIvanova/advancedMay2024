class Device:
    def description(self):
        return "device"


class Phone(Device):
    def description(self):
        return Device.description(self) + " Specifically, a phone."


class Camera(Device):
    def description(self):
        return Device.description(self) + " Specifically, a camera."


class Smartphone(Phone, Camera):
    def description(self):
        res1 = Phone.description(self)
        res2 = Camera.description(self)
        return res1 + res2 + " And it can be used as both a phone and a camera."

smartphone = Smartphone()
print(smartphone.description())

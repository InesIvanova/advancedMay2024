class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


class MyCustomRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 8


class CleaningRobot(Robot):
    pass


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


def get_sensors(robot):
    print(robot.sensors_amount())



basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
my_custom = MyCustomRobot("Hi")
cleaning = CleaningRobot("Cleaning")

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
number_of_robot_sensors(my_custom)
number_of_robot_sensors(cleaning)



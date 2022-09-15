class Robot:
    def __init__(self, name):
        self.name = name

    def return_name(self):
        return self.name

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

    def shoot(self):
        return 'boom!'


def number_of_robot_sensors(robot):
    print(f'{robot.sensors_amount()} - {robot.return_name()}')


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)

print(griffin.shoot())

from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("one1", "Education", 50, 10)

    def test_init(self):
        r = Robot("one1", "Education", 50, 10)
        self.assertEqual(r.robot_id, "one1")
        self.assertEqual(r.category, "Education")
        self.assertEqual(r.available_capacity, 50)
        self.assertEqual(r.price, 10)
        self.assertEqual(r.hardware_upgrades, [])
        self.assertEqual(r.software_updates, [])

    def test_init_robot_invalid_category_raises(self):
        with self.assertRaises(ValueError) as ex:
            r = Robot("one1", "a", 50, 10)
        self.assertEqual(str(ex.exception), "Category should be one of "
                                            "'['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_init_robot_invalid_price_raises(self):
        with self.assertRaises(ValueError) as ex:
            r = Robot("one1", "Education", 50, -2)
        self.assertEqual(str(ex.exception),"Price cannot be negative!")

    def test_upgrade_hardware_is_already_in_the_list(self):
        self.robot.hardware_upgrades.append("Part A")

        self.assertEqual(self.robot.hardware_upgrades, ["Part A"])
        self.assertEqual(self.robot.price, 10)

        result = self.robot.upgrade("Part A", 10)

        self.assertEqual(self.robot.hardware_upgrades, ["Part A"])
        self.assertEqual(self.robot.price, 10)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not upgraded.")

    def test_upgrade_robot(self):
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.price, 10)

        result = self.robot.upgrade("Part 1", 10)

        self.assertEqual(self.robot.hardware_upgrades, ["Part 1"])
        self.assertEqual(self.robot.price, 25)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was upgraded with Part 1.')

    def test_update_no_updates_yet_does_update(self):
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 50)

        result = self.robot.update(15, 200)

        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    def test_update_version_is_less_than_existing_updates_does_not_update(self):
        self.robot.software_updates = [10, 20, 5]

        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 50)

        result = self.robot.update(15, 200)

        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    def test_update_available_capacity_is_not_enough_does_not_update(self):
        self.robot.software_updates = [10, 20, 5]

        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertLess(self.robot.available_capacity, 200)

        result = self.robot.update(25, 200)
        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    def test_update(self):
        self.robot.software_updates = [10, 20, 5]

        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 50)

        result = self.robot.update(25, 30)
        self.assertEqual(self.robot.software_updates, [10, 20, 5, 25])
        self.assertEqual(self.robot.available_capacity, 20)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was updated to version 25.')

    def test_compare(self):
        robot_less = Robot("one1", "Education", 50, 1)
        robot_equal = Robot("one1", "Education", 50, 10)
        robot_greater = Robot("one1", "Education", 50, 20)

        result = self.robot.__gt__(robot_less)
        self.assertEqual(result, f'Robot with ID '
                                 f'{self.robot.robot_id} '
                                 f'is more expensive than '
                                 f'Robot with ID '
                                 f'{robot_less.robot_id}.')

        result = self.robot.__gt__(robot_equal)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} '
                                 f'costs equal to Robot with ID {robot_equal.robot_id}.')

        result = self.robot.__gt__(robot_greater)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} '
                                 f'is cheaper than Robot with ID {robot_greater.robot_id}.')


if __name__ == "__main__":
    main()

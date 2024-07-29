from OOP_testing.ex_4 import Car


from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("BMW", "4", 8, 50)

    def test_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("4", self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_set_make_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_set_model_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_set_fuel_consumption_less_then_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        # test less than zero
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_car_set_fuel_capacity_less_then_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        # test less than zero
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_set_fuel_amount_less_then_or_equal_to_zero_raises(self):
        # test less than zero
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_less_than_or_equal_to_zero_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

        # Zero
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_less_than_capacity_is_added(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_greater_than_capacity_sets_to_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)

        fuel_amount = self.car.fuel_capacity + 1
        self.car.refuel(fuel_amount)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive_not_enough_fuel_amount_raises(self):
        self.assertEqual(0, self.car.fuel_amount)

        needed = (10 / 100) * self.car.fuel_consumption
        needed += 1

        with self.assertRaises(Exception) as ex:
            self.car.drive(needed)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        self.assertEqual(0, self.car.fuel_amount)

    def test_drive(self):
        # We will spend 0.8
        distance = 10

        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)
        self.car.drive(distance)


        expected = 49.2
        self.assertEqual(expected, self.car.fuel_amount)

if __name__ == "__main__":
    main()
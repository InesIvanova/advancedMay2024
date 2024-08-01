from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        # TODO
        reduce = mileage / self.MAX_MILEAGE * 100
        self.battery_level -= reduce
        self.battery_level = round(self.battery_level)
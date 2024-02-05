class Engine():
    def __init__(self, capacity, cylinders):
        self.eng_capacity = capacity
        self.__cylinders = cylinders

    def __show_cylindes(self):
        return self.__cylinders

    def capacity_per_cylinder(self):
        cylinders = self.__show_cylindes()
        return self.eng_capacity/cylinders

    @staticmethod
    def start_engine():
        return "Starting engine"

    @staticmethod
    def stop_engine():
        return "Stopped engine"

class Car(Engine):
    def __init__(self, capacity, cylinders, wheels, doors):
        super().__init__(capacity, cylinders)
        self.wheels = wheels
        self.doors = doors

    def _doors_number(self):
        return self.doors

    @staticmethod
    def open_doors():
        return "Opened the doors"

    @staticmethod
    def close_doors():
        return "Closed the doors"

    def print_all(self):
        return("Engine cap {}, cap per cylinder {}, doors {}, wheels {}".format(self.eng_capacity, self.capacity_per_cylinder(), self.doors, self.wheels) )



class Honda(Car):
    def __init__(self, wheels, doors, capacity, cylinders, max_speed):
        super().__init__(wheels, doors, capacity, cylinders)
        self.max_speed = max_speed

    def set_speed(self, max_speed):
        self.max_speed = max_speed

    def print_all(self):
        return ("Engine cap {}, cap per cylinder {}, doors {}, wheels {}, max speed {}".format(self.eng_capacity,
                                                                                 self.capacity_per_cylinder(),
                                                                                 self.doors, self.wheels, self.max_speed))

    @classmethod
    def speed_unknown(cls, wheels, doors, capacity, cylinders, max_speed):
        return cls(wheels, doors, capacity, cylinders, 0)


engine = Engine(1200, 4)
print(engine.start_engine())
print(engine.stop_engine())
print(engine.capacity_per_cylinder())
print()

car = Car(1400, 4, 4, 5)
print(car.open_doors())
print(car.close_doors())
print(car.start_engine())
print(car.print_all())
print()

honda = Honda(2000, 6, 4, 2, 200)
honda.set_speed(220)
print(honda.print_all())
honda2 = Honda.speed_unknown(2000, 6, 4, 2, 'Unknown')
print(honda2._doors_number())
print(honda2.print_all())

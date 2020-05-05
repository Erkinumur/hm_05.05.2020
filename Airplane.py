class Airplane:
    def __init__(self, make, model, year, max_speed, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False

    def take_off(self):
        print(f'Самолет {self.make} {self.model} взлетел.')
        self.is_flying = True
    
    def land(self):
        print(f'Самолет {self.make} {self.model} приземлился.')
        self.is_flying = False

    def fly(self, distance):
        print(f'Самолет {self.make} {self.model} пролетает {distance} км.')
        self.odometer += distance


su_27 = Airplane('Cу', "27", 1990, 2500, 100000)

su_27.take_off()
print(f'"is_flying" = {su_27.is_flying}')

su_27.fly(25000)
print(f'odometer = {su_27.odometer}')

su_27.land()
print(f'"is_flying" = {su_27.is_flying}')

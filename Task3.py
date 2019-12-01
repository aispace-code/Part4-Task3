# В самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
#то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

class Car:

    def __init__(self, make, model, year, odometer, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __substract_fuel(self, used_fuel):
        self.fuel -= used_fuel
        print('Lets drive! You still have this much fuel: ', str(self.fuel))

    def add_distance(self, notenough):
        self.odometer = notenough

    def drive(self, distance):
        if distance <= self.fuel * 10:
            miles = distance
            self.add_distance(miles)
            fuel_used_fuel = miles/10
            self.__substract_fuel(fuel_used_fuel)
        else:
            print('You dont have enough fuel!')

cars = Car('audi', 'quattro', 2016, 0, 0)

cars.drive(100)

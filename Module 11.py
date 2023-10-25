#Exercise 11.1:
class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name,author,pageCount):
        self.author = author
        self.pageCount = pageCount
        super().__init__(name)

    def print_information(self):
        print(f"The name of the book is: {self.name}. The author of the book is {self.author} and it has {self.pageCount} pages.")


class Magazine(Publication):
    def __init__(self,name,chiefEditor):
        self.chiefEditor = chiefEditor
        super().__init__(name)

    def print_information(self):
        print(f"The name of the magazine is: {self.name}. The chief Editor of the magazine is: {self.chiefEditor}.")

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No.6","Rosa Liksom",192)
magazine1.print_information()
book1.print_information()

#Exercise 11.2:
class Car:
    def __init__(self,registrationNumber, maximumSpeed,currentSpeed = 0,travelledDistance = 0):
        self.registrationNumber = registrationNumber
        self.maximunSpeed = maximumSpeed
        self.currentSpeed = currentSpeed
        self.travelledDistance = travelledDistance

    def acceleration(self,changeOfSpeed):
        if(self.currentSpeed + changeOfSpeed < 0):
            self.currentSpeed = 0
        elif(self.currentSpeed + changeOfSpeed < self.maximunSpeed):
            self.currentSpeed= self.currentSpeed + changeOfSpeed
        else:
            self.currentSpeed = self.maximunSpeed

    def drive(self,numberOfHours):
        if(numberOfHours >= 0):
            self.travelledDistance = numberOfHours * self.currentSpeed+self.travelledDistance

class ElectricCar(Car):
    def __init__(self,registrationNumber, maximumSpeed,batteryCapacity):
        self.batteryCapacity = batteryCapacity
        super().__init__(registrationNumber,maximumSpeed)

class GasolineCar(Car):
    def __init__(self,registrationNumber, maximumSpeed,tankVolume):
        self.tankVolume = tankVolume
        super().__init__(registrationNumber, maximumSpeed)

electricCar1 = ElectricCar("ABC-15",180,52.5)
gasolineCar1 = GasolineCar("ACD-123",165,32.3)

electricCar1.acceleration(127)
gasolineCar1.acceleration(135)
electricCar1.drive(3)
gasolineCar1.drive(3)
print(f"The electric car travelled {electricCar1.travelledDistance} km.")
print(f"The gasoline car travelled {gasolineCar1.travelledDistance} km.")

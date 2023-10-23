#Exercise 9.1, 9.2, 9.3, 9.4:
import random
class Car:
    raceHour = 0
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

carExample = Car("ABC-123",142)
print(f"The registration number of the car is {carExample.registrationNumber:s} and the maximum speed of the car is {carExample.maximunSpeed:d} km/h.")

carExample.acceleration(30)
carExample.acceleration(70)
carExample.acceleration(50)
print(f"The current speed of the car is {carExample.currentSpeed:d} km/h.")
carExample.acceleration(-200)
print(f"The current speed of the car is {carExample.currentSpeed:d} km/h.\n")

carList = []
for i in range(10):
    carList.append(Car(f"ABC-{i+1}",random.randint(100,200)))

raceEnd = False
while not raceEnd:
    Car.raceHour += 1
    for car in carList:
        car.acceleration(random.randint(-10,15))
        car.drive(1)
        if(car.travelledDistance>= 10000):
            raceEnd = True

print("{:<8} {:<20} {:<15} {:<15} {:<15}".format("Number","Registration Number","Maximum Speed","Current Speed", "Travelled Distance"))
for i, car in enumerate(carList):
    print("{:<8} {:<20} {:<15} {:<15} {:<15}".format( i+1, car.registrationNumber,car.maximunSpeed,car.currentSpeed,car.travelledDistance))

#Exercise 10.1, 10.2, 10.3:
class Elevator:
    def __init__(self,bottomFloor,topFloor):
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor
        self.currentFloor = bottomFloor

    def floor_up(self):
        self.currentFloor += 1
        print(f"The elevator is at floor {self.currentFloor}.")
        return

    def floor_down(self):
        self.currentFloor -= 1
        print(f"The elevator is at floor {self.currentFloor}.")
        return

    def go_to_floor(self,floor):
        if(self.bottomFloor <= floor < self.currentFloor):
            while(floor < self.currentFloor):
                self.floor_down()
        elif(self.currentFloor < floor <= self.topFloor):
            while(self.currentFloor < floor):
                self.floor_up()
        elif(self.currentFloor == floor):
            print(f"You are already at floor {floor}.")
        else:
            print("Invalid.")

h = Elevator(-3,25)
h.go_to_floor(4)
h.go_to_floor(-3)
print()

class Building:
    def __init__(self,bottomFloor,topFloor,elevators):
        self.elevators = {}
        i= 1
        while(i <= elevators):
            self.elevators[i]= Elevator(bottomFloor,topFloor)
            i += 1
    def run_elevator(self,elevatorNumber,destinationFloor):
        if(0 < elevatorNumber <= len(self.elevators)):
            print(f"You are running elevator {elevatorNumber}.")
            self.elevators[elevatorNumber].go_to_floor(destinationFloor)
            print()
        else:
            print("Invalid.")

    def fire_alarm(self):
        for i in self.elevators:
            print(f"You are running elevator {i}.")
            self.elevators[i].go_to_floor(self.elevators[i].bottomFloor)
            print()

buildingA = Building(-2,10,5)
buildingA.run_elevator(3,4)
print()
buildingA.fire_alarm()

#Exercise 10.4:

import random
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

class Race:
    def __init__(self,name,kilometers,carList):
        self.name = name
        self.kilometers = kilometers
        self.carList = carList

    def hour_passes(self):
        for car in self.carList:
            car.acceleration(random.randint(-10,15))
            car.drive(1)

    def print_status(self):
        print("{:<8} {:<20} {:<15} {:<15} {:<15}".format("Number", "Registration Number", "Maximum Speed",
                                                         "Current Speed", "Travelled Distance"))
        for i, car in enumerate(carList):
            print("{:<8} {:<20} {:<15} {:<15} {:<15}".format(i + 1, car.registrationNumber, car.maximunSpeed,
                                                             car.currentSpeed, car.travelledDistance))
        print()

    def race_finished(self):
        raceEnd = False
        for car in carList:
            if (car.travelledDistance >= 10000):
                raceEnd = True
        return raceEnd

carList = []
for i in range(10):
    carList.append(Car(f"ABC-{i+1}",random.randint(100,200)))

grandDemolitionDerby = Race("Grand Demolition Derby",8000,carList)

print(f"Welcome to the {grandDemolitionDerby.kilometers} km {grandDemolitionDerby.name} race!")
print("Here is the information of the 10 racing cars:\n")
grandDemolitionDerby.print_status()

raceHour = 0
while not grandDemolitionDerby.race_finished():
    raceHour += 1
    grandDemolitionDerby.hour_passes()
    if(raceHour % 10 == 0):
        grandDemolitionDerby.print_status()
else:
    print("The race ended and here are the results:")
    grandDemolitionDerby.print_status()

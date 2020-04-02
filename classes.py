class Car: 

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        if (weight > 300 and weight < 10000):
            self.__weight = weight
        else :
            print("ERROR: Вес машины не модет быть больше 10000 и меньше 300")

    def ride(self):
        print("I am riding")
        print("color : " + self.__color)
        print("My weight : " + str(self.__weight))
        return self.__color

    def __init__(self, color, weight):
        self.__color = color
        self.__weight = weight

class Truck(Car):
    
    def info(self):
        print("I am truck")

    def ride(self):
        print("TRUCK RIDING")
        print("MY carring : " + str(self.carrying))

    def __init__(self, carrying):
        self.carrying = carrying

new_car = Car("Blue", 150)
new_car.ride()
new_car.weight = 1550
new_car.ride()

new_truck = Truck(20000)

new_truck.info()
new_truck.ride()
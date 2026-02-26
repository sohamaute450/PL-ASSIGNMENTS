#Method Overriding
class vehicle:
    def move(self):
        print("Vehicle is Moving")

class car(vehicle):
    def move(self):
        print("Driving on the Road")

class cycle(vehicle):
    def move(self):
        print("Pedalling on the Road")

c=car()
c1=cycle()

c.move()
c1.move()

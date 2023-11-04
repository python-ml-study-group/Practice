class Nanocar:
    def __init__(self):
        self.engine = "800cc"
        self.seats = 4
        self.color = "red"
        self.certification = "BIS5"
    def print (self):
        print (f"Nano car, which has Seats: {self.seats}, color: {self.color}, engine: {self.engine}, certification: {self.certification}") 

class Nanocar_v2(Nanocar):
    def __init__(self):
        super().__init__()
        self.engine = "1000cc"
        self.seats = 5
    def drivebackwards(self):
        print ("Driving backwards") 
    def print (self):
        print (f"Nano car v2, which has Seats: {self.seats}, color: {self.color}, engine: {self.engine}, certification: {self.certification}, it can run backwards") 


car = Nanocar_v2()
car.print()

carold = Nanocar()
carold.print()

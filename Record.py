class CarRecord():
    def __init__(self):
        self.VehicleID=""
        self.Registration=""
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00
ThisCar=CarRecord()
ThisCar.EngineSize=2500
NewCar=CarRecord()
Car=[NewCar for i in range(100)]
Car[1].EngineSize=2500

class Automobile: # Parent class
    color = "Blue"
    def VehicleType(self):
        return 'Sedan'
    
    
class Car(Automobile): # Child class inheriting from Automobile class
    color = "Red" #Variable override
    def VehicleType(self): # Method override
        return 'Saloon'
    
toyota = Car() # Child class object
print(toyota.color) #variable override

tesla = Car() # Child class object
print(tesla.VehicleType()) #Method override

car11 = Automobile()
print(car11.VehicleType())

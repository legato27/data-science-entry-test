class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")
        return self.year, self.make, self.model
    

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

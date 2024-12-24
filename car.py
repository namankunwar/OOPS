class BlueCar:

    def __init__(self, brand:str, power_rating:str, overall_rating:float)->None:
        self.brand = brand
        self.power_rating = power_rating
        self.overall_rating = overall_rating
        self.turned_on:bool = False
    

    def turn_on(self):
        if self.turned_on:
            print(f"the {self.brand} car is arleady on !!")
        else:
            self.turned_on = True
            print(f"The {self.brand} is now on !!")
    
    def turn_off(self):
        if self.turned_on == False:
            print(f" the {self.brand} is arleady off !!")
        else:
            self.turned_on = False
            print (f" THE {self.brand} is now off !!")

    def run(self, second:int):
        if self.turned_on:
            print(f"the {self.brand} is running for {second} !!")
        else:
            print(f"It appears the {self.brand} has been stopped by some mystical force !")
    

    #dunder method
    def __add__(self, other):
        return (f"{self.brand} + {other.brand}")

    def __mul__(self, other):
        return (f"{self.brand} * {other.brand}")
    
    #important dunder method
    #this is used as user friendly
    def __str__(self) ->str:
        return (f"{self.brand} is a rating of {self.power_rating} !!")
    
    #this is for developer to see whats going on 
    def __repr__(self):
        return (f' BlueCar(brand= "{self.brand}" , power_rating="{self.power_rating}")')
       
import time


class Car:
    # define the init method => to start something
    def __init__(self,model,color,fuel_capacity):
        self.model = model
        self.color = color
        self.fuel_capacity = fuel_capacity
        
    def intro(self):
        self.greet = f'''
        I am a {self.color} {self.model}
        The best among the best.....
        With a fuel capacity of {self.fuel_capacity}
        '''
        for i in self.greet:
            print(i, end='', flush=True)
            time.sleep(0.05)
            
    def carColor(self):
        print('My color is', self.color)
        
    # method that can modify our attribute
    def fuel_used(self, fuelAmount = 0):
        self.fuel_capacity -= fuelAmount


newCar = Car('Tesla', 'Black Matte', 55000)

newCar.intro()

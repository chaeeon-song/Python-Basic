class Car:

    COLOR = {1: "빨강", 2: "파랑", 3: "노랑"}

    def __init__(self, speed=0, gear=1, color_code=1):
        self.speed = max(0, speed) 
        self.gear = (1, 6)
        print(f"({self.speed}, {self.gear}, {self.color})")


    def speed(self):
        return self.speed

    def gear(self):
        return self.gear
    
    def carcolor(self):
        return self.carcolor

    def changecolor(self, carcolor):
        if carcolor in self.COLOR:
            self.carcolor = carcolor
            print(f"({self.speed}, {self.gear}, {self.color})")
        else :
            print('Error!')
            
    def changeGear(self, gear):
        if 1 <= gear <= 6:
            self.gear = gear
            print(f"({self.speed}, {self.gear}, {self.color})")
        else:
            print("Error!")
            
    def speedUp(self, increase_speed):
        if increase_speed > 0:
            self.speed += increase_speed
            print(f"speedUp!\n({self.speed}, {self.gear}, {self.color})")
        else:
            print("Error!") 
            
    def speedDown(self, decrease_speed):
        self.speed = max(0, self.speed - decrease_speed)
        print(f"speedDown!\n({self.speed}, {self.gear}, {self.color})")

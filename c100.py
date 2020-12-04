class Car(object):

     def __init__(self,model,color,company,speed_limit):
       self.color=color
       self.model=model
       self.company=company
       self.speed_limit=speed_limit

     def start(self):
        print("starting")

     def accelerate(self):
        print("accelerating..."
        "accelerate")

     def change_gear(self,gear_type):
         self.gear_type=gear_type
         num=3*self.gear_type
         print(num)
        

maruthi=Car("a7","grey","suzuki","80")
print(maruthi.accelerate())
print(maruthi.change_gear(3))
print(maruthi.color)
        

    
    
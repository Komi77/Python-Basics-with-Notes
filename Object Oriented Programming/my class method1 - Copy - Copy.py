class Employee():
    Companyname = "Apple"
    Car = "Vigo"

    def show(self, name):
        print(f"The employee {name} is in the company {self.Companyname} and has a car {self.Car} ")

    def changeCompanyname (self, newname):
        self.Companyname = newname
    #this func is to change the name of the company, but it will not change the class variable which is the overall company name (for every employee), instead it will only change the company name for a specific instance which is for an employee object like emp1.


    @classmethod
    def changecarname (self, newcar):
        self.Car = newcar
    
    #here we put the classmethod decorator what it does is that now when we put it, and then change the name of the car, it will not only change the name of the car for that specific instance or employee object like emp1 but it will change the car name overall.


emp1 = Employee()
emp1.show("Komi")
print(emp1.Companyname)
emp1.changeCompanyname("Meta")
emp1.show("Komi")  
print(Employee.Companyname)
#here we see that when we change the company name for the func info it changes from apple to meta, but now again when we print the company name it will be apple, because we did not change the overall class variable which is the company name.

print(emp1.Car)
emp1.changecarname("Mclearn P1")
emp1.show("Komi")  
print(Employee.Car)
#here we will see that when we change the name of the car, it changes in the func info but it also changes the class variable which is the overall car name from vigo to Mclearn P1. 

    
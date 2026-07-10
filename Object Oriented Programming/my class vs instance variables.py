class Employee:
    company_name = "Google"
    noofemployees = 0

    def __init__(self, name):
        self.name = name 
        self.raise_salary = 0.4
        Employee.noofemployees =+ 1

    def Show(self):
        print(f"The employee whose name is {self.name} in the company {self.company_name} where {self.noofemployees} people work should get a raise of {self.raise_salary}")


emp1 = Employee("Shakur")
emp1.raise_salary = 2.6
print(emp1.raise_salary)
emp1.company_name = "Apple"
print(emp1.company_name)
emp1.Show()    
    
emp1 = Employee("Arham")
emp1.raise_salary = 0.5
print(emp1.raise_salary)
emp1.company_name = "Premier Group"
print(emp1.company_name)
emp1.Show()  


print(Employee.company_name)

Employee.company_name = "Microsoft"
print(Employee.company_name)




#Now look at all this code and understand what is the diff b/w class and instance variables, basically to put it simply instance variables are inside a method or a func but the class variables are outside a func or method. What it symbolizes is that the instance variables that are inside a func are specific to a certain object like inside the func innit and for the object emp1 raise is 2.6 while for emp2 is 0.5, so we can change the pay raise because it is not a general thing rather it is specific to the specific employee although we have set the value of raise to 0.4 by default, so if we dont change it for our different employees (objects) it will be the same for everyone and i get it that i said that instance variables are specific for each object or instance or employee in this case but then why is the pay raise of everyone same, well we have to set a default value, right? so thats why we have set it 0.4 although we all know that its diff for every employee. So that is an instance variable but a class variable is something that is general and applicable to all like the company name. which in our case is google but you can see that we have still changed it for some employees like emp1 and emp2, so we can also change the values of class variable for some instances or objects but in general it is the same for everyone. You can also see that we have also changed the whole company name which means we are changing the value of the class variable not for a specific object (like emp1). So, for everyone except employees like emp1 and emp2 whose company names we have especially changed, everyones company name will be changed to the new name. Same goes with a class variable called no of employees which is 0 (zero) at the start but then we put that class variable inside an instance variable, so now whenever new instances (employees) develop, it increases.

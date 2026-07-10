#MAKING A GETTER:

class Lama:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"The value is {self._value}")

    
#Here we make a simple class with funcs, first func makes an argument which is value and we can set the value in the paranthesis. Then we wrote the second func, where we basically just print the value with some sentence.

    @property
    def ten_value(self):
        return 10 * self._value
    
#This right here is a getter, what it does is that it can modify the value that we give, what i mean is that by using getters we can perform operations like multiplication, subtraction etc. on the value that we give in the class, we can't do it directly without using the decorator known as @property. So by using getters we can modify the value, however you have to note that it can't directly change the whole value what i mean by that is that if we give the value 4, getters can't change it to 5 or 8, like it cant do it directly.


    #MAKING A SETTER:

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value


#What we do here is that we make a setter, first understand what a setter does, it basically changes the whole value initially, what i mean is that inside the class we store the value in self._value, and we set this value below inside the paranthesis, which rn is 10, but lets say i wanna change it, what I'll do is that i can use setters and change it to 67. So what i do is that first i write this decorator @ten_value.setter, ten_value is a getter that we made earlier and rn we are making a decorator with its name to make a setter, then we say that self._value is equal to new_value, and when below we write a.ten_value = 67, it actually changes the value to 67, now if we tried to do it without the setter, it wouldn't had worked and the value would not have been changed.



a = Lama(10)
a.ten_value = 67
print(a._value)
print(a.ten_value)
a.show()

#See here that we changed the a.ten_value to 67, then printed a._value and a.ten_value, which gives 67 and 670 result respectively.


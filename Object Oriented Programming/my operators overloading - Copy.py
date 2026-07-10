class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        return  Vector(self.i + x.i, self.j + x.j, self.k + x.k )
    
que1 = Vector(4,5,6)
print(que1)

que2 = Vector(2,7,3)
print(que2)

que3 = Vector(1,5,9)
print(que3)

que4 = Vector(3,8,7)
print(que4)

print(que1 + que2 + que3 + que4)

#If we make many objects from a class and now we want to add them or subtract or multiply them we first make a func inside the class as either __add__ or __sub__ or __mul__, by writing self and x in the func we mean that add this func to whomever else has this function (something like that lol) but yeah thats how we fking do it.


class Hector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __mul__(self, x):
        return  Hector(self.i * x.i, self.j * x.j, self.k * x.k )
    

paad1 = Hector(4,3,2)
print(paad1)
paad2 = Hector(7,6,1)
print(paad2)
paad3 = Hector(1,9,2)
print(paad3)
    
print(paad1 * paad2 * paad3)

#Here we easily multiplied multiplied objects.
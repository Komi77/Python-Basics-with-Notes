class Square:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def area (self):
        return self.x * self.y
    
sq1 = Square(5,4)
print(sq1.area())


class Circle(Square):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
    def area(self):
        return 3.14 * super().area()
    

cir1 = Circle(5)
print(cir1.area())


#what we did here was that we first created a circle class which is a subclass of square, the formula for area of square is x*y, but that for a circle is 3.14 * radius^2. So, we did a clever trick to reuse the parent class square, and we overwrote the code of this class, what we did is that we did    super().__init__(radius, radius) which means the two arguments of the class square (parent class) which were x and y, are now both equal to the value of the radius, so when we find out the area of a circle and call for the super().area() which is basically us calling for the area func used in the parent class square, and it is multiplied by 3.14, and we have changed both the arguments from x,y to radius, radius, so what will happen is that 3.14 will be multiplied by square of radius which will we given in the argument and here it is 5. Thats how we overwrote the parent class, changed its arguments for our own sake and found out the area of a circle. Yayyyyyyyyyyyyyyy!  
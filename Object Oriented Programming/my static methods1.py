class Komi:
    def __init__(self, num):
        self.num = num

    def pencho(self, n):
        self.sanam = self.num + n

    def halo(self, a, b):
        self.a = a
        self.b = b
        return a + b

    @staticmethod
    def pele(a,b):
        return a + b
    
#Now concentrate on two funcs one is halo and one is pele, what static method really is, is that it eliminates the need to write self inside of the paranthesis, what i mean by that is that look at the func halo it contains two arguments a and b but first we have to sort of check or verify those two arguments by writing them like self.a or self.b, then we can return the func a + b. What staticmethod does is that it eliminates the need to do that we can simply first write the decorator static method then we simply return a + b.

re = Komi(4)
print(re.num)
re.pencho(5)
print(re.sanam)
print(re.halo(3,2))
print(re.pele(3,2))

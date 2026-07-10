def dumbass(fx):
    def goo(a,b):
        print("Whats the problemo now dummy")
        result = fx(a,b)
        print("Hope you got it right nigga")
        return result
    return goo


@dumbass 
def kut(a, b):
    print (a + b)


kut (5, 10)



def guide(fx):
    def woh(a):
        print("The candidate is enrolled in the exams")
        result = fx(a)
        print("This is a confidential info")
        return result
    return woh


@guide
def guy(a):
    print(f"The name of the candidate is {a}")


guy("Kumail")
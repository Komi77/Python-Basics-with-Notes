#WHAT ARE CLASSES AND OBJECTS?

#for e.g. lets say that there are 10 passengers on a train, now we have to store the information about all these 10 passengers, we can do this by either wasting alot of our time and writing for e.g., passenger 1 --> name : Kumail, ticket number: 425446754 blah blah blah, now by writing like this the main problemo is that we have to write these things which many call pre-printed details like name, ticket number, ticket price, etc. etc. , so what we can do is we can instead create a class, now the info that these classes usually store are these as i called pre printed details, by this we dont have to write them again and again, instead we can just write our name, ticket number, price etc. and we dont have to write the questions again and again, think of classes as a pre printed paper, you just have to write the ans, and when you fill it with ans it becomes an object, now one class can make different object, like my paper will be for e.g. different from ali's because his ans which you can think of as input is diff, so as you see one class (which is the empty test paper with pre printed questions) can make different objects (my paper and ali's or zain's paper).

#This is how to make a class and its objects;

#CREATING A CLASS:
class Person:
    name = "Kumail"
    occupation = "Astronomer"
    networth = "$54"
    def lol(self):
        return print(f"{self.name} is a {self.occupation}")



#CREATING OBJECT#1:
a = Person()
a.name = "Turab"
a.occupation = "Darzi"
print(a.name)
print(a.occupation)
print(a.networth)
a.lol()


#Here what we did is that first we created a class, and it has all the pre printed details about a person along with its input, what i mean is that this class has all the headings as name, occupation, networth, so that you dont have to write them again, and just as default we filled those "pre-printed headings" with the info of a geezer named Kumail. But then what we did below is that we enclosed that class in a variable, then we started to change the name, occupation, which are basically the headings so what we did here is that we made a sample and now we are chaning that sample to our name, means that the sample is about a person, and we filled it with some default guy, now we can change it and fill it with someone elses info. Pretty cool, right? and notice how the networth doesn't change and the default one is printed upon printing it, it is because we didn't change it for this person.





b = Person()
b.name = "Warren"
b.occupation = "Shoe Salesman"
b.networth = "$1,000,000"
print(b.name)
print(b.occupation)
print(b.networth)
b.lol()

#As you can see we used the same sample which we call class in coding terms and used it to enter the info of some other guy, and we can use this over and over, and we dont have to write those headings over and over, its a life saver.



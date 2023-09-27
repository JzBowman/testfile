import random

class Car:
    def __init__(self, model, year, brand, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.price = price
        
    def getModel(self):
        return self.model
    def setModerl(self, newMod):
        self.model = newMod
    def getYear(self):
        return self.year
    def setYear(self, newYear):
        self.year = newYear
    def getBrand(self):
        return self.brand
    def setBrand(self, newBrand):
        self.brand = newBrand
    def getPrice(self):
        return self.price
    def setPrice(self, newPrice):
        self.price = newPrice

class Mustang(Car):
    def __init__(self, model, year, brand, price, color, mileage):
        super().__init__(model, year, brand, price)
        self.color = color
        self.mileage = mileage
    
    def getColor(self):
        return self.color
    def setColor(self, newColor):
        self.color = newColor
    def getMileage(self):
        return self.mileage
    def setMileage(self, newMil):
        self.mileage = newMil
class Porche(Car):
    def __init__(self, model, year, brand, price, manufacturer):
        super().__init__(model, year, brand, price)
        self.manufacturer = manufacturer
        
    def getMan(self):
        return self.manufacturer
    def setMan(self, newMan):
        self.manufacturer = newMan
        
        
c1 = Mustang("Mustag Convertible", 2000, "Chevrolet", "$23,260", "Red", "30,000 mi")
print("\t ===============")
print("\t ==Car Auction==")
print("\t ===============")
c2 = Porche("Porche 911", 1985, "Porche", "$32,000", "Porche AG")

#User questionare
userAge = int(input("Enter you age: \n"))
if(userAge >= 18):
    print("Age looks good, continue.")
else:
    print("\t !!!!!!WARNING: TOO YOUNG!!!!!!")
    print("\t either way, you'll be able to check the auction\n")
    
#Car 1: Mustang Convertible
print("\t --------CAR 1---------")
print("\t Model:")
print("\t", c1.getModel())
print("\t Price: ")
print("\t", c1.getPrice())
print("\t Car Color: ")
print("\t", c1.getColor())
print("\t Car Mileage: ")
print("\t", c1.getMileage())

print("\t--------CAR 2---------")

#Car 2: Porche 911
print("\t Model:")
print("\t", c2.getModel())
print("\t Price: ")
print("\t", c2.getPrice())
print("\t Manufacturer:")
print("\t", c2.getMan())

print("\t-------BANK ACCOUNT------")
print("\t Here's the money you currently have: ")

print("\t", random.randint(1, 40000))

d={'Money': 400000, "Credit": 1200}
def buyCar():
    d[money]=d[money]-10
    d[credit]=d[credit]+20

print("Type how much money you see in your account here to check for inssuficient funds: ")
userNum = int(input("\nType here: \n"))
accNum = 0
num = 23000

while True:
  if(userNum >= 23000):
    print("\nCongrats, you have enough funding!")
    break
  elif(userNum <= 23000):
    print("Not enought, try again: ")
    print(random.randint(1000, 40000))
    userNum = int(input("Enter you new amount: "))
    if(userNum <= 23000):
        print("Try again: ")
        print(random.randint(1000, 40000))
        userNum = int(input("Enter you new amount: "))
        if(userNum <= 23000):
          print("Not enought, try again: ")
        print(random.randint(1000, 40000))
        userNum = int(input("Enter you new amount: "))
        if(userNum >= 23000):
         print("Continue!")
        else:
            ("You can still continue")
            break

print("\nHere's your auction number if you wish to still join auction: ")
randNum = random.randint(100, 350)
print(randNum)


    
userPur = input("If you have insufficient funds, you can still chose for later, in the meantime, chose car 1 or car 2  \n")
if(userPur == '1'):
    print("\t --------RECIPT--------")
    print("\t Your Ford Mustang will arrivve for auction shortly!\n")
else:
    print("\t --------RECIPT--------")
    print("\t Understood, the Porche 911 will arrive shortly for auction!\n")

  

class Rating:
    def __init__(self, rating, option, star):
        self.rating = rating
        self.option = option
        self.star = star
        
    def getRating(self):
        return self.rating
    def setRating(self, newRat):
        self.rating = newRat
    def getOption(self):
        return self.option
    def setOption(self, newOp):
        self.option = newOp
    def getStar(self):
        return self.star
    def setStar(self, newStar):
        self.star = newStar

userExp = int(input("Did you like the experience? If so, type the score from 1 to 5, 5 being the best \n"))
if(userExp >= 3):
    print("Glad you had some fun, see you next time!")
else:
    print("Hope to make it up to you next time!")
#Cesar Neri
#December 18, 2016

#Exercise 15-1 From Murach's Python programming Book

#Use of Polymorphism and Inheritance

#!/usr/bin/env python3from objects


class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
            self.name = name
            self.price = price
            self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

class Media(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, mFormat=""):
        Product.__init__(self, name, price, discountPercent)
        self.mFormat = mFormat        
    
class Book(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, mFormat="", author="", ):
        Media.__init__(self, name, price, discountPercent, mFormat)
        self.author = author

    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author
                
class Movie(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, mFormat="", year=0):
        Media.__init__(self, name, price, discountPercent, mFormat)
        self.year = year

    def getDescription(self):
        return Product.getDescription(self) + " (" + str(self.year) + ")"

class Album(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, mFormat="", artist=""):
        Media.__init__(self, name, price, discountPercent, mFormat)
        self.artist = artist

    def getDescription(self):
        return Product.getDescription(self) + " by " + self.artist
            

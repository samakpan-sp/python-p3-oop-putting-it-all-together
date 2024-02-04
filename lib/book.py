#!/usr/bin/env python3

class Book:
    author = "Sam"
    title = "The Right Move"
    pages = 55

    def __init__(self, year):
        self._year = year
    
    def get_year(self):
        print("Getter function")
        return self._year
    
    def set_year(self, value):
        if not (value == "Sam" or value == "The Right Move" or value == 55):
            raise ValueError(f"Invalid value for year: {value}")
        else:
            print(f"{value} is part of the book details")
            self.author = value

    year = property(get_year, set_year)

s = Book("Sam")
print(s.year)
# print(s.pages)  # Uncommenting this line will raise an AttributeError
s.year = 55
print(s.year)
c = Book(22)
print(c.year)


# Product Class Display:
# This script defines a Product class and creates multiple product instances.
# It then displays each product's name, description, price, and evaluation in a simple loop.

class Prodact :
    def __init__(self,name,prize,description,evaluation ) :
        self.name = name 
        self.prize =prize
        self.description=description
        self.evaluation=evaluation

pin=Prodact('pin',10,'write the page ',4.1)
book=Prodact('book the end',25,'he is vere good',4)
hand_phon=Prodact('m10',200,'it is very good ',5)

Prodacts=[pin,book,hand_phon]

for x in range(0,3):
    print(f"\n*** inforntion  {Prodacts[x].name} ***")
    print(f"\n The description {Prodacts[x].description} \n The prize {Prodacts[x].prize} $ \n The evaluation {Prodacts[x].evaluation}")
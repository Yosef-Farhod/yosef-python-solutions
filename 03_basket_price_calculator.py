# Simple basket calculator:
# This script asks the user to input the names and prices of items in a shopping basket,
# then optionally shows the list of items and the total price.


price_all=[]
bacat_all=[]

print('    ***welcom to ishop calculator*** ')
namber=int(input('\nHow many itmes are there in basket today?'))
print("\n let's get to couting them....")

for f in range(1,namber+1) :
    bacat=input(f"pleas tell my the name of the itme namber{f} :")
    bacat_all.append(bacat)
    price=int(input(f"what is the price of {bacat}\n$"))
    price_all.append(price)

see=input('would you like to see inter basket items :  ').lower()

if see =='yes' :
    print(bacat_all)
else :
    print('Good bay\n')

see_price=input("would you like to see how much it'll cost  : ").lower()

if see_price=='yes' :
    print('Buy these items will cost :')
    print(sum(price_all))
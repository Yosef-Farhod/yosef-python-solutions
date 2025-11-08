# //تدريب علي استخدام الكلاس 


class Profile :
    def __init__(self,name,email,lanigth):
        self.name = name
        self.email = email
        self.lanigth = lanigth

Ahmed = Profile("yosef","Yosef@gmail.com","Ardic")
Tito = Profile("Tito","Tito@gmail.com","English")# //تدريب علي استخدام الكلاس 


class Profile :
    def __init__(self,name,email,lanigth):
        self.name = name
        self.email = email
        self.lanigth = lanigth

Ahmed = Profile("yosef","Yosef@gmail.com","Ardic")
Tito = Profile("Tito","Tito@gmail.com","English")
print(Ahmed.name)

class Message :
   
   def __init__(self,send,resiver,conut,date):
        self.send = send 
        self.resiver = resiver 
        self.conut = conut 
        self.date = date 

one_massege = Message("Ahmed","Ali","How are you ","2025/7/2/9.19")
two_message =Message("Ali","Ahmed","I am fine and you ","2025/7/2/9.20")
    
print(one_massege.date)
print(two_message.conut)

class Product :
   
   def __init__(self,name,price,description,rating):
        self.name = name 
        self.price = price
        self.description = description
        self.rating = rating

apple = Product("Apple",30,"helthie food",4)      
banna = Product("Banna",20,"This is favrot food to manke ",4.2)

print(apple.price)



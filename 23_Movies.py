class Movies : 
    def __init__(self,title,director,release,grnre):
        self.title = title
        self.directon = director
        self.release = release 
        self.genre = grnre 

    def disblay(self):
        print(f"\nTitle : {self.title}")
        print(f"Director : {self.directon}")
        print(f"Release Year: {self.release}")
        print(f"Genre: {self.genre}\n")

    def ching_director(self,new):
        self.directon = new


movies1 = Movies("Inception","Christopther Nolan",2010,"Sci-Fi")
movies2 = Movies("The Godfather","Francis Ford Coppole",1972,"Crime")
movies3 = Movies("parasit","Bong Joon-ho",2019,"Thriller")

print("______ MOVIES LIST ______")
movies1.disblay()
movies2.disblay()
movies3.disblay()

movies1.ching_director("Shokry Sarhan")
movies2.ching_director("Ahmed Mazhar")
movies3.ching_director("Isamel Yassin")

print("Changing Movie Directors ....\n\n")
movies1.disblay()
movies2.disblay()
movies3.disblay()

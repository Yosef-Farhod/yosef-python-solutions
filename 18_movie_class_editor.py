# Movie Class Editor:
# This script defines a class for storing movie details such as title,
# director, release year, and genre. It includes methods to display movie
# information and to edit the director's name.

class The_moves :
    def __init__(self,titel,direcor,release_yers,Genre) :
        self.titel = titel 
        self.direcor = direcor
        self.release_yers = release_yers
        self.Genre = Genre 

    def print_the_moves (self) :
        print(f"\n\nTitel : {self.titel}") 
        print(f"Direcor : {self.direcor}")
        print(f"Release yers : {self.release_yers}") 
        print(f"Genre : {self.Genre}")

    def Edit(self,new_direcor) :
        self.direcor=new_direcor

        
        

movie_1 =The_moves('Incrqtion','Shokry sarhon',2010,'SCI_FI')
movie_2=The_moves('The Godfather','Ahmed mazhar',1972,'Crime')
movie_3=The_moves('parasite','ismael yasine',2019,'Horror')
  
movie_1.print_the_moves()
movie_2.print_the_moves()
movie_3.print_the_moves()

movie_1.Edit('Ahmed mazhar')
movie_1.print_the_moves()

movie_2.Edit('abdo mota')
movie_2.print_the_moves()

movie_3.Edit('fife abko')
movie_3.print_the_moves()
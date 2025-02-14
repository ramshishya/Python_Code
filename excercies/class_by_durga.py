class Movie:
    """ This is the first program for OOPS by Ram """
    def __init__(self,title,hero,herion):
        print("Initialization")
        self.title=title
        self.hero=hero
        self.herion=herion
        
    def info(self):
     print("Movie name : ",self.title,"Hero Name= ",self.hero,"Herion name =" ,self.herion)

list_of_movie=[]
while True:
   title= input("what is the Movie Name")
   hero=input("What is the Hero Name")
   herion=input( "Please enter hero name")
   m=Movie(title,hero,herion)
   list_of_movie.append(m)
   print("movie added into list succesfuly")
   option=input("do you want me to add one more movie [yes|No]")
   if option.lower()=='no' :
        break
print("Print all Movie name")
for movie in list_of_movie:
    movie.info()
    

m=Movie('Bahubali','Prabhash','Anushkha')
m.info()
print(Movie.__doc__) 
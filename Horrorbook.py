import random
class Horrorbook:
  def __init__(self,):
      self.Firstword = random.choice(Firstword)
      self.Lastword = random.choice(Lastword)
      self.Pagenumber = random.randint(2,2000)
      self.Firstname = random.choice(Firstname)
      self.Lastname = random.choice(Lastname)

Firstword = [
   "Red",
   "The",
   "Deathly",
   "Silent",
   "It",
   "Someone",
   "Something",
   "Fluff",
   "Darkness",
   "Fallen",
   "Bone",
   "White",
   "Scream",
   "Wolf",
   "Monster",
   "Salvation",
   "Terror",
   "Horror",
   "A",
   "Underneath",
   "Before",
   "Conjure",
   "Creeper",
   "Starved",
   "Sleep",
   "Ghoul",
   "She",
   "Dark",
   "Shadow",
   "Grotesque",

 ]
Lastword = [
   "Death",
   "Died",
   "Lurks",
   "Prowls",
   "Garden",
   "Winter",
   "Vanished",
   "Breathes",
   "Me",
   "Stolen",
   "Jolly",
   "Blood",
   "Massacre",
   "Cries",
   "Promise",
   "Promised",
   "Dawn",
   "Below",
   "Lost",
   "Innocence",
   "Slaughter",
  ]

 ]

Firstname = [
    "J",
    "Kelsey",
    "James",
    "Samuel",
    "Jackson",
    "Paloma",
    "Benjamin",
    "Harmoni",
    "Haley",
    "Charity",
    "Lavender",
    "Morgan",
    "Arthur",
    "Gwen",
    "Lance",
    "Gawaine",
    "Veronica",
    "Mercy",
    "Sarah",
    "Brandon",
    "Ursula",
    "Mercedes",
    "Jo",
    "Naomi",
    "Robin",
    "Diana",
    "Selene",
    "Calypso",
    "Jason",
    "Percy",
    "Anne",
    "Edith",
    "Christopher",
    "Peter",
    "Mina",
    "Ariel",
    "Meredith",
    "Cassandra",
    "Icarus",
    "Ezekiel",
    ]

Lastname = [
    "Rowling",
    "O'Brian",
    "Queen",
    "Smithy",
    "Waters",
    "Walker",
    "Xavier",
    "Morgan",
    "Hunter",
    "Harker",
    "Baggins",
    "Moore",
    "Brooks",
    "Nasar",
    "Holmes",
    "Jenkins",
    "Stone",
    "Deacon",
    "Bishop",
    "Gray",
    "Summers",
    "Autumn",
    "Bell",
    "Roland",
    "Dover",
    "Baron",
    "Daniels",
    "Terrance",
    "Palmer",
    "Cooper",
    "Connors",
    "Frost",
    "Castle",
    "Booth",
    "Harper",
    "Crystal",
    "Everest",
    "Geils",


  ]

def main():
     printHeader()
     Horrorbooks = [
        Horrorbook(),
        Horrorbook(),
        Horrorbook(),
        Horrorbook(),
     ]

     selection = int(getUserSelection())
     if selection == 0:
         printHorrorbooksbyFirstword(Horrorbooks)
     elif selection == 1:
         printHorrorbooksbyLastword(Horrorbooks)
     elif selection == 2:
         printHorrorbooksbyPagenumber(Horrorbooks)
     elif selection == 3:
         printHorrorbooksbyFirstname(Horrorbooks)
     elif selection == 4:
         printHorrorbooksbyLastname(Horrorbooks)

     else: print ("SELECTION NOT RECOGNIZED")


inputQuestions =[
"For Scary Horrorbook by Firstword, type 0",
"For Terrifying Horrorbook by Lastword, type 1",
"For Horrifing Horrorbook by Pagenumber, type 2",
"For Frightening Horrorbook by Author's Firstname, type 3",
"For Blood Curdling Horrorbook by Author's Lastname, type 4"
]

def getUserSelection():
    print (inputQuestions[0])
    print (inputQuestions[1])
    print (inputQuestions[2])
    print (inputQuestions[3])
    print (inputQuestions[4])

    return input("Type Selection and press enter" )

def printHeader():
    print("HORRORBOOK INFO")

def printHorrorbooksbyFirstword(Horrorbooks):
    print ("----Horrorbooks by Firstword----")
    sortHorrorbooks = sorted(Horrorbooks, key=lambda Horrorbook: Horrorbook.Firstword)
    for Horrorbook in sortHorrorbooks:
        print(Horrorbook.Firstword + "," + Horrorbook.Lastword + "," + str(Horrorbook.Pagenumber) + "," + Horrorbook.Firstname + "," + Horrorbook.Lastname)
def printHorrorbooksbyLastword(Horrorbooks):
    print ("----Horrorbooks by Lastword----")
    sortHorrorbooks = sorted(Horrorbooks, key=lambda Horrorbook: Horrorbook.Lastword)
    for FantasyBook in sortFantasyBooks:
         print(Horrorbook.Lastword + "," + Horrorbook.Firstword + "," + str(Horrorbook.Pagenumber) + "," + Horrorbook.Firstname + "," + Horrorbook.Lastname)
def printHorrorbooksbyPagenumber(Horrorbooks):
    print("----Horrorbooks by Pagenumber----")
    sortHorrorbooks = sorted(Horrorbooks, key=lambda Horrorbook: str(Horrorbook.Pagenumber))
    for Horrorbook in sortHorrorbooks:
        print(str(Horrorbook.Pagenumber) + "," + Horrorbook.Firstword + "," + Horrorbook.Lastword + "," + Horrorbook.Firstname + "," + Horrorbook.Lastname)
def printHorrorbooksbyFirstname(Horrorbooks):
    print("----Horrorbooks by Firstname----")
    sortHorrorbooks = sorted(Horrorbooks, key=lambda Horrorbook: Horrorbook.Firstname)
    for Horrorbook in sortHorrorbooks:
        print(Horrorbook.Firstname + "," + Horrorbook.Lastname + "," + Horrorbook.Firstword + "," + Horrorbook.Lastword + "," + str(Horrorbook.Pagenumber))
def printHorrorbooksbyLastname(Horrorbooks):
    print("----Horrorbooks by Lastname----")
    sortHorrorbooks = sorted(Horrorbooks, key=lambda Horrorbook: Horrorbook.Lastname)
    for Horrorbook in sortHorrorbooks:
        print(Horrorbook.Lastname + "," + Horrorbook.Firstname + "," + Horrorbook.Firstword + "," + Horrorbook.Lastword + "," + str(Horrorbook.Pagenumber))
main()

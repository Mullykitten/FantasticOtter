import random
class FantasyBook:
  def __init__(self,):
      self.Firstword = random.choice(Firstword)
      self.Lastword = random.choice(Lastword)
      self.Pagenumber = random.randint(2,2000)
      self.Firstname = random.choice(Firstname)
      self.Lastname = random.choice(Lastname)

Firstword = [
   "Magical",
   "Grimm",
   "Fairy",
   "Elven",
   "Siren",
   "Jounrey",
   "Eternal",
   "Enchanted",
   "Cursed",
   "Conjure",
   "Mystic",
   "Bewitched",
   "Wonderful",
   "Wicked",
   "Glimmer",
   "Thrilling",
   "Beastly",
   "Sandman",
   "Lone",
   "Venomous",
   "Slayer of",
   "Peculiar",
   "Fantastic",
   "Disappearance of",
   "King of",
   "Lord of",
   "Queen of",
   "Below",
   "Fallen",
   "Miraculous",
   "Legend of",
   "Strange",
   "Dark",
   "Wonderous",

 ]
Lastword = [
   "Dragons",
   "Light",
   "Curses",
   "Beast",
   "Quest",
   "Realms",
   "Heroes",
   "Hero",
   "Monster",
   "Angels",
   "Good",
   "Evil",
   "Sky",
   "Earth",
   "Witches",
   "Magic",
   "Children",
   "Spirits",
   "Fire",
   "Ice",
   "Water",
   "Power",
   "Music",
   "Truth",
   "Phantoms",
   "Promises",
   "Wolves",
   "Falcons",
   "Gold",

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
     import Image
     image = Image.open("image." Lastword ".jpg")
     image.show(),

     FantasyBooks = [
        FantasyBook(),
     ]

     selection = int(getUserSelection())
     if selection == 0:
         printFantasyBooksbyFirstword(FantasyBooks)
     elif selection == 1:
         printFantasyBooksbyLastword(FantasyBooks)
     elif selection == 2:
         printFantasyBooksbyPagenumber(FantasyBooks)
     elif selection == 3:
         printFantasyBooksbyFirstname(FantasyBooks)
     elif selection == 4:
         printFantasyBooksbyLastname(FantasyBooks)

     else: print ("SELECTION NOT RECOGNIZED")


inputQuestions =[
"For Awesome FantasyBook by Firstword, type 0",
"For Awesome FantasyBook by Lastword, type 1",
"For Awesome FantasyBook by Pagenumber, type 2",
"For Awesome FantasyBook by Author's Firstname, type 3",
"For Awesome FantasyBook by Author's Lastname, type 4"
]

def getUserSelection():
    print (inputQuestions[0])
    print (inputQuestions[1])
    print (inputQuestions[2])
    print (inputQuestions[3])
    print (inputQuestions[4])

    return input("Type Selection and press enter" )

def printHeader():
    print("FANTASYBOOK INFO")

def printFantasyBooksbyFirstword(FantasyBooks):
    print ("----FantasyBooks by Firstword----")
    sortFantasyBooks = sorted(FantasyBooks, key=lambda FantasyBook: FantasyBook.Firstword)
    for FantasyBook in sortFantasyBooks:
        print(FantasyBook.Firstword + "," + FantasyBook.Lastword + "," + str(FantasyBook.Pagenumber) + "," + FantasyBook.Firstname + "," + FantasyBook.Lastname)
def printFantasyBooksbyLastword(FantasyBooks):
    print ("----FantasyBooks by Lastword----")
    sortFantasyBooks = sorted(FantasyBooks, key=lambda FantasyBook: FantasyBook.Lastword)
    for FantasyBook in sortFantasyBooks:
         print(FantasyBook.Lastword + "," + FantasyBook.Firstword + "," + str(FantasyBook.Pagenumber) + "," + FantasyBook.Firstname + "," + FantasyBook.Lastname)
def printFantasyBooksbyPagenumber(FantasyBooks):
    print("----FantasyBooks by Pagenumber----")
    sortFantasyBooks = sorted(FantasyBooks, key=lambda FantasyBook: str(FantasyBook.Pagenumber))
    for FantasyBook in sortFantasyBooks:
        print(str(FantasyBook.Pagenumber) + "," + FantasyBook.Firstword + "," + FantasyBook.Lastword + "," + FantasyBook.Firstname + "," + FantasyBook.Lastname)
def printFantasyBooksbyFirstname(FantasyBooks):
    print("----FantasyBooks by Firstname----")
    sortFantasyBooks = sorted(FantasyBooks, key=lambda FantasyBook: FantasyBook.Firstname)
    for FantasyBook in sortFantasyBooks:
        print(FantasyBook.Firstname + "," + FantasyBook.Lastname + "," + FantasyBook.Firstword + "," + FantasyBook.Lastword + "," + str(FantasyBook.Pagenumber))
def printFantasyBooksbyLastname(FantasyBooks):
    print("----Fantasy by Lastname----")
    sortFantasyBooks = sorted(FantasyBooks, key=lambda FantasyBook: FantasyBook.Lastname)
    for FantasyBook in sortFantasyBooks:
        print(FantasyBook.Lastname + "," + FantasyBook.Firstname + "," + FantasyBook.Firstword + "," + FantasyBook.Lastword + "," + str(FantasyBook.Pagenumber))
main()

import random
from PIL import Image
class Dog:
  def __init__(self,):
      self.Breed = random.choice(Breed)
      self.Gender = random.choice(Gender)
      self.Age = random.randint(1,12)
      self.Name = random.choice(Name)
      self.Personality = random.choice(Personality)


Breed = [
   "German Shepherd",
   "Dalmation",
   "Goldendoodle",
   "Newfoundland",
   "Gold Lab",
   "Coonhound",
   "Affenpinscher",
   "Rottweiler",
   "Corgi",
   "Rottweiler",
   "English Sheepdog",


 ]
Gender = [
   "Male",
   "Female",


 ]

Name = [
    "Jay",
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
    "Spot",
    "Dot",
    "Buddy",
    "Fluffy",
    "Abby",
    "Nemo",
    "Gus",
    "Simba",
    "Oliver",
    "Violet",
    "Buster",
    "Tank",
    "Annie",
    "Frannie",
    "Rockie",
    "Tucker",
    "Whitney",
    "Katie",
    "Samantha",

    ]

Personality = [
    "Sweet",
    "Quiet",
    "Shy",
    "Talkative",
    "Clever",
    "Energetic",
    "Lively",
    "Slow",
    "Friendly",
    "Patient",
    "Loyal",
    "Protective",
    "Social",
    "Sleepy",


  ]

def main():
     printHeader()
     Dogs = [
     Dog(),
     ]
     selection = int(getUserSelection())
     if selection == 0:
         printDogsbyBreed(Dogs)


     else:
         print ("SELECTION NOT RECOGNIZED")


inputQuestions =[
"For Awesome Pupper, type 0",
 ]

def getUserSelection():
    print (inputQuestions[0])


    return input("Type Selection and press enter" )

def printHeader():
    print("DOG INFO")

def printDogsbyBreed(Dogs):
    print ("----Dogs by Breed----")
    sortDogs = sorted(Dogs, key=lambda Dog: Dog.Breed)
    for Dog in Dogs:
        print(Dog.Breed + "," + Dog.Gender + "," + str(Dog.Age) + "," + Dog.Name + "," + Dog.Personality)
        image = Image.open("dogs/" + Dog.Breed + ".jpg")
        image.show("http://images2.fanpop.com/image/photos/13300000/Beautiful-Rottweiler-rottweiler-13378967-1280-800.jpg")







main()

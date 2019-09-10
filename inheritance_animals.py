import time

class animals():
    def __init__(self,age=1,nutrition="carnivorous",number_of_feet=4,living_places="land",genus=""):
        self.age=age
        self.nutrition=nutrition
        self.number_of_feet=number_of_feet
        self.living_places=living_places
        self.genus=genus

class dog(animals):
    def __init__(self,age=1,nutrition="carnivorous",number_of_feet=4,living_places="land",genus="pitbull",domestic="Yes"):
        super(dog,self).__init__(age,nutrition,number_of_feet,living_places,genus)

        self.domestic=domestic

    def __str__(self):
         return "Dog Informations:  \nAge : {} \nNutrition : {} \nNumber Of Feet : {} \nLiving Place : {} \nGenus : {} \nDomestic : {}".format(self.age,self.nutrition,self.number_of_feet,self.living_places,self.genus,self.domestic)

    def homes_dog(self):


        if self.domestic=="Yes":
            print("can enter the house")
        elif self.domestic=="No":
            print("unfortunately only in the garden")
        else:
           print("Yes or No")

class bird(animals):
    def __init__(self, age=1, nutrition="carnivorous", number_of_feet=2, living_places="air", genus="eagle",
                 predatory="Yes"):
        super(bird,self).__init__(age, nutrition, number_of_feet, living_places,genus)
        self.predatory = predatory
    def __str__(self):
        return "Bird Informations:  \nAge : {} \nNutrition : {} \nNumber Of Feet : {} \nLiving Place : {} \nGenus : {} \nPredatory : {}".format(self.age,self.nutrition,self.number_of_feet,self.living_places,self.genus,self.predatory)

    def predatory_bird(self, decision):
        if decision=="Yes":
            print("Run")
        elif decision=="No":

            print("dont worry")
        else:
            print("Yes or No")

class horse(animals):
    def __init__(self, age=1, nutrition="carnivorous", number_of_feet=4, living_places="land", genus="arabic horse",racehorse="Yes"):
        super(horse,self).__init__(age, nutrition, number_of_feet, living_places,genus)
        self.racehorse = racehorse
    def __str__(self):
        return "Horse Informations:  \nAge : {} \nNutrition : {} \nNumber Of Feet : {} \nLiving Place : {} \nGenus : {} \nRace Horse : {}".format(self.age,self.nutrition,self.number_of_feet,self.living_places,self.genus,self.racehorse)

    def race(self):
        race=input("do you want to race?  : ")
        if race=="Yes":
            if self.racehorse=="Yes" and self.age >= 3:
                print("this horse is a racehorse.you can race this horse")
            elif self.racehorse=="No" and self.age >= 3:
                print("this horse isn't a racehorse.you can not race this horse")
            elif self.racehorse=="Yes" and self.age < 3:
                print("Unfortunately, this horse is 3 under age")
            else:
                print("Enter values correctly")
        elif race=="No":
            print("You know if you don't want to race.")

        else:
            print("Yes or No")

animall=animals()
horsee=horse()
dogg=dog()
birdd=bird()
print("""
q.Quit
1.Dog Domestic
2.Dog Information
3.Horse Information
4.Bird Information
5.Horse Race?
6.Bird Predatory
7.Horse Information Updating
8.Bird Information Updating
9.Dog Information Updating
""")

while True:
    operation=input("Please enter the desired transaction : ")

    if operation=="q":
        print("good bye")

    elif operation=="1":
        d = input("What is the domestic : ")
        dogg.domestic = d
        dogg.homes_dog()


    elif operation=="2":
        print(dogg)
    elif operation=="3":
        print(horsee)
    elif operation=="4":
        print(birdd)


    elif operation=="5":
        horsee.race()
    elif operation=="6":
        a=input("is the bird of prey")
        birdd.predatory_bird(a)
    elif operation=="7":
        decision=input("Do you want to update horse information : ")
        if decision=="Yes":
            age=int(input("Enter your age : "))
            nutrition=input("Enter your nutrition : ")
            number_of_feet=int(input("Enter your number of feet : "))
            living_places=input("Enter your living place : ")
            genus=input("Enter your genus : ")
            racehorse=input("Enter your racehorse : ")
            print("Updating information...")
            time.sleep(1)
            horsee=horse(age,nutrition,number_of_feet,living_places,genus,racehorse)
            print("Mission Completed")

        elif decision=="No":
            print("Okay")
        else:
            print("Yes or No")

    elif operation=="8":
        decision=input("Do you want to update bird information : ")
        if decision=="Yes":
            age=int(input("Enter your age : "))
            nutrition=input("Enter your nutrition : ")
            number_of_feet=int(input("Enter your number of feet : "))
            living_places=input("Enter your living place : ")
            genus=input("Enter your genus : ")
            predatory=input("Enter your predatory : ")
            print("Updating information...")
            time.sleep(1)
            birdd=bird(age,nutrition,number_of_feet,living_places,genus,predatory)
            print("Mission Completed")

        elif decision == "No":
            print("Okay")
        else:
            print("Yes or No")

    elif operation=="9":
        decision=input("Do you want to update dog information : ")
        if decision=="Yes":
            age=int(input("Enter your age : "))
            nutrition=input("Enter your nutrition : ")
            number_of_feet=int(input("Enter your number of feet : "))
            living_places=input("Enter your living place : ")
            genus=input("Enter your genus : ")
            domestic=input("Enter your domestic : ")
            print("Updating information...")
            time.sleep(1)
            dogg=dog(age,nutrition,number_of_feet,living_places,genus,domestic)
            print("Mission Completed")
        elif decision=="No":
            print("Okay")
        else:
            print("Yes or No")

import random
import time
import os
import threading
import logging
import json
import ast







class Animations:

    def __init__(self):
        self.y = 0
        self.rightFactor = 0 #cat starts 0 characters to the right
        self.leftFactor = 232 #cat starts 232 characters to the left
        self.file = open('catAnimations', 'r')
        self.lines = self.file.readlines()
        self.facing = True #True = facing right | False = facing left

    def idle(self):
        pass

    def deathRight(self):
        x = random.randint(1,10)
        try:
            for line in self.lines[111:114]:
                print(f'{"  " * self.y}{line.rstrip()}')
            time.sleep(x)
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occured')

    def deathLeft(self):
        x = random.randint(1,10)
        try:
            for line in self.lines[116,119]:
                print(f'{"  " * self.y}{line.rstrip()}')
            time.sleep(x)
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occured')

    def walkRight(self, timesleep=0.1):
        x = random.randint(1, 58)
        try:
            for i in range(x):
                if self.rightFactor >= 232:
                    raise IndentationError

                for line in self.lines[16:19]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(timesleep)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.y += 1
                self.rightFactor = self.y * 2
                if self.rightFactor >= 232:
                    raise IndentationError

                for line in self.lines[21:24]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(timesleep)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.y += 1
                self.rightFactor = self.y * 2
                if self.rightFactor >= 232:
                    raise IndentationError

                if i == x - 1:
                    raise IndentationError

        except IndentationError:
            for line in self.lines[11:14]:
                print(f'{"  " * self.y}{line.rstrip()}')
            self.rightFactor = self.y * 2
            self.leftFactor = 232 - self.rightFactor
            self.facing = True

    def leftWalk(self, timesleep=0.1):
        x = random.randint(1, 58)
        try:
            for i in range(x):
                if self.leftFactor >= 232:
                    raise IndentationError

                for line in self.lines[31:34]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(timesleep)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.y -= 1
                self.leftFactor = self.y * 2
                if self.leftFactor >= 232:
                    raise IndentationError
                if self.y < 0:
                    raise IndentationError

                for line in self.lines[36:39]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(timesleep)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.y -= 1
                self.leftFactor = self.y * 2
                if self.leftFactor >= 232:
                    raise IndentationError
                if self.y < 0:
                    raise IndentationError

                if i == x - 1:
                    raise IndentationError

        except IndentationError:
            for line in self.lines[26:29]:
                print(f'{"  " * self.y}{line.rstrip()}')
            self.leftFactor = 232 - (self.y * 2)
            self.rightFactor = 232 - self.leftFactor
            self.facing = False

    def eatingRight(self):
        x = random.randint(1,10)
        try:
            for i in range(x):
                for line in self.lines[41:44]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[46:49]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[51:54]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occured.')

        finally:
            for line in self.lines[41:44]:
                print(f'{"  " * self.y}{line.rstrip()}')
            time.sleep(1.2)
            os.system('cls' if os.name == 'nt' else 'clear')
            for line in self.lines[1:4]:
                print(f'{"  " * self.y}{line.rstrip()}')

    def eatingLeft(self):
        x = random.randint(1,10)
        try:
            for i in range(x):
                for line in self.lines[56:59]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[61:64]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[66:69]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occured.')

        finally:
            for line in self.lines[56:59]:
                print(f'{"  " * self.y}{line.rstrip()}')
            time.sleep(1.2)
            os.system('cls' if os.name == 'nt' else 'clear')
            for line in self.lines[6:9]:
                print(f'{"  " * self.y}{line.rstrip()}')

    def sleepRight(self):
        x = random.randint(20,120)
        try:
            for i in range(x):
                for line in self.lines[71:74]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[76:79]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[81:84]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occured.')

        finally:
            x = random.randint(2,4)
            jd = random.randint(1, 2)
            for i in range(jd):
                for line in self.lines[86:89]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(x):
                for line in self.lines[71:74]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[86:89]:
                    print(f'{"  " * self.y}{line.rstrip()}')
                time.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
            for line in self.lines[1:4]:
                print(f'{"  " * self.y}{line.rstrip()}')

    def sleepLeft(self):
        x = random.randint(20,50)
        try:
            for i in range(x):
                for line in self.lines[91:94]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[96:99]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[101:104]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occured.')

        finally:
            x = random.randint(2,4)
            jd = random.randint(1,2)
            for i in range(jd):
                for line in self.lines[106:109]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

            for i in range(x):
                for line in self.lines[91:94]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[106:109]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.2)
                os.system('cls' if os.name == 'nt' else 'clear')
            for line in self.lines[6:9]:
                print(f'{"  " * (self.y-2)}{line.rstrip()}')

    def cleanRight(self):
        x = random.randint(10,20)
        try:
            for i in range(x):
                for line in self.lines[121:114]:
                    print(f'{"  " * (self.y)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[126:129]:
                    print(f'{"  " * (self.y)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occurred')

    def cleanLeft(self):
        x = random.randint(10, 20)
        try:
            for i in range(x):
                for line in self.lines[131:134]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')

                for line in self.lines[136:139]:
                    print(f'{"  " * (self.y-2)}{line.rstrip()}')
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print('An error occurred')


class MainGame:
    petName = str
    health = int
    hunger = int
    happiness = int
    sleepStatus = int
    day = int
    pause = bool
    foodAvaliable = dict
    gameInfo = dict
    money = float
    counter = int

    def __init__(self, username='username', petName='Name', health=100, hunger=0, happiness=100, sleepStatus=0, day=1,
                 pause=False, foodAvaliable={1: ['Meat', 5, 10, -60, 40, -5], 2: ['Cat Nip',2, -5, -10, 90, -2],
                                             3: ['Tuna', 4, 15, -50, 50, -5], 4: ['Cheese', 3, 10, -30, 30, -2],
                                             5: ['Normal Cat Food', 2, 30, -40, 5, -1]}, gameInfo={}, money=60, counter=120, animationsInstance = Animations()):
        self.username = username
        self.petname = petName
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.sleepStatus = sleepStatus  # number of days since last sleep
        self.day = day
        self.pause = pause
        self.foodAvaliable = foodAvaliable
        self.gameInfo = gameInfo  # [username] : [petName, health, hunger, happiness, sleepStatus, day, pause, foodAvaliable, money, counter]
        self.money = money
        self.daytempsomething = 0
        self.counter = counter
        self.animationsInstance = animationsInstance
        self.storeFood = {1: ['Meat', 5, 10, -60, 40, -5, 30], 2: ['Cat Nip',5, -5, -10, 90, -2, 10], 3: ['Tuna', 5, 15, -50, 50, -5, 20], 4: ['Cheese', 5, 10, -30, 30, -2, 15], 5: ['Normal Cat Food', 5, 30, -40, 5, -1, 5]}

    def startGame(self):
        print(f'Starting game with {self.petname}')
        while True:
            print('\n---------------------------------------------------')
            print(f'| Pet: {self.petname}\t| Health: {self.health}%\t| Hunger: {self.hunger}%\t'
                  f'| Happiness: {self.happiness}%\t| Sleepiness: {self.sleepStatus}%\t'
                  f'| Day: {self.day}\t| Seconds Until Next Day: {self.counter}')
            print('\n- - Please select an action - -\n')
            print('1: Feed\n')
            print('2: Sleep\n')
            print('3: Clean\n')
            print('4: Take on a Walk\n')
            print('5: Check Status\n')
            print('6: Go Shopping\n')
            print('7: Pause\n')
            print('8: Quit to Menu\n')

            if self.health <= 0:
                print(f'{self.petname.title} has died. The simulator is now over.')
                if self.animationsInstance.facing == True:
                    self.animationsInstance.deathRight()
                elif self.animationsInstance.facing == False:
                    self.animationsInstance.deathLeft()
                self.saveGame()
                print('Your game has been automatically saved and you are being sent back to the main menu.')
                return

            if self.daytempsomething < self.day:
                self.daytempsomething += 1
                format = '\nNOTIFICATION: %(message)s'
                logging.basicConfig(format=format, level=logging.INFO,
                                    datefmt='%H:%M:%S')
                t = threading.Thread(target=self.dayTimer)
                t.start()

            try:
                time.sleep(0.5)
                user = int(input('Enter: '))

                if user > 8 or user < 0:
                    raise ValueError

                elif user == 1:
                    self.feed() #done

                elif user == 2:
                    self.sleep() #done

                elif user == 3:
                    self.clean() #done

                elif user == 4:
                    self.walk() #done

                elif user == 5:
                    self.checkStatus() #done

                elif user == 6:
                    self.goShopping() #done

                elif user == 7:
                    self.pauseFunc()

                elif user == 8:
                    while True:
                        savePrompt = input('Save (y/n): ')
                        if savePrompt.lower() == 'y':
                            self.gameInfo[self.username] = [self.petname, self.health, self.happiness, self.sleepStatus,
                                                            self.day, self.pause, self.foodAvaliable, self.money, self.counter]
                            break
                        elif savePrompt.lower() == 'n':
                            print('Closing game unsaved')
                            break
                        else:
                            print('Please enter a valid input')
                    print(f'Thank you for playing the Pet Caring Simulator!')

                else:
                    raise ValueError

            except ValueError:
                print('Please enter a valid input.\n\n')

    def dayTimer(self):
        logging.info(f'Day {self.day}')

        dayCounter = self.counter
        while dayCounter > 0:
            if self.pause == False:
                dayCounter -= 1
            time.sleep(1)

        self.day += 1
        self.sleepStatus += random.randint(30,50)
        logging.info(f'Day {self.day} Has Begun!\n')
        self.storeRestock()


    def storeRestock(self):
        for key in self.storeFood:
            q = random.randint(3,6)
            while q < self.storeFood[key][1]:
                q = random.randint(3,6)
            self.storeFood[key][1] = q

    def statusCheck(self):
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0
        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0
        if self.sleepStatus > 100:
            self.sleepStatus = 100
        elif self.sleepStatus < 0:
            self.sleepStatus = 0

    def printStats(self):
        print(f'{self.petname}:')
        print(f'     -Health: {self.health}')
        print(f'     -Hunger: {self.hunger}')
        print(f'     -Happiness: {self.happiness}')
        print(f'     -Sleepiness: {self.sleepStatus}')
        time.sleep(2)

    def feed(self):
        for key in self.foodAvaliable:
            print(f'{key}: {self.foodAvaliable[key][0]}')
            print(f'     -Amount: {self.foodAvaliable[key][1]}')
            print(f'     -Health: {self.foodAvaliable[key][2]}%')
            print(f'     -Hunger: {self.foodAvaliable[key][3]}%')
            print(f'     -Happiness: {self.foodAvaliable[key][4]}%')
            print(f'     -Sleepiness: {self.foodAvaliable[key][5]}%')

        while True:
            try:
                feedUser = int(input(f'Please type the number to feed {self.petname} that food: '))
                if len(self.foodAvaliable) == 0:
                    print(f'There is no food to feed {self.petname}. Please buy some and come back.')
                elif feedUser < 0 or feedUser > len(self.foodAvaliable):
                    raise ValueError

                else:
                    if self.foodAvaliable[feedUser][1] <= 0:
                        print(f'There are not any {self.foodAvaliable[feedUser]} available at the moment. Please buy some and come back, or use another food.')
                    else:
                        print(f'Now feeding {self.petname} {self.foodAvaliable[feedUser][0]}')
                        time.sleep(0.5)
                        self.foodAvaliable[feedUser][1] -= 1
                        self.health += self.foodAvaliable[feedUser][2]
                        self.hunger += self.foodAvaliable[feedUser][3]
                        self.happiness += self.foodAvaliable[feedUser][4]
                        self.sleepStatus += self.foodAvaliable[feedUser][5]
                        self.statusCheck()

                        if self.animationsInstance.facing == True:
                            self.animationsInstance.eatingRight()
                        elif self.animationsInstance.facing == False:
                            self.animationsInstance.eatingLeft()

                        time.sleep(2.5)
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print(f'{self.petname} is very happy you fed them! Here are their new stats: ')

                        self.printStats()
                        time.sleep(2)
                        wieujhf = input('Enter anything to continue...\n')
                        break


            except ValueError:
                print('Please enter a valid input\n')

    def play(self):
        print('PLAY STANDBY')

    def sleep(self):
        if self.animationsInstance.facing == True:
            self.animationsInstance.sleepRight()
        elif self.animationsInstance.facing == False:
            self.animationsInstance.sleepLeft()
        self.sleepStatus -= random.randint(55, 90)
        self.statusCheck()

        jfj = random.randint(1,20)
        if jfj == 20:
            print(f'Oh no! {self.petname.title()} woke up feeling groggy! They\'re still super sleepy. Their new stats are listed below:')
            self.sleepStatus += 80
            self.happiness -= 20
            self.statusCheck()
            self.printStats()
            wieujhf = input('Enter anything to continue...\n')
        else:
            print(f'{self.petname.title()} slept so well! Their new stats are listed below:')
            self.printStats()
            wieujhf = input('Enter anything to continue...\n')




    def clean(self):
        if self.animationsInstance.facing == True:
            self.animationsInstance.cleanRight()
        elif self.animationsInstance.facing == False:
            self.animationsInstance.cleanLeft()
        print(f'{self.petname} enjoyed their bath and is feeling super clean! Their new stats are listed below:')
        psw = random.randint(40, 70)
        self.happiness += psw
        self.health += (psw / 2)
        self.statusCheck()
        self.printStats()
        wieujhf = input('Enter anything to continue...\n')

    def walk(self):
        print(f'You are now taking {self.petname} on a walk!')

        q = 0
        while True:
            try:
                walkDirect = int(input(f'1: Left\n2: Run Left\n3: Right\n4: Run Right\n5: Stop Walking {self.petname}\nEnter: '))
                if walkDirect > 5 or walkDirect < 1:
                    raise ValueError
                elif walkDirect == 1:
                    self.animationsInstance.leftWalk()
                    q += 1
                elif walkDirect == 2:
                    self.animationsInstance.leftWalk(0.01)
                    q += 2
                elif walkDirect == 3:
                    self.animationsInstance.walkRight()
                    q += 1
                elif walkDirect == 4:
                    self.animationsInstance.walkRight(0.01)
                    q += 2
                elif walkDirect == 5:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid input\n')
        print(f'{self.petname.title()} is really happy they went on a walk! Their new stats are listed below: ')
        self.health += (10 + (2*q))
        self.hunger += (30 + (5*q))
        self.happiness += (35 + (5*q))
        self.sleepStatus += (37 + (5*q))
        self.statusCheck()
        self.printStats()

        wieujhf = input('Enter anything to continue...\n')

    def checkStatus(self):
        print(f'\n\nGetting {self.petname}\'s Stats...')
        barHealth = '|' * self.health
        barHunger = '|' * self.hunger
        barHappiness = '|' * self.happiness
        barSleep = '|' * self.sleepStatus

        print(f'    Health: {barHealth}\n'
              f'    Hunger: {barHunger}\n'
              f' Happiness: {barHappiness}\n'
              f'Sleepiness: {barSleep}\n'
              f'            0%       10%      20%       30%       40%       50%       60%       70%       80%       90%       100%\n'
              f'            ------------------------------------------------------------------------------------------------------')
        wieujhf = input('Enter anything to continue...\n')

    def goShopping(self):
        print('Welcome to the Store!! We restock every day! \nHere is the avaliable stock:\n')
        time.sleep(0.5)

        while True:
            for key in self.storeFood:
                print(f'{key}: {self.storeFood[key][0]}')
                print(f'     -Amount: {self.storeFood[key][1]}')
                print(f'     -Health: {self.storeFood[key][2]}%')
                print(f'     -Hunger: {self.storeFood[key][3]}%')
                print(f'     -Happiness: {self.storeFood[key][4]}%')
                print(f'     -Sleepiness: {self.storeFood[key][5]}%')
                print(f'     -Cost: ${self.storeFood[key][6]}')
            print(f'{len(self.storeFood)+1}: Quit')

            try:
                storeUser = int(input('\nEnter the number relating to the food you would like to buy: '))
                if len(self.storeFood) == 0:
                    print('There is no food avaliable to buy. Please come back later.')
                    break
                elif storeUser < 0 or storeUser > len(self.storeFood)+1:
                    raise ValueError

                elif storeUser == len(self.storeFood)+1:
                    print('Thank you for shopping with us!')
                    break

                elif self.money < self.storeFood[storeUser][6]:
                    print(f'{self.storeFood[storeUser][0]} costs {self.storeFood[storeUser][6]}, but you only have {self.money}. You cannot buy this currently.')
                    time.sleep(1)

                else:
                    if self.storeFood[storeUser][1] <= 0:
                        print(f'There are not any {self.storeFood[storeUser][0]} avaliable at the moment.')
                    else:
                        print(f'Ok! You have now bought the {self.storeFood[storeUser][0]}!')
                        self.foodAvaliable[storeUser][1] += 1
                        self.storeFood[storeUser][1] -= 1
                        self.money -= self.storeFood[storeUser][6]
                time.sleep(1)
            except ValueError:
                print('Please enter a valid input')
                time.sleep(1)
        time.sleep(2)

    def pauseFunc(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Game Paused.')
        self.pause = True
        while True:
            print('\nPause Menu')
            print('1: Resume')
            print('2: Options')
            print('3: Quit to Menu')
            try:
                pauseUser = int(input('Enter:'))
                if pauseUser < 0 or pauseUser > 3:
                    raise ValueError
                elif pauseUser == 1:
                    print('Game Resumed')
                    self.pause = False
                    break
                elif pauseUser == 2:
                    print()#PUT IN CODE

                elif pauseUser == 3:
                    print('Quitting...')
                    savePrompt = input('Save? \n(y/n): ')
                    if savePrompt.lower() == 'y':
                        self.saveGame()
                        return
                    else:
                        return

            except ValueError:
                print('Please enter a valid input.')

    def saveGame(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.gameInfo[self.username] = [self.petname, self.health, self.hunger, self.happiness, self.sleepStatus,
                                        self.day, self.pause, self.foodAvaliable, self.money, self.counter]
        try:
            with open('gameStorage.txt', 'r') as file:
                existingData = file.read()
                existingData = ast.literal_eval(existingData) if existingData else {}
        except FileNotFoundError:
            existingData = {}
        #json.dump(self.gameInfo, open('gameStorage.txt', 'w'))
        #print(self.gameInfo)

        existingData.update(self.gameInfo)

        with open('gameStorage.txt', 'w') as file:
            file.write(str(existingData))
            print('Data successfully stored')


def loadGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        with open('gameStorage.txt', 'r') as file:
            data = file.read()
            return ast.literal_eval(data) if data else {}
    except FileNotFoundError:
        print('File not found')
        return {}
    #gameInfo = json.load(open('gameStorage.txt'))
    #return gameInfo



def changeOptions():
    options = [100, 0, 100, 0, 1,
               {1: ['Meat', 5, 10, -60, 40, -5], 2: ['Cat Nip', 2, -5, -10, 90, -2], 3: ['Tuna', 4, 15, -50, 50, -5],
                4: ['Cheese', 3, 10, -30, 30, -2], 5: ['Normal Cat Food', 2, 30, -40, 5, -1]}, 0, 120]
    baseOptions = [100, 0, 100, 0, 1,
               {1: ['Meat', 5, 10, -60, 40, -5], 2: ['Cat Nip', 2, -5, -10, 90, -2], 3: ['Tuna', 4, 15, -50, 50, -5],
                4: ['Cheese', 3, 10, -30, 30, -2], 5: ['Normal Cat Food', 2, 30, -40, 5, -1]}, 0, 120]

    while True:
        try:
            print('1: Change Health\n'
                  '2: Change Hunger\n'
                  '3: Change Happiness\n'
                  '4: Change Sleep Status\n'
                  '5: Change Starting Day\n'
                  '6: Change Food Avaliable\n'
                  '7: Change Money\n'
                  '8: Change Day timer\n'
                  '9: Reset Options\n'
                  '10: Exit')
            optionsUser = int(input('\nEnter: '))
            if optionsUser > 10 or optionsUser < 0:
                raise ValueError
            elif optionsUser == 1:
                userHealth = int(input(f'Health is currently at 100. Enter new value: '))
                if userHealth <= 0:
                    raise ValueError
                else:
                    options[0] = userHealth
            elif optionsUser == 2:
                userHunger = int(input(f'Hunger is currently at 0. Enter new value: '))
                if userHunger <= 0:
                    raise ValueError
                else:
                    options[1] = userHunger
            elif optionsUser == 3:
                userHappiness = int(input(f'Happiness is currently at 100. Enter new value: '))
                if userHappiness <= 0:
                    raise ValueError
                else:
                    options[2] = userHappiness
            elif optionsUser == 4:
                userSleepStatus = int(input(f'Sleep Status is currently at 0. Enter new value: '))
                if userSleepStatus <= 0:
                    raise ValueError
                else:
                    options[3] = userSleepStatus
            elif optionsUser == 5:
                userDay = int(input(f'Day is currently at 1. Enter new value: '))
                if userDay <= 0:
                    raise ValueError
                else:
                    options[4] = userDay
            elif optionsUser == 6:
                print('COMING SOON')
            elif optionsUser == 7:
                userMoney = int(input(f'Money is currently at 0. Enter new value: '))
                options[6] = userMoney
            elif optionsUser == 8:
                userCounter = int(input(f'Day timer is currently at 120 seconds (2 minutes). Enter new value: '))
                if userCounter <= 0:
                    raise ValueError
                else:
                    options[7] = userCounter
            elif optionsUser == 9:
                options = baseOptions
            elif optionsUser == 10:
                return options
        except ValueError:
            print('Please enter a valid input\n')
    return options

def startMenu():

    options = [100, 0, 100, 0, 1,
               {1: ['Meat', 5, 10, -60, 40, -5], 2: ['Cat Nip', 2, -5, -10, 90, -2], 3: ['Tuna', 4, 15, -50, 50, -5],
                4: ['Cheese', 3, 10, -30, 30, -2], 5: ['Normal Cat Food', 2, 30, -40, 5, -1]}, 0, 120]

    while True:
        print('---------------------------------------------------------------------\n'
              'Welcome to the Pet Caring Simulator!! Please enter your choice below!\n'
              '\n'
              '1: New Game\n'
              '2: Load Game\n'
              '3: Options\n'
              '4: Credits\n')


        try:
            user = int(input('Enter: '))
            if user > 4 or user < 1:
                raise ValueError

            elif user == 1:
                userusername = input('Username: ')
                userpetname = input('Pet Name: ')
                if userusername == '' and userpetname == '':
                    mainGame = MainGame(health = options[0], hunger = options[1], happiness = options[2], sleepStatus = options[3],
                                       day = options[4], foodAvaliable = options[5], money = options[6], counter = options[7])
                    mainGame.startGame()
                elif not userusername == '' and userpetname == '':
                    mainGame = MainGame(username = userusername, health = options[0], hunger = options[1], happiness = options[2], sleepStatus = options[3],
                                       day = options[4], foodAvaliable = options[5], money = options[6], counter = options[7])
                    mainGame.startGame()
                elif userusername == '' and not userpetname == '':
                    mainGame = MainGame(petName = userpetname, health = options[0], hunger = options[1], happiness = options[2], sleepStatus = options[3],
                                       day = options[4], foodAvaliable = options[5], money = options[6], counter = options[7])
                    mainGame.startGame()
                elif not userusername == '' and not userpetname == '':
                    mainGame = MainGame(username = userusername, petName = userpetname, health = options[0], hunger = options[1], happiness = options[2], sleepStatus = options[3],
                                       day = options[4], foodAvaliable = options[5], money = options[6], counter = options[7])
                    mainGame.startGame()



            elif user == 2:
                gameInfo = loadGame()
                usernamejljl = input('Enter your username: ')
                if usernamejljl in gameInfo:
                    loadpetname = gameInfo[usernamejljl][0]
                    loadhealth = gameInfo[usernamejljl][1]
                    loadhunger = gameInfo[usernamejljl][2]
                    loadhappiness = gameInfo[usernamejljl][3]
                    loadSleep = gameInfo[usernamejljl][4]
                    loadday = gameInfo[usernamejljl][5]
                    loadpause = gameInfo[usernamejljl][6]
                    loadfood = gameInfo[usernamejljl][7]
                    loadmoney = gameInfo[usernamejljl][8]
                    loadcounter = gameInfo[usernamejljl][9]

                    if loadpetname == '':

                        mainGame = MainGame(username = usernamejljl, health = loadhealth, hunger = loadhunger, happiness = loadhappiness, sleepStatus = loadSleep, day = loadday, pause = loadpause,
                                       foodAvaliable = loadfood, money = loadmoney, counter = loadcounter)
                        mainGame.startGame()
                    else:
                        mainGame = MainGame(username=usernamejljl, petName=loadpetname, health=loadhealth,
                                            hunger=loadhunger, happiness=loadhappiness, sleepStatus=loadSleep, day=loadday,
                                            pause=loadpause,
                                            foodAvaliable=loadfood, money=loadmoney, counter=loadcounter)
                        mainGame.startGame()
                else:
                    print('Username not found.')

            elif user == 3:
                options = changeOptions()

            elif user == 4:
                pass #PUT IN CREDITS

        except ValueError:
            print('Please enter a valid input.\n')





Animations = Animations()
while False:
    user = input(':')
    if user == '1':
        print(Animations.leftWalk())
    elif user == '2':
        print(Animations.walkRight())
    elif user == '3':
        print(Animations.y, Animations.rightFactor, Animations.leftFactor)
    elif user == '4':
        if Animations.facing == True:
            print(Animations.eatingRight())
        elif Animations.facing == False:
            print(Animations.eatingLeft())
    elif user == '5':
        if Animations.facing == True:
            print(Animations.sleepRight())
        elif Animations.facing == False:
            print(Animations.sleepLeft())


while True:
    print(startMenu())






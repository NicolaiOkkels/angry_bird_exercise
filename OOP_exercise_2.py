
class Board:

    def __init__(self):
        pass

    def drawBoard(self):
        pig = Pig('P')
        bird = Bird('B',1,1)
        for i in range(10):
            print('*', end=" ")
            for j in range(10):
                if (j,i) == (pig.x, pig.y):
                    print(pig.name, end=" ")
                elif (j,i) == (bird.x, bird.y):
                    print(bird.name, end=" ")
                else:
                    print('*', end=" ")
            print('')

class Bird:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y

    def getName(self):
        return self.name

    def __repr__(self): 
        return "X: % s Y: % s" % (self.x, self.y) 
        
class Pig:

    def __init__(self, name, x = 4, y = 1):
        self.name = name
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    def getName(self):
        return self.name

class GameLoop:
    def __init__(self):
        pass

    def run(self):
        board = Board()
        pig = Pig('P')
        bird = Bird('B',1,1)
        print('--------------------------')
        board.drawBoard()
        print('--------------------------')
        
        #First command 
        value = ''
        won = False

        while(value != 'q'):
            value = input()
            
            if value == 'f':
                temp = bird.getX()
                if 0 <= temp <= 9:
                    temp += 1
                    bird.setX(temp)
                    print('move forward')
                else:
                    print('Cant move outside the board')
            elif value == 'l':
                temp = bird.getY()
                if 1 <= temp <= 9:
                    temp -= 1
                    bird.setY(temp)
                    print('move left')
                else:
                    print('Cant move outside the board')    
            elif value == 'r':
                temp = bird.getY()
                if 0 <= temp <= 8:
                    temp += 1
                    bird.setY(temp)
                    print('move right')
                else:
                    print('Cant move outside the board')
            elif value == 'p':
                print(f'current position: {bird.getX}, {bird.getY}')
            elif value == 'q':
                if  won == True:
                    print('You defeated the pig!!')
                else:
                    print('You lost..')
                exit()
            else: 
                print('invalid input: {value}')
            if (bird.x,bird.y) == (pig.x, pig.y):
                won = True
                print(won)

print('What steps do you want to perform')
print('Options: move forward (f), turn left (l), turn right (r)')
print('Type "q" to quit the game')

game = GameLoop()
game.run()

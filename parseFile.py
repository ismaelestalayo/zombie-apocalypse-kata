import sys
import os


INPUT_FILE = sys.argv[1]


"""##################################################################
CLASSES"""
class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def findPlayer(playerList, name):
    return [p for p in playerList if p.name == name][0]

class Player():
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
    
    def __repr__(self):
        return str(self.toArray()).replace("'", '"')
    
    def toArray(self):
        return [type(self).__name__.lower(), self.coords.x, self.coords.y]


class Zombie(Player):
    def __init__(self, name, coords):
        super().__init__(name, coords)   
    


class Survivor(Player):
    def __init__(self, name, coords, life, exp, numItems):
        super().__init__(name, coords)
        self.life = life
        self.exp = exp
        self.numItems = numItems
    
    def addItem(self, items):
        self.items = items


class SurvivorItem():
    def __init__(self, name, slot):
        self.name = name
        self.slot = slot


class SceneItem():
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
    
    def __repr__(self):
        return str(self.toArray()).replace("'", '"')
    
    def toArray(self):
        return [self.name.lower(), self.coords.x, self.coords.y]


class State():
    def __init__(self, survivors, zombies, sceneItems):
        self.survivors = survivors
        self.zombies = zombies
        self.sceneItems = sceneItems


class Instruction():
    def __init__(self, type):
        self.type = type
    
    def play(state):
        return state

class Move(Instruction):
    def __init__(self, player, direction):
        super().__init__("M")
        self.player = player
        self.direction = direction
    
    def play(state):
        
        # newState = State()
        return


class MoveItem(Instruction):
    def __init__(self, survivor, item, slot):
        super().__init__("R")
        self.survivor = survivor
        self.item = item
        self.slot = slot

class PickUp(Instruction):
    def __init__(self, survivor, item, slot):
        super().__init__("P")
        self.survivor = survivor
        self.item = item
        self.slot = slot

class Attack(Instruction):
    def __init__(self, player1, player2, weapon, effective):
        super().__init__("A")
        self.player1 = player1
        self.player2 = player2
        self.weapon = weapon
        self.effective = effective





def read_file(file_path):
    file = open(file_path, "r")
    return file.readlines()


def readLine(line):
    return line.replace("\n", "").split(" ")



"""metadata"""
def readMetadata(lines):
    return [int(d) for d in readLine(lines[0])]


"""survivors"""
def readSurvivor(line):
    metadata = [d for d in readLine(line)]
    survivor = Survivor(
        life = int(metadata[0]),
        exp = int(metadata[1]),
        numItems = int(metadata[2]),
        coords = Coord(int(metadata[3]), int(metadata[4])),
        name = metadata[5]
    )
    return survivor

def readSurvivorItems(lines, startLine, numItems):
    items = []
    for i in range(startLine, startLine + numItems):
        line = readLine(lines[i])
        item = SurvivorItem(
            name = line[0],
            slot = line[1]
        )
        items += [item]
    return items


def readSurvivors(lines, numSurvivors):
    survivors = []
    numLinea = 1
    for i in range(1, 1+numSurvivors):
        survivor = readSurvivor(lines[numLinea])
        numLinea += 1
        items = readSurvivorItems(lines, numLinea, survivor.numItems)
        numLinea += survivor.numItems
        survivor.addItem([items])
        survivors += [survivor]
    return survivors


"""##################################################################
ZOMBIES """
def zombiesStartingLine(survivors):
    startLine = 1
    for survivor in survivors:
        startLine += 1 + survivor.numItems
    return startLine


def readZombies(lines, numZombies, startLine):
    zombies = []
    for line in lines[startLine: startLine + numZombies]:
        name, x, y = readLine(line)
        zombie = Zombie(
            name=name,
            coords=Coord(int(x), int(y))
        )
        zombies += [zombie]
    return zombies


"""##################################################################
ZOMBIES """
def readSceneItems(lines, numSceneItems, startLine):
    sceneItems = []
    for line in lines[startLine: startLine + numSceneItems]:
        line = readLine(line)
        item = SceneItem(
            name=line[0],
            coords=Coord(int(line[1]), int(line[2]))
        )
        sceneItems += [item]
    return sceneItems


"""##################################################################
INSTRUCTIONS """
def readInstructions(lines, numInstructions, startLine):
    instructions = []
    for line in lines[startLine: startLine + numInstructions]:
        line = readLine(line)
        instructionType = line[0]
        if (instructionType == "M"):
            instructions += [Move(
                player = line[1],
                direction= line[2]
            )]
        elif (instructionType == "P"):
            instructions += [PickUp(
                survivor=line[1],
                item=line[2],
                slot= line[3]
            )]
        elif (instructionType == "R"):
            instructions += [MoveItem(
                survivor=line[1],
                item=line[2],
                slot=line[3]
            )]
        elif (instructionType == "A"):
            instructions += [Attack(
                player1=line[1],
                player2=line[2],
                weapon=line[3],
                effective=int(line[4])
            )]
            
    return instructions



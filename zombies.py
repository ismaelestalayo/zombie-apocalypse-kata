from parseFile import *


lines = read_file(INPUT_FILE)
numSurvivors, numZombies, numSceneItems, sceneSize, numInstructions = readMetadata(lines)
survivors = readSurvivors(lines, numSurvivors)


zombieStartLine = zombiesStartingLine(survivors)
zombies = readZombies(lines, numZombies, zombieStartLine)

sceneItemsStartLine = zombieStartLine + numZombies
sceneItems = readSceneItems(lines, numSceneItems, sceneItemsStartLine)

instructionsStartLine = sceneItemsStartLine + numSceneItems
instructions = readInstructions(lines, numInstructions, instructionsStartLine)

currentState = State(
    survivors=survivors,
    zombies=zombies,
    sceneItems=sceneItems
)
states = [currentState]

NUM_INSTRUCTIONS = 0



def movePlayer(instruction, state):
    foundSurvivor = [s for s in survivors if s[5] == instruction[1]]
    player = findPlayer( state.zombies + state.survivors, instruction.player)
    return 


def playTurn(instruction, currentState):
    return






"""
file:///Users/jorgefuentelasala/Desktop/zombies/zombies.html?scenario=8&elements=%5B%5B%22zombie%22%2C0%2C0%5D%2C%5B%22survivor%22%2C2%2C3%5D%2C%5B%22machete%22%2C4%2C5%5D%5D
"""

for instruction in instructions:
    if (type(instruction) == Move):
        print()



def parseURL(states):
    queryString = f"zombies.html?scenario={sceneSize}&"
    
    # elements=zombie%2C0%2C0%5D%2Csurvivor%2C2%2C3%5D%2Cmachete%2C4%2C5%5D%5D"
    for state in states:
        queryString += "elements=zombie"
        for zombie in state.zombies:
            return ""
    return ""
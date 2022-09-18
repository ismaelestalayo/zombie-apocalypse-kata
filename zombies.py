from parseFile import *


import os
import webbrowser


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








elements = [z for z in zombies] + [s for s in survivors] + [i for i in sceneItems]
elements = str(elements).replace(" ", "")

FILE = os.path.abspath("zombies-web/zombies.html")
URL = f"file:///{FILE}?scenario={sceneSize}&elements={elements}"


# TODO: animate instructions
for instruction in instructions:
    if (type(instruction) == Move):
        print()



print("> Copy and paste this URL in the browser: ")
print("> (webbrowser library has problems opening a local website with query parammeters): \n")
print(URL + "\n\n")

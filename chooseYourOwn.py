'''
Choose your own adventure. Basic shell

Let's start with a map that looks like this:

------------------------------
|     |     |     |     |     |
|  1  |  2  |  3  |  4  |  5  |
|     |     |     |     |     |
------------------------------
|     |     |     |     |     |
|  6  |  7  |  8  |  9  | 10  |
|     |     |     |     |     |
------------------------------
|     |     |     |     |     |
| 11  | 12  | 13  | 14  | 15  |
|     |     |     |     |     |
------------------------------
|     |     |     |     |     |
| 16  | 17  | 18  | 19  | 20  |
|     |     |     |     |     |
------------------------------
|     |     |     |     |     |
| 21  | 22  | 23  | 24  | 25  |
|     |     |     |     |     |
------------------------------

'''

lookDictionary = {
    1:"Location 1: content coming soon",
    2:"Location 2: content coming soon",
    3:"A single clay hut can be seen in the distance",
    4:"Location 4: content coming soon",
    5:"Location 5: content coming soon",
    6:"Location 6: content coming soon",
    7:"An open expanse extends that way",
    8:"You see the crossroads where you started",
    9:"You see smoke rising in the distance",
    10:"Location 10: content coming soon",
    11:"Location 11: content coming soon",
    12:"Location 12: content coming soon",
    13:"A chasm appears to prevent your movement. Perhaps if you had some rope you could cross?",
    14:"Location 14: content coming soon",
    15:"Location 15: content coming soon",
    16:"Location 16: content coming soon",
    17:"Location 17: content coming soon",
    18:"Location 18: content coming soon",
    19:"Location 19: content coming soon",
    20:"Location 20: content coming soon",
    21:"Location 21: content coming soon",
    22:"Location 22: content coming soon",
    23:"Location 23: content coming soon",
    24:"Location 24: content coming soon",
    25:"Location 25: content coming soon"
}

pickUpableItems = {
    1:"",
    2:"",
    3:["rope"],
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"",
    10:"",
    11:"",
    12:"",
    13:"",
    14:"",
    15:"",
    16:"",
    17:"",
    18:"",
    19:"",
    20:"",
    21:"",
    22:"",
    23:"",
    24:"",
    25:""    
}

requiredItems = {
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"",
    10:"",
    11:"",
    12:"",
    13:["rope"],
    14:"",
    15:"",
    16:"",
    17:"",
    18:"",
    19:"",
    20:"",
    21:"",
    22:"",
    23:"",
    24:"",
    25:""    
}

walkDictionary = {
    1:"You are in location 1: content coming soon",
    2:"You are in location 2: content coming soon",
    3:"As you walk closer to the hut, you see a young child sleeping inside. A rope is coiled in the corner.",
    4:"You are in location 4: content coming soon",
    5:"You are in location 5: content coming soon",
    6:"You are in location 6: content coming soon",
    7:"As you start to walk, you feel the sun beat down on you. Nothing of interest is around you.",
    8:"You are at a crossroads",
    9:"You approach a small bonfire, you cannot find who or what lit this fire.",
    10:"You are in location 10: content coming soon",
    11:"You are in location 11: content coming soon",
    12:"You are in location 12: content coming soon",
    13:"You fling your rope across the chasm. It thankfully gets stuck on a rock and you shimmy slowly across. Congrats, that is as far as this current adventure goes. Stay tuned for future updates",
    14:"You are in location 14: content coming soon",
    15:"You are in location 15: content coming soon",
    16:"You are in location 16: content coming soon",
    17:"You are in location 17: content coming soon",
    18:"You are in location 18: content coming soon",
    19:"You are in location 19: content coming soon",
    20:"You are in location 20: content coming soon",
    21:"You are in location 21: content coming soon",
    22:"You are in location 22: content coming soon",
    23:"You are in location 23: content coming soon",
    24:"You are in location 24: content coming soon",
    25:"You are in location 25: content coming soon"
}

endgameLocation = [13]

def lookDirection(currentLocation,direction):
    lookingAt = relativeDirection(currentLocation,direction)
    if lookingAt > 0:
        return(lookDictionary[lookingAt])
    else:
        return("The world ends over that way. Nothing to see")

def walkDirection(currentLocation,direction,inventory):         #if you get the same location sent back, that represents that you cannot move that way without a required item
    walkingTo = relativeDirection(currentLocation,direction)
    if walkingTo > 0:
        if requiredItems[walkingTo] != "":                      #if the location you are moving to has a requirement
            for x in requiredItems[walkingTo]:                  #check all the requirements of the location
                if x not in inventory:                          #if you do not have any of the requirements, do not let them move
                    return(currentLocation)
        newLocation = walkingTo
        return(newLocation)
    else:
        return(-1)

def relativeDirection(currentLocation,direction):               #check if from the current spot, if the new square to look at is off the edge of the map or not. If it is an impossible movement, return -1. If it is valid return the relative location
    if direction == "north" and currentLocation <= 5:
        return(-1)
    elif direction == "east" and currentLocation % 5 == 0:
        return(-1)
    elif direction == "south" and currentLocation >= 21:
        return(-1)
    elif direction == "west" and currentLocation % 5 == 1:
        return(-1)
    else:
        return(newLocation(currentLocation,direction))

def newLocation(currentLocation,direction):
    if direction == "north":
        newLocation = currentLocation - 5
    elif direction == "east":
        newLocation = currentLocation + 1
    elif direction == "south":
        newLocation = currentLocation + 5
    elif direction == "west":
        newLocation = currentLocation - 1
    else:
        newLocation = -1
    return(newLocation) 

def main():
    currentLocation = 8
    playerInventory = []
    gameStatus = "running"
    print("Welcome to Adventures in the wasteland. \nAvailable commands are 'walk [north, south, east, west]', look [north, south, east, west], pickup [item name]")
    while gameStatus == "running":
        print(walkDictionary[currentLocation])
        playerInput = input().split(" ")
        playerCommand = playerInput[0]
        if playerCommand == "look":
            print(lookDirection(currentLocation, playerInput[1]))
        elif playerCommand == "walk":
            newLocation = walkDirection(currentLocation, playerInput[1], playerInventory)
            if newLocation > 0:
                if newLocation == currentLocation:
                    print("You do not have the required items to move onwards")
                currentLocation = newLocation
            else:
                print("The world ends that way. I am not going that way")
        elif playerCommand == "pickup":
            if playerInput[1] in pickUpableItems[currentLocation] and playerInput[1] not in playerInventory:
                playerInventory.append(playerInput[1])
                print("here is what is in your inventory:", playerInventory)
                print("picked up {}".format(playerInput[1]))
            elif playerInput[1] in playerInventory:
                print("You already picked that up")
            else:
                print("Could not find {}".format(playerInput[1]))
        if currentLocation in endgameLocation:
            print(walkDictionary[currentLocation])
            gameStatus = "winner"








#----------------Basic tests below--------------------------#
# print("going illegally North from position 5. Expecting -1 as an answer")
# x = relativeDirection(5, "north")
# print(x)

# print("going illegally East from position 15. Expecting -1 as an answer")
# x = relativeDirection(15, "east")
# print(x)

# print("going illegally South from position 22. Expecting -1 as an answer")
# x = relativeDirection(22, "south")
# print(x)

# print("going illegally West from position 16. Expecting -1 as an answer")
# x = relativeDirection(16, "west")
# print(x)


# print("going legally North from position 10. Expecting 5 as an answer")
# x = relativeDirection(10, "north")
# print(x)

# print("going legally East from position 13. Expecting 14 as an answer")
# x = relativeDirection(13, "east")
# print(x)

# print("going legally South from position 17. Expecting 22 as an answer")
# x = relativeDirection(17, "south")
# print(x)

# print("going legally West from position 2. Expecting 1 as an answer")
# x = relativeDirection(2, "west")
# print(x)


main()
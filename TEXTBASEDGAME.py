import random
import keyboard
import sys, os # Used to check operating system and clear the shell

# Prints out an array line by line
def printMap(j, MAP):
	for i in MAP:
		print(MAP[j][0])
		j = j + 1


def waitForKey():
	keyboard.wait('esc')	
	

# Clears Screen (should work on Windows and OSX)
def clearScreen(operatingSystem):
	if operatingSystem == 'darwin':
		os.system('clear')
	elif operatingSystem == 'win32':
		os.system('cls')


# Will save the game
def saveGame():
	return 0


OS = sys.platform
playing = False
num = 0
mapOne = [["############"], ["#          #"], ["#          #"], ["#     @    #"], ["#          #"], ["#          #"], ["#          #"], ["############"]]
choice = ""

# what we plan to do:

# player = @ symbol
# walls are #
# you can't hit the walls
# secret rooms (sorcerers cave sytle) you can't see the rooms until you move into them
# ? = key - you won't see the door until you pick up the key
# the keys are colour coded for certain doors and the key might ot correspond to the door of the room you are in 

print("\nText based adventure")
print("\nWelcome to this adventure!\n\t1)Start a new game")
choice = int(input("\nEnter a number: "))
if choice == 1:
	playing = True
else:
	print("ERROR - Invalid input")


while playing == True:
	clearScreen(OS)

	print("\nText based adventure\n")
	printMap(num, mapOne)

	waitForKey()		

	playing = False


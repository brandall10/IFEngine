from game import *
from room import *
from player import * 
from map import *

end = False

def main():
	map = Map()
	startRoom = map.Build()
	adventurer=Player(name="Adventurer", currentRoom=startRoom)
	game = Game(name="Treasure Troll", player=adventurer)

if __name__ == "__main__":
	main()	

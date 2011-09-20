from person import *
from room import *
from item import *

class Map(object):

	def Build(self):
		house = Room(name="House", description="You're in the first floor of an old house")
		backyard = Room(name="Backyard", description="You're in the backyard of the house.")	
		shed = Room(name="Shed", description="You're in the shed")
		attic = Room(name="Shed", description="You're in the attic of the house")

		# above ground map
		house.set_exits(north=backyard, east=shed, up=attic)
		shed.set_exits(west=house)
		backyard.set_exits(south=house)
		attic.set_exits(down=house)

		toolchest = ContainerItem("toolchest", "A rusty old toolchest.", shed)
		lamp = Item("lamp", "A shiny lamp.", toolchest)
		matches = Item("matches", "A book of matches.", toolchest)
		sword = Weapon("sword", "A killer sword.", attic)

		# dungeon map
		cellar = Room(name="Cellar", description="You're in cellar under the house.")
		trollLair1 = Room(name="Lair", description="You're in the lair of a nasty troll.")
		trollLair2 = Room(name="Lair", description="You're in the lair of a nasty troll.")
		trollLair3 = Room(name="Lair", description="You're in the lair of a nasty troll.")
		trollLair4 = Room(name="Lair", description="You're in the lair of a nasty troll.")
		
		cellar.set_exits(north=trollLair1, up=house)
		house.set_exits(down=cellar)
		trollLair1.set_exits(south=cellar, east=trollLair4, north=trollLair2)
		trollLair2.set_exits(south=trollLair1, east=trollLair3)
		trollLair3.set_exits(west=trollLair2, south=trollLair4)
		trollLair4.set_exits(west=trollLair1, north=trollLair3)
		
		axe = Weapon(name="axe", description="Killer odor fighter.")
		treasure = Item(name="treasure", description="Leather covered treasure 4 ur pleasure.")

		room_list = (trollLair1, trollLair2, trollLair3, trollLair4)
		troll = Person("troll", "A nasty troll is here looking at you like dinner.", trollLair2, rooms=room_list, items=[axe, treasure], life=10)

		return house

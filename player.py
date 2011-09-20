# player class - keeps track of player status
from item import * 
from random import choice

class Player(object):
	def __init__(self, name, currentRoom=None):
		self.name = name
		self.currentRoom = currentRoom
		self.life = 10
		self.items = [] 

	def look(self, item=None):
		if not item:
			print self.currentRoom
			return
		for i in self.items:
			if i.name==item:
				print i
				return
		for i in self.currentRoom.items:
			if i.name==item:
				print i
				return
		
	def go(self, direction=None):
		direction = direction.lower()
		directiontxt = "self.currentRoom.exits['%s']" % direction
		try:
			if eval(directiontxt) == None:
				print "You cannot go " + direction + "."
			else:
				self.currentRoom.player = None
				self.currentRoom = eval(directiontxt)
				self.currentRoom.player = self
				print self.currentRoom
		except (AttributeError, KeyError):
			print "The direction you are going does not exist.  Try harder next time."
		
	def get(self, item):
		# special case of "all"
		if item=="all": return self.getall() 
		# proceed with getting one item
		found = self.finditem(self.currentRoom, item)
		self.takeitem(found)
	def getall(self):
		for i in list(self.currentRoom.items): 
			self.takeitem(i)
	def takeitem(self, item):
		if item: 
			item.move(self)	
			print "%s: Taken." % item.name
		else:
			print "Item not found."
	def take(self, item):
		self.get(item)

	def drop(self, item):
		found = self.finditem(self, item)
		if found: 
			found.move(self.currentRoom)
			print "%s: Dropped." % found.name
			# end game scenario
			if found.name is "treasure" and self.currentRoom.name is "Backyard":
				print "You've won!"
				exit()	
		else:
			print "Item not found."

	def attack(self, opponent, weapon):
		found_weapon = self.finditem(self, weapon)
		if not self.currentRoom.people or opponent != self.currentRoom.people.name:
			print "I do not see a \"%s\" here." % opponent
		elif not found_weapon:
			print "You don't have a \"%s\"." % weapon
		elif not isinstance(found_weapon, Weapon):
			print "%s isn't a weapon!" % weapon
		else:
			damage = choice(range(0,5))
			if not damage:
				print "You missed!"
			elif damage < 3:
				print "Minor flesh wound!"
			else:
				print "Major hit!"
			self.currentRoom.people.injured(found_weapon.strength*damage)
		
		# enemy may have been killed so need to check	
		if self.currentRoom.people:
			print self.currentRoom.people.react()

	def open(self, item):
		for i in self.items:
			if i.name == item and isinstance(i, ContainerItem):
				print i.open()
				return
		print "Can't open \"%s\"." % item
	
	def close(self, item):
		for i in self.items:
			if i.name == item and isinstance(i, ContainerItem):
				print i.close()
				return
		print "Can't close \"%s\"." % item
	
	def inventory(self):
		for i in self.items: print i.name	
	
	def quit(self):
		exit()

	# return item object from name
	def finditem(self, location, item):	
		# first try regular environment
		retval = next((i for i in location.items if i.name==item), None)
		if retval: return retval
		# nothing?  then try to drill down into personal open containers
		containers = [i for i in self.items if isinstance(i, ContainerItem) and i.isopen==True]
		for cont in containers:
			retval = next((i for i in cont.items if i.name==item), None)
			if retval:
				return retval	 
		# empty handed
		return None	
	

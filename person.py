from random import choice
from room import *

# really should take similarities w/ player class and put in base, call this one enemy.  
# Also add events so player is not coupled to this and vise versa
class Person(object):
	def __init__(self, name, description, currentRoom, rooms=None, items=None, life=1, strength=1):
		self.name = name
		self.description = description
		self.rooms = rooms
		self.items = items 
		for i in items:
			i.parent = self
		self.life = life
		self.strength = strength
		self.currentRoom = currentRoom
		self.currentRoom.people = self

	def move(self):
		# randomly select exit
		n = self.currentRoom.exits
		d = n[choice(n.keys())]  # TODO: convert to lambda expresion, simplify
		# if exit not in rooms keep searching choosing for one that is	
		while d not in self.rooms:
			d = n[choice(n.keys())]
		# move
		self.currentRoom.people = None
		self.currentRoom = d 
		self.currentRoom.people = self

		return "The %s takes a glance at you and leaves the room." % self.name

	def attack(self):
		damage = choice(range(0,5)) 
		result = None
		if not damage:
			result = "The %s attacks but misses!" % self.name
		elif damage < 3:
			result = "The %s attacks and inflicts a minor flesh wound!" % self.name
		else:
			result = "The %s attacks and inflicts major damage!" % self.name

		self.currentRoom.player.life -= damage
		if self.currentRoom.player.life <= 0:
			print "You have died. Try again"
			exit() # TODO: handle this properly in the game engine
		return result
	
	def do_nothing(self):
		return "The %s taunts you." % self.name

	def react(self):
		action = choice(("attack", "move", "do_nothing"))
		cmd = getattr(self, action)
		return cmd()	

	def injured(self, amount):
		self.life -= amount
		if self.life <= 0:
			print "The %s has been killed!" % self.name
			for i in list(self.items):
				i.move(self.currentRoom)
			self.currentRoom.people = None	
			self = None
			
	def __str__(self):
		return "%s\n%s" % (self.description, self.react())

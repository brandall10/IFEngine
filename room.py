# Base class for all rooms
from item import make_item_list

class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.exits = {}
		self.items = [] 
		self.player = None 
		self.people = None 

	def set_exits(self, north=None, east=None, west=None, south=None, up=None, down=None):
		if north: self.exits['north'] = north
		if south: self.exits['south'] = south
		if east: self.exits['east'] = east
		if west: self.exits['west'] = west
		if up: self.exits['up'] = up
		if down: self.exits['down'] = down

	def __str__(self):
		retval = self.description
		if self.people:
			retval += "\n%s" % self.people
		if len(self.items) > 0:
			for i in self.items:
				retval += "\nThere is a(n) %s here." % i.name
		if len(self.exits) > 0:
			retval += "\nThere are exit(s) to the "
			ex = list("")
			for k in self.exits:
				ex += "%s, " % k
			ex[len(ex)-2] = '.'
			retval += "".join(ex)
		return retval
	
	

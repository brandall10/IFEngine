class Item(object):
	def __init__(self, name, description, parent=None):
		self.name = name
		self.description = description
		self.parent = parent
		if self.parent:
			self.parent.items.append(self)
			
	def move(self, parent):
		self.parent.items.remove(self)
		self.parent = parent
		self.parent.items.append(self)

	def remove(self):
		self.parent.items(remove)
		self.parent = None

	def __str__(self):
		return self.description

class Weapon(Item):
	def __init__(self, name, description, parent=None, strength=1):
		Item.__init__(self, name, description, parent)
		self.strength=strength

class ContainerItem(Item):
	def __init__(self, name, description, parent):
		Item.__init__(self, name, description, parent)
		self.isopen=False
		self.items = []

	def get_state(self):
		if self.isopen==False:
			return "The %s is closed." % self.name
		if self.isopen==True and len(self.items) > 0:
			retval = "The %s is opened. It contains: " % self.name
			retval += make_item_list(self.items)
			return retval
	
	def open(self):
		self.isopen=True
		return self.get_state()

	def close(self):
		self.isopen=False
		return self.get_state()
		
	def __str__(self):
		return "%s %s" % (self.description, self.get_state())

def make_item_list(items):
	if len(items)==0:
		return ""
	ex = list("")
	for i in items:
		ex += i.name + ", "
	ex[len(ex)-2] = '.'
	return "".join(ex)



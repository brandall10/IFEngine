# game - wiring it all up

end = False

class Game(object):
	def __init__(self, name, player):
		self.name = name
		self.player = player
		print "Welcome to "+self.name
		print player.currentRoom
		while end == False:
			cmd = raw_input("> ")
			self.process(cmd)

	def process(self, cmd):
		global end
		cmdlist = cmd.split()
		try:
			if len(cmdlist) == 1:
				cmd = getattr(self.player, cmdlist[0])
				cmd()
			elif len(cmdlist) == 2:
				cmd = getattr(self.player, cmdlist[0])
				cmd(cmdlist[1])
			elif len(cmdlist) == 4:
				cmd = getattr(self.player, cmdlist[0])
				cmd(cmdlist[1], cmdlist[3])
			else:
				print "I don't understand \"%s\"." % cmd
		except AttributeError:
			print "I don't understand \"%s\"." % cmd

		except TypeError:
			print "%s ...?" % cmdlist[0]

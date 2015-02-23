import pickle
import vars
import store
import story
import fight
import sys
def newgame(): ## process for creating a new game
	vars.stats
	name = raw_input("What's your name, glorious initiate? ")
	vars.stats['name'] = name
	vars.stats['room'] = """
	%s's room:""" % (name)
	print "Welcome %s!. Your Xbox Live subscription has expired and you are looking for a new way to play games. Will you take the path to enlightenment, or will you continue with your peasantry?" % (vars.stats['name'])
	story.story(vars.stats['room'], vars.background)
def mainmenu(): ##game load
	vars.stats
	while 1 == 1:
		path = raw_input("Would you like to start a (n)ew game or (l)oad a saved one? ")
		if path == 'n':
			newgame()
		elif path == 'l':
			loadfile()
def gamemenu(): ## main menu once in game
	vars.stats
	while 1 == 1:
		choice = raw_input("Choices: (s)ave, (q)uit, (n)ext quest, (m)icrocenter (p)layer info, (i)nventory, (f)ight a random enemy: ")
		if choice == "s":
			with open('pcmrpgsave.txt', 'wb') as handle:
				pickle.dump(vars.stats, handle)
		elif choice == "q":
			sys.exit()
		elif choice == "n":
			story.newquest()
		elif choice == "m":
			store.microcenter(vars.stats['quest'], vars.stats['items'])
		elif choice == "p":
			for stat, item in vars.stats.items():
				print "%r is %r" % (stat, item)
		elif choice == "i":
			inventory()
		elif choice == "f":
			fight.genfight(blank)
def loadfile(): ## for loading the pickle dump- must be saved as pcmrpgsave.txt in same folder
	vars.stats
	with open('pcmrpgsave.txt', 'rb') as handle:
		vars.stats = pickle.loads(handle.read())
	print "Welcome back %s!" % (vars.stats['name'])
	gamemenu()
def gameover(): ##deletes save and quits
	f = open('pcmrpgsave.txt', 'r+')
	f.truncate()
	sys.exit()
def inventory(): ## inventory list
	vars.stats
	for object in vars.stats['items']:
		print object
	print "You have %d gold" % (vars.stats['monies'])
	print "You have %d health out of %d max" % (vars.stats['health'], vars.stats['maxhealth'])
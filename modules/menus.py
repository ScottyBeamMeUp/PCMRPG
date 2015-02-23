import pickle
from vars import *
from fight import *
from store import *
from story import *
def newgame(): ## process for creating a new game
	global stats
	name = raw_input("What's your name, glorious initiate? ")
	stats['name'] = name
	stats['room'] = """
	%s's room:""" % (name)
	print "Welcome %s!. Your Xbox Live subscription has expired and you are looking for a new way to play games. Will you take the path to enlightenment, or will you continue with your peasantry?" % (stats['name'])
	story(stats['room'], background)
def mainmenu(): ##game load
	global stats
	while 1 == 1:
		path = raw_input("Would you like to start a (n)ew game or (l)oad a saved one? ")
		if path == 'n':
			newgame()
		elif path == 'l':
			loadfile()
def gamemenu(): ## main menu once in game
	global stats
	while 1 == 1:
		choice = raw_input("Choices: (s)ave, (q)uit, (n)ext quest, (m)icrocenter (p)layer info, (i)nventory, (f)ight a random enemy: ")
		if choice == "s":
			with open('pcmrpgsave.txt', 'wb') as handle:
				pickle.dump(stats, handle)
		elif choice == "q":
			sys.exit()
		elif choice == "n":
			newquest()
		elif choice == "m":
			microcenter(stats['quest'], stats['items'])
		elif choice == "p":
			for stat, item in stats.items():
				print "%r is %r" % (stat, item)
		elif choice == "i":
			inventory()
		elif choice == "f":
			genfight()
def loadfile(): ## for loading the pickle dump- must be saved as pcmrpgsave.txt in same folder
	global stats
	with open('pcmrpgsave.txt', 'rb') as handle:
		stats = pickle.loads(handle.read())
	print "Welcome back %s!" % (stats['name'])
	gamemenu()
def gameover(): ##deletes save and quits
	f = open('pcmrpgsave.txt', 'r+')
	f.truncate()
	sys.exit()
def inventory(): ## inventory list
	global stats
	for object in stats['items']:
		print object
	print "You have %d gold" % (stats['monies'])
	print "You have %d health out of %d max" % (stats['health'], stats['maxhealth'])
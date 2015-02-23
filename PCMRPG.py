import sys
import pickle
import random
## variables -- define numbers and story blocks
enemylist = ["Console Peasant", "IGN Reviewer", "Exclusive Developer", "MegaPublisher", "Microsoft Employee", "Sony Employee",]
stats = {'health' : 100, 'maxhealth' : 100, 'damage' : 5, 'armor' : 0, 'quest' : 0, 'status' : "peasant", "items" : ["Macbook Air", "Xbox 360"], 'monies': 0}
blank = ''
flashpeasant = {'name': "Console Peasant", 'health' : 20, 'maxhealth' : 20, 'damage' : 5, 'armor' : 0, 'monies' : 100} ## for first fight-pregenerated so you can't lose
background = """
You feel a light shining down all around you.
Your PC gamer friend mentioned that this might occur when researching your next purchase
An apparition of GabeN appears next to you.
He says "It is your time now. Fight off the evil console peasantry so you can ascend into the world of the PC Gamers!"
"""
start = """
You log on to your MacBook Air. There's a note. It says to visit /r/pcmasterrace. You make your first post. Does 
it say "(H)ow do I get started?" or "(P)Cs SUCK CONSOLE MASTERRACE"""""
start2 = '''
The reply reads, "You start by vanquishing the peasant within. I know this sounds cheesy, but you can do this by destroying other peasants. Go to MicroCenter to buy your first part. 
+/u/goldtip 100'''
start3 = '''
You get downvoted into oblivion.
You are told to go back to the console shill subreddits.
However, one poster, who was downvoted as well, says:
"I believe in you. You can ascend, but you need gold. Go kill some console peasants in a flash game.'''
storefront2 = """
		__________________________________________
		|AMD Radeon R9 (260X)	|nVidia GTX (750)| 
		|100 G                  |100 G           |
		|+10 Damage             |+5 Damage       |
		|-10 Max Health         |+5 Armor        |
		------------------------------------------
		To heal yourself, type repair.
		"""
## definitions -- code goes here
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
def story(location, quest): ## for printing story elements, and upping quest var
	global stats
	print """
	%s
	%s
	""" % (location, quest)
	if stats['quest'] == 0:
		stats['quest'] += 1 ## quest var controls place in story and difficulty
		gamemenu()
	elif stats['quest'] == 1:
		choice2 = raw_input()
		if choice2 == 'H':
			stats['quest'] += .1
			story(blank, start2)
		elif choice2 == 'P':
			stats['quest'] += .2
			story(blank, start3)
	elif stats['quest'] == 1.1:
		stats['quest'] += .9
		stats['monies'] += 100
		
	elif stats['quest'] == 1.2:
		initfight(flashpeasant)
		stats['quest'] += 0.8
		gamemenu()
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
def newquest(): ## determines which story block to pass
    global stats
    if stats['quest'] == 1:
        story(stats['room'], start)
def loadfile(): ## for loading the pickle dump- must be saved as pcmrpgsave.txt in same folder
	global stats
	with open('pcmrpgsave.txt', 'rb') as handle:
		stats = pickle.loads(handle.read())
	print "Welcome back %s!" % (stats['name'])
	gamemenu()
def microcenter(quest, inventory): ##shows store and passes to the store processor
	global stats
	print "Welcome to MicroCenter! We have all you need for PC building and peasant slaying!"
	if quest>= 0 and quest<=2:
		print storefront2
		storeitem = raw_input("Please choose an item: ")
		storereq(2, storeitem)
def storereq(storeinstance, storeitem): ## processes store requests
	global stats
	if storeinstance == 2:
		if storeitem == "repair":
			restorecost = (stats['maxhealth'] - stats['health']) * 1.5
			print "A restore to full health will be %r gold." % (restorecost)
			repairchoice = raw_input("Y/N: ")
			if repairchoice == "Y" and stats['monies'] - restorecost >= 0:
				stats['monies'] = stats['monies'] - restorecost
				gamemenu()
			elif stats['monies'] - restorecost < 0:
				print "Not enough gold."
				gamemenu()
			elif repairchoice == "N":
				gamemenu()
			else:
				print "Invalid Choice"
				gamemenu()
		elif storeitem == "260X" and stats['monies'] - 100 >= 0 and "AMD R9 260X" not in stats['items']:
			stats['damage'] += 10
			stats['maxhealth'] = stats['maxhealth'] - 10
			stats['monies'] = stats['monies'] - 100
			stats['items'].append("AMD R9 260X")
			if stats['health'] > stats['maxhealth']:
				stats['health'] = stats['maxhealth']
		elif "AMD R9 260X" in stats['items']:
			print("You already have this item")
		elif storeitem == "750" and stats['monies'] - 100 >= 0 and "nVidia GTX 750" not in stats['items']:
			stats['damage'] += 5
			stats['armor'] += 5
			stats['monies'] = stats['monies'] - 100
			stats['items'].append("nVidia GTX 750")
		elif "nVidia GTX 750" in stats['items']:
			print("You already have this item")
		elif storeitem != "750" and storeitem != "260X":
			print("You didn't choose an item!")
			gamemenu()
		elif stats['monies'] - 100 < 0:
			print("Not enough gold!")
			gamemenu()
		else:
			print("That's not a choice!")
			gamemenu()
def initfight(enemy): ##fight engine
	global stats
	print "A wild %s appeared!" % (enemy['name'])
	while enemy["health"] > 0 and stats["health"] > 0:
		print "Enemy Health Remaining: %d" % (enemy["health"])
		print "%s's Health Remaining: %d" % (stats["name"], stats['health'])
		attack = raw_input("Would you like to (a)ttack, (v)iew inventory, or (r)un: ")
		if attack == "a":
			enemy["health"] = enemy["health"] - stats["damage"] + enemy['armor']
			stats["health"] = stats["health"] - enemy["damage"] + stats['armor']
		if attack == "v":
			inventory()
		if attack == "r":
			randint = random.randint(1,100)
			if stats['quest'] == 1.2:
				print "You can't run from the first fight!"
			elif randint >= 75:
				gamemenu()
			elif randint >=50:
				stats['monies'] = stats['monies'] / 2
				print "In a panic, you lost half of your gold."
				gamemenu()
			else:
				print "You failed to run away"
				stats["health"] = stats["health"] - enemy["damage"]
	if enemy["health"] <= 0:
		stats['monies'] += enemy['monies']
		print "You won! You gained %d gold." % (enemy['monies'])
		if stats['quest'] == 1.2:
			stats['quest'] += .8
		gamemenu()
	elif stats['health'] <= 0:
		print "You Died"
		gameover()
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
def genfight(): ## enemy generation
	global stats
	randomenemy = {'name' : None, 'health' : None, 'maxhealth' : None, "armor": None, "damage" : None, "monies" : None}
	randint = random.randint(1,100)
	if randint < 50:
		randomenemy['name'] = enemylist[0]
		dmgscale = 1
		healthscale = 1
		armorscale = 0
		goldscale = 1
	elif randint < 68:
		randomenemy['name'] =  enemylist[1]
		dmgscale = 2
		healthscale = 2
		armorscale = 0
		goldscale = 2
	elif randint < 78:
		randomenemy['name'] = enemylist[2]
		dmgscale = 3
		healthscale = 3
		armorscale = 1
		goldscale = 3
	elif randint < 85:
		randomenemy['name'] = enemylist[3]
		dmgscale = 4
		healthscale = 4
		armorscale = 1
		goldscale = 4
	elif randint < 93:
		randomenemy['name'] = enemylist[4]
		dmgscale = 5
		healthscale = 5
		armorscale = 2
		goldscale = 5
	elif randint < 100:
		randomenemy['name'] = enemylist[5]
		dmgscale = 6
		healthscale = 6
		armorscale = 3
		goldscale = 6
	dmgint = random.randint(3,5)
	randomenemy['damage'] = dmgint + dmgscale * stats['quest']
	healthint = random.randint(2,4)
	randomenemy['health'] = healthint + healthscale * stats['quest']
	armorint = random.randint(1,3)
	randomenemy['armor'] = armorint + armorscale + stats['quest']
	goldint = random.randint(2,3)
	randomenemy['monies'] = goldint * goldscale * stats['quest']
	randomenemy['maxhealth'] = randomenemy['health']
	initfight(randomenemy)
## exec--hold my mouse I'm going in!
mainmenu()
## quest 0 is game start
## quest 1 is reddit post
## quest 1.1 is positive post
## quest 1.2 is negative post
## quest 2 is pending
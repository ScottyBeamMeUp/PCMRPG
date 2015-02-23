from vars import *
from menus import *
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
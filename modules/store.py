import vars
import menus
def microcenter(quest, inventory): ##shows store and passes to the store processor
	vars.stats
	print "Welcome to MicroCenter! We have all you need for PC building and peasant slaying!"
	if vars.stats['quest']>= 0 and vars.stats['quest']<=2:
		print vars.storefront2
		storeitem = raw_input("Please choose an item: ")
		storereq(2, storeitem)
def storereq(storeinstance, storeitem): ## processes store requests
	vars.stats
	if storeinstance == 2:
		if storeitem == "repair":
			restorecost = (vars.stats['maxhealth'] - vars.stats['health']) * 1.5
			print "A restore to full health will be %r gold." % (restorecost)
			repairchoice = raw_input("Y/N: ")
			if repairchoice == "Y" and vars.stats['monies'] - restorecost >= 0:
				vars.stats['monies'] = vars.stats['monies'] - restorecost
				menus.gamemenu()
			elif vars.stats['monies'] - restorecost < 0:
				print "Not enough gold."
				menus.gamemenu()
			elif repairchoice == "N":
				menus.gamemenu()
			else:
				print "Invalid Choice"
				menus.gamemenu()
		elif storeitem == "260X" and vars.stats['monies'] - 100 >= 0 and "AMD R9 260X" not in vars.stats['items']:
			vars.stats['damage'] += 10
			vars.stats['maxhealth'] = vars.stats['maxhealth'] - 10
			vars.stats['monies'] = vars.stats['monies'] - 100
			vars.stats['items'].append("AMD R9 260X")
			if vars.stats['health'] > vars.stats['maxhealth']:
				vars.stats['health'] = vars.stats['maxhealth']
		elif "AMD R9 260X" in vars.stats['items']:
			print("You already have this item")
		elif storeitem == "750" and vars.stats['monies'] - 100 >= 0 and "nVidia GTX 750" not in vars.stats['items']:
			vars.stats['damage'] += 5
			vars.stats['armor'] += 5
			vars.stats['monies'] = vars.stats['monies'] - 100
			vars.stats['items'].append("nVidia GTX 750")
		elif "nVidia GTX 750" in vars.stats['items']:
			print("You already have this item")
		elif storeitem != "750" and storeitem != "260X":
			print("You didn't choose an item!")
			menus.gamemenu()
		elif vars.stats['monies'] - 100 < 0:
			print("Not enough gold!")
			menus.gamemenu()
		else:
			print("That's not a choice!")
			menus.gamemenu()
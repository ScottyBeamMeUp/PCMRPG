import vars
import menus
import random
def initfight(enemy): ##fight engine
	print "A wild %s appeared!" % (enemy['name'])
	while enemy["health"] > 0 and vars.stats["health"] > 0:
		print "Enemy Health Remaining: %d" % (enemy["health"])
		print "Enemy Armor Remaining: %d" % (enemy["armor"])
		print "%s's Health Remaining: %d" % (vars.stats["name"], vars.stats['health'])
		print "%s's Armor Remaining: %d" % (vars.stats["name"], vars.stats['health'])
		attack = raw_input("Would you like to (a)ttack, use thermal (p)aste, (v)iew inventory, or (r)un: ")
		if attack == "a":
			enemy["health"] = enemy["health"] - vars.stats["damage"] + enemy['armor']
			if enemy['armor'] - 1 >= 0:
				enemy["armor"] = enemy['armor'] - 1
			vars.stats["health"] = vars.stats["health"] - enemy["damage"] + vars.stats['armor']
			if vars.stats["armor"] -1 >= 0:
				vars.stats["armor"] = vars.stats["armor"] -1
		if attack == "v":
			menus.inventory()
		if attack == "r":
			randint = random.randint(1,100)
			if vars.randomyes == 0:
				print "You can't run from a non-random encounter!"
			elif randint >= 75:
				vars.randomyes = 0
				menus.gamemenu()
			elif randint >=50:
				vars.randomyes = 0
				vars.stats['monies'] = vars.stats['monies'] / 2
				print "In a panic, you lost half of your gold."
				menus.gamemenu()
			else:
				print "You failed to run away"
				vars.stats["health"] = vars.stats["health"] - enemy["damage"]
		if attack == "p":
			if vars.stats['paste'] >= 1:
				vars.stats['health'] += 10
				vars.stats['paste'] = vars.stats['paste'] - 1
			else:
				print "You don't have any paste!"
	if enemy["health"] <= 0:
		vars.randomyes = 0
		vars.stats['monies'] += enemy['monies']
		print "You won! You gained %d gold." % (enemy['monies'])
		if vars.stats['quest'] == 1.2:
			vars.stats['quest'] += .8
	elif vars.stats['health'] <= 0:
		print "You Died"
		menus.gameover()
def genfight(choice): ## enemy generation
	randomenemy = {'name' : None, 'health' : None, 'maxhealth' : None, "armor": None, "damage" : None, "monies" : None}
	if choice == "0":
		randomenemy['name'] = vars.enemylist[0]
	elif choice == "1":
		randomenemy['name'] = vars.enemylist[1]
	elif choice == "2":
		randomenemy['name'] = vars.enemylist[2]
	elif choice == "3":
		randomenemy['name'] = vars.enemylist[3]
	elif choice == "4":
		randomenemy['name'] = vars.enemylist[4]
	elif choice == "5":
		randomenemy['name'] = vars.enemylist[5]
	else:
		randint = random.randint(1,100)
		if randint < 50:
			randomenemy['name'] = vars.enemylist[0]
		elif randint < 68:
			randomenemy['name'] =  vars.enemylist[1]
		elif randint < 78:
			randomenemy['name'] = vars.enemylist[2]
		elif randint < 85:
			randomenemy['name'] = vars.enemylist[3]
		elif randint < 93:
			randomenemy['name'] = vars.enemylist[4]
		elif randint < 100:
			randomenemy['name'] = vars.enemylist[5]
		vars.randomyes = 1
	if randomenemy['name'] == vars.enemylist[0]:
		dmgscale = 1
		healthscale = 1
		armorscale = 0
		goldscale = 1
	elif randomenemy['name'] == vars.enemylist[1]:
		dmgscale = 2
		healthscale = 2
		armorscale = 0
		goldscale = 2
	elif randomenemy['name'] == vars.enemylist[2]:
		dmgscale = 3
		healthscale = 3
		armorscale = 1
		goldscale = 3
	elif randomenemy['name'] == vars.enemylist[3]:
		dmgscale = 4
		healthscale = 4
		armorscale = 1
		goldscale = 4
	elif randomenemy['name'] == vars.enemylist[4]:
		dmgscale = 5
		healthscale = 5
		armorscale = 2
		goldscale = 5
	elif randomenemy['name'] == vars.enemylist[5]:
		dmgscale = 6
		healthscale = 6
		armorscale = 3
		goldscale = 6
	dmgint = random.randint(3,5)
	randomenemy['damage'] = dmgint * (dmgscale + vars.stats['quest'])
	healthint = random.randint(3,5)
	randomenemy['health'] = healthint * (healthscale + vars.stats['quest'])
	armorint = random.randint(1,3)
	randomenemy['armor'] = armorint + armorscale + vars.stats['quest']
	goldint = random.randint(2,3)
	randomenemy['monies'] = goldint * goldscale * vars.stats['quest'] * 2
	randomenemy['maxhealth'] = randomenemy['health']
	initfight(randomenemy)
from vars import *
import random
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
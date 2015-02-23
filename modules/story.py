from vars import *
from menus import *
from fight import *
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
def newquest(): ## determines which story block to pass
    global stats
    if stats['quest'] == 1:
        story(stats['room'], start)
import menus
import fight
import vars
def story(location, quest): ## for printing story elements, and upping quest var
	vars.stats
	print """
	%s
	%s
	""" % (location, quest)
	if vars.stats['quest'] == 0:
		vars.stats['quest'] += 1 ## quest var controls place in story and difficulty
		menus.gamemenu()
	elif vars.stats['quest'] == 1:
		choice2 = raw_input()
		if choice2 == 'H':
			vars.stats['quest'] += .1
			story(vars.blank, vars.start2)
		elif choice2 == 'P':
			vars.stats['quest'] += .2
			story(vars.blank, vars.start3)
	elif vars.stats['quest'] == 1.1:
		vars.stats['quest'] += .9
		vars.stats['monies'] += 100
		
	elif vars.stats['quest'] == 1.2:
		fight.initfight(vars.flashpeasant)
		vars.stats['quest'] += 0.8
		menus.gamemenu()
def newquest(): ## determines which story block to pass
    vars.stats
    if vars.stats['quest'] == 1:
        story(vars.stats['room'], vars.start)
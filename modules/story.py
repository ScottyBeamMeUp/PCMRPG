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
	elif vars.stats['quest'] == 2:
		for g in range(1,4):
			fight.genfight(vars.consolepeasant)
		vars.stats['quest'] += 1
		
		
def newquest(): ## determines which story block to pass
    vars.stats
    if vars.stats['quest'] == 1:
        story(vars.stats['room'], vars.start)
    elif vars.stats['quest'] == 2.0 and "AMD R9 260X" or "nVidia GTX 750" in vars.stats['items']:
    	story(vars.stats['room'], vars.youtubemission)
    elif vars.stats['quest'] == 2.0 and "AMD R9 260X" or "nVidia GTX 750" not in vars.stats['items']:
    	print "You should go buy a graphics card first!"
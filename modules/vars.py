## variables -- define numbers and story blocks
enemylist = ["Console Peasant", "IGN Reviewer", "Exclusive Developer", "MegaPublisher", "Microsoft Employee", "Sony Employee",]
stats = {'health' : 100, 'maxhealth' : 100, 'damage' : 5, 'armor' : 0, 'quest' : 0, 'status' : "peasant", "items" : ["Macbook Air", "Xbox 360"], 'monies': 0, "paste" : 0}
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
consolepeasant = "0"
ignreviewer = "1"
dev = "2"
megapublisher = "3"
MSEmployee = "4"
SonyEmployee = "5"
youtubemission = '''
You go online to watch your favorite youtube videos.
When you see the comments, a special rage fills your body.
You feel the need to bring justice to the peasants.'''
free = 0
randomyes = 0
storefront3 = """
		____________________________________________________________________
		|Thermal (P)aste |(C)ase          |Intel Core (i)3 |(A)MD FX 6300  |
		|Consumable 10 G |Armor Boost 20 G|150 G           |125 G          |
		|Restore 10      |+ 4 Armor       |+ 20 Damage     |+ 25 Damage    |
		|health in battle|                |+ 10 Max Health |- 5 Max Health |
		-------------------------------------------------------------------
		To heal yourself, type repair. You get one free repair before your next quest.
		"""
storefront3nonfree = """
		____________________________________________________________________
		|Thermal (P)aste |(C)ase          |Intel Core (i)3 |(A)MD FX 6300  |
		|Consumable 10 G |Armor Boost 20 G|150 G           |125 G          |
		|Restore 10      |+ 4 Armor       |+ 20 Damage     |+ 25 Damage    |
		|health in battle|                |+ 10 Max Health |- 5 Max Health |
		-------------------------------------------------------------------
		To heal yourself, type repair.
		"""
afteryoutube = """
The maker of the video thanks you and recommends that you buy yourself a CPU.
"""
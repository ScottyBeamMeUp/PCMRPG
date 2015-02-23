import os
import modules.menus
cwd = os.getcwd
if os.path.exists('modules/fight.py') and os.path.exists('modules/store.py') and os.path.exists('modules/menus.py') and os.path.exists('modules/story.py') and os.path.exists('modules/vars.py'):
	modules.menus.mainmenu()
else:
	raise Exception(MissingFile)
## exec--hold my mouse I'm going in!

## quest 0 is game start
## quest 1 is reddit post
## quest 1.1 is positive post
## quest 1.2 is negative post
## quest 2 is pending
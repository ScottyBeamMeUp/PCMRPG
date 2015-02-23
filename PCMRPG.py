import os
## check for all modules and then exec
if os.path.exists("__init__.py") and os.path.exists("modules/__init__.py") and os.path.exists('modules/fight.py') and os.path.exists('modules/store.py') and os.path.exists('modules/menus.py') and os.path.exists('modules/story.py') and os.path.exists('modules/vars.py'):
	import modules.menus
	modules.menus.mainmenu()
else:
	raise Exception(MissingFile)

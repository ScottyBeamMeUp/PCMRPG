#!/bin/bash
if which pyinstaller >/dev/null; then
  pyinstaller --onefile PCMRPG.py
  cp dist/PCMRPG PCMRPGshell.app/Contents/Resources/Scripts/
else
  echo Pyinstaller is not installed. Please install it.
fi

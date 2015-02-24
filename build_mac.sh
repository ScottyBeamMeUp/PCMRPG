#!/bin/bash
if which pyinstaller >/dev/null; then
  pyinstaller --onefile PCMRPG.py
  cp dist/PCMRPG PCMRPGshell.app/Contents/Resources/Scripts/
else
  echo pyinstaller is not installed. Please install it.
  while true; do
    read -p "Do you wish to resolve dependencies?" yn
    case $yn in
        [Yy]* ) dependency; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
fi
dependency ()
{
  if which pip >/dev/null; then
    echo Installing pip
    curl -0 https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
  fi
  echo Installing pyinstaller
  pip install pyinstaller
}

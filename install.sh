#!/bin/bash

dialog --title 'Lyrixal installer' --msgbox "Welcome to \nLyrixal Telegram Bot installer." 8 45
py3ver=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
if [[ $py3ver == 3\.4* ]]; then
  dialog --title 'Lyrixal installer' --colors --msgbox "Installed Python3 version: \n\Zb$py3ver\Zn\n\n\Z2Running compatibale Python version!\Zn" 8 45
  if [[ $(pip --version) == pip* ]]; then
	sudo pip instal requirements
	dialog --title 'Lyrixal installer' --inputbox "Copy your bot token from @BotFather:" 8 45 2> key.txt
	dialog --title 'Lyrixal installer' --colors --msgbox "\Z2Install and config COMPLETE! \Zn" 8 45
  else
	dialog --title 'Lyrixal installer' --colors --msgbox "'pip' is not installed\n\n\Z1Install failed. \Zn" 8 45
  fi
else
	dialog --title 'Lyrixal installer' --colors --msgbox "Installed Python3 version: \n\Zb$py3ver\Zn\n\n\Z1Running incompatibale Python version!\Zn" 8 45
	dialog --title 'Lyrixal installer' --colors --msgbox "\Z1Install failed. \Zn" 8 45
fi

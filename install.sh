#!/bin/bash
ansi_reset="\033[0m"
ansi_bold="\033[1m"
ansi_backgreen="\033[42m"
ansi_backred="\033[41m"
ansi_invert="\e[7m"
ansi_underline="\e[4m"
ansi_red="\e[91m"
ansi_green="\e[92m"


echo -e $ansi_bold"Lyrixal Telegram Bot installer"$ansi_reset
echo "Python3 vertsion check"
py3ver=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
echo -e "Installed Python3 version: "$ansi_bold$py3ver$ansi_reset
if [[ $py3ver == 3\.4* ]]; then
  echo -e $ansi_green"Running compatibale Python version"$ansi_reset;
  echo "installing requirements..."
  if [[ $(pip --version) == pip* ]]; then
	sudo pip install -r requirements
	echo -e $ansi_bold"Enter your bot token from @BotFather:"$ansi_reset
	read user_token
	echo $user_token > key.txt
	echo -e $ansi_bold$ansi_green"Install compelete!"$ansi_reset;
  else
	echo -e $ansi_red"pip is not installed"$ansi_reset;
	echo -e $ansi_bold$ansi_red"Install unsuccessful"$ansi_reset;
  fi
else
	echo -e $ansi_red"Running incompatibale Python version"$ansi_reset;
	echo -e $ansi_bold$ansi_red"Install unsuccessful"$ansi_reset;
fi

echo -e $ansireset;

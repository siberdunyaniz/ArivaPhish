#!/bin/bash
# Update Script
# Script created by @arivatools


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mArivaPhish\e[1;92m directory ...\n\n"
sleep 1.5
cd ..
rm -rf ArivaPhish
cd ArivaPhish
chmod +x *
printf "\n\e[1;92m Update Complete ...\n\e[0m"

}

dependencies
script

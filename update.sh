#!/bin/bash

RED="\033[1;31m"
GREEN="\033[1;32m"
NOCOLOR="\033[0m"

echo

echo -e "Step 1: ${GREEN}Pre-configuring packages${NOCOLOR}"
sudo dpkg --configure -a

echo

echo -e "Step 2: ${GREEN}Fix and attempt to correct a system with broken dependencies${NOCOLOR}"
sudo apt-get install -f

echo

echo -e "Step 3: ${GREEN}Update apt cache${NOCOLOR}"
sudo apt-get update

echo

echo -e "Step 4: ${GREEN}Upgrade packages${NOCOLOR}"
sudo apt-get upgrade

echo

echo -e "Step 5: ${GREEN}Distribution upgrade${NOCOLOR}"
sudo apt-get dist-upgrade

echo

echo -e "Step 6: ${GREEN}Remove unused packages${NOCOLOR}"
sudo apt-get --purge autoremove

echo

echo -e "Step 7: ${GREEN}Clean up${NOCOLOR}"
sudo apt-get autoclean

echo

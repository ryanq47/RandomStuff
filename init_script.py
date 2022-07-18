## Now a python script for better logic handling

##########
# Init kali install script
##########

import os
import subprocess as sp

USERNAME = input("Enter your username (not root): ")



## -- Updates -- ##
def updates():
	os.system("yes | sudo apt update")
	os.system("yes | sudo apt full-upgrade")
	os.system("yes | sudo apt autoremove")

## -- Rotate SSH keys -- ##
def sshkeys():
	os.system("dpkg-reconfigure openssh-server")

def vuln_check():
	## -- rkhunter -- ##
	os.system("yes | apt install rkhunter")
	os.system("rkhunter -c --sk --checkall")

	## chkroot ##
	os.system("yes | apt install chkrootkit")
	os.system("chkrootkit")


def github_tools():
	## -- Github tools -- ##

	#git clone github.com/ryanq47/WEBFLINGER
	#git clone www.github.com/ryanq47/SLAP

	#git clone www.github.com/ryanq47/STARTUP HARDEN script



	## Unpacknig tools##

	#unzip WEBFLINGER.zip -d /opt/tools
	#unzip SLAP.zip -d /opt/tools


	## unzip tools and put in /opt, add to system path
	#export PATH-$PATH:/opt/tools/ >> ~./bashrc


	## Making info directory
	try:
		os.system("mkdir /home/" + USERNAME + "/Desktop/Knowledge")
	except:
		print("File exists, continuing on")

	os.system("git clone https://github.com/RoseSecurity/Anti-Virus-Evading-Payloads")
	os.system("mv Anti-Virus-Evading-Payloads /home/" + USERNAME + "/Desktop/Knowledge/")

	os.system("git clone https://github.com/strandjs/IntroLabs")
	os.system("mv IntroLabs /home/" + USERNAME + "/Desktop/Knowledge/")


## Setting Background
#xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorVirtual1/workspace0/last-image -s ~/Desktop/test.jpeg

## Cron the startup hardening script

## Running logic 
updates()
sshkeys()
vuln_check()
github_tools()



print("Done")

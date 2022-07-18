##########
# Init kali install script
##########

## -- Updates -- ##
yes | sudo apt update
yes | sudo apt full-upgrade
yes | sudo apt autoremove

## -- Rotate SSH keys -- ##
dpkg-reconfigure openssh-server


## -- rkhunter -- ##
yes | apt install rkhunter
rkhunter -c --sk --checkall

## chkroot ##
yes | apt install chkrootkit
chkrootkit



## -- Github tools -- ##

git clone github.com/ryanq47/WEBFLINGER
git clone www.github.com/ryanq47/SLAP

#git clone www.github.com/ryanq47/STARTUP HARDEN script



## Unpacknig tools##

unzip WEBFLINGER.zip -d /opt/tools
unzip SLAP.zip -d /opt/tools


## unzip tools and put in /opt, add to system path
export PATH-$PATH:/opt/tools/ >> ~./bashrc


## Making info directory
mkdir ~/Desktop/Knowledge

git clone www.github.com/RoseSecurity/Anti-Virus-Evading-Payloads
unzip Anti-Virus-Evading-Payloads.zip -d ~/Desktop/Knowledge


## Cron the startup hardening script


echo "Done"

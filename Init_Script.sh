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

git clone www.github.com/ryanq47/TOOL1
git clone www.github.com/ryanq47/TOOL2

git clone www.github.com/ryanq47/STARTUP HARDEN script



## Unpacknig tools##

unzip TOOL1.zip -d /opt/tools
unzip TOOL1.zip -d /opt/tools


## unzip tools and put in /opt, add to system path
export PATH-$PATH:/opt/tools/ >> ~./bashrc


## Cron the startup hardening script


echo "Done"

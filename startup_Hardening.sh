##########
# Hardening Script 
##########

## -- Updates -- ##
yes | sudo apt update
yes | sudo apt full-upgrade
yes | sudo apt autoremove

## -- Rotate SSH keys -- ##
dpkg-reconfigure openssh-server


## -- rkhunter -- ##
rkhunter -c --sk --checkall

## chkroot ##
chkrootkit

echo "Done"

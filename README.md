# imagineer

assume a fresh install of raspbian then...

clone this repository

move MotorShield Folder and edublocks tar file to root directory

to install edublocks

>tar -xf edublocks-arm6l.tar.xz

>edublocks/install-deps.sh

>edublocks/install.sh

now create an autostart for edublocks

>cd .config

create a folder called autostart

>cd autostart

create a file called edublocks.desktop

>sudo nano edublocks.desktop

[Desktop Entry]
Type=Application
Name=EduBlocks
Exec=/usr/bin/python3 /home/pi/edublocks.py

create a file called edublocks.py in the root directory

>sudo nano edublocks.py

import subprocess
subprocess.call(["edublocks"])

now reboot

>reboot

sudo reboot

If all is well then EduBlocks will autostart, you will need to find the ipaddress of the raspberry pi

Assuming that you are using a laptop on the same network then enter the ipaddress and port 8081

192.168.xx.xx:/8081

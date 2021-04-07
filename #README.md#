iRobot Create 2 Roomba Setup

Prerequisites
Software
ROS Melodic
Ubuntu 18.04 (Headless) with GUI (optional)

Hardware
iRobot Create 2
iRobot DIN to USB Cable
Ethernet Cord
HDMI Cord
Keyboard & Mouse
Raspberry Pi Model 3 B+
Raspberry Pi Camera

Installing Ubuntu and ROS

Ubuntu 18.04 headless can be found here (link: https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview)

You may need to use an Ethernet connection for the RPi if modifying the config files doesn't work. I found that it was best to install everything using an ethernet connection. Then connect to Wifi when you have access to the GUI. Although we installed the headless version it was still useful to add the GUI to it to do some simple tasks like switching wifi networks etc. A tutorial for adding the GUI can be found here: https://phoenixnap.com/kb/how-to-install-a-gui-on-ubuntu

If you're on headless you can switch to the GUI using CTRL-ALT-F1
If you're on GUI you can switch to headless using CTRL-ALT-F2

After connecting the RPi to the internet you can enable ssh using openssh.

$ sudo apt update
$ sudo apt install openssh-server
$ sudo systemctl status ssh

If the firewall is enabled you may need to enable the SSH port:

$ sudo ufw allow ssh 

Melodic Installation instructions can be found here: http://wiki.ros.org/melodic/Installation/Ubuntu

The ROS-Base (Bare Bones) option was selected for this project because it's lightweight and won't require any use of GUI tools. 

To insure that the create robot is funtional with ROS follow this tutorial here: https://github.com/AutonomyLab/create_robot







# Etholog Installation 
* This repository allows you to install and run Etholog on a 32 bit Windows XP virtual machine; I used Virtual Box for my installation and that is the package I refer to in this tutorial.
# You will need the following:
* The VirtualBox install file appropriate for your host(Windows, Linux, OSX,etc.) operating system
* The VirtualBox Guest Additions file (an iso file). You want the version that complements your VirtualBox install version
* The 32 bit version of Windows XP (an iso file)
### I'm including the Etholog zip file in this repo. The others you will have to find on your own. Try http://softlay.net/operating-system/windows-xp-sp3-iso-full-version-free-download.html or https://pcriver.com/operating-systems/windows-xp-professional-iso-download.html
### * Install Virtual Box: https://www.virtualbox.org/wiki/Downloads
* Install Windows XP 32 bit using the iso file. Etholog runs on 32 bits NOT 64 bits.
* "Remove" the iso file from its virtual cd drive and load the Guest Additions iso file.
### * After you install Guest Additions(https://docs.oracle.com/cd/E36500_01/E36502/html/qs-guest-additions.html), create a folder on your host machine that you also wish to access on your XP virtual machine. Remember the path as you will need to enter it in the next step.
* Go the "Settings" button for your new XP machine, locate the "Shared Folders" tab and in the top right corner, look for a folder icon with a plus sign on top of it. Click it, add the path to the folder you wish to share. It is also advised to select the "Auto Mount" option, hit "Ok".
* Next, add the etholog zip file to the shared folder you just created. Unzip and install it via XP and you should be good to go running Etholog on a Virtual Machine.

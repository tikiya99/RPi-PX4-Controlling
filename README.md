# RPi-PX4-Controlling

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install future
sudo pat-get install screen wxgtk libxml libxslt
sudo pip install pyserial
sudo pip install dronekit
sudo pip install MAVProxy

raspi-config
Disable UART for console
sudo nano /boot/config.txt - add "dtoverlay=disable-bt"
if ttyAMA0 isnt in /dev, enable_uart=1 in boot/config

mavproxy.py --master=/dev/ttyAMA0

Enter command once the APM is connected;
mode GUIDED

@echo off
echo "Installing Crome For better Experience"
cd Tools
ChromeSetup.exe /silent /install
echo "Installation Done"
echo "-----------------------------------"
echo "Installing selenium module for python"
python -m pip install selenium
echo "Module installation done"
copy chromedriver.exe c:\Drivers
echo "Driver Copy done:Note: It should be in path"
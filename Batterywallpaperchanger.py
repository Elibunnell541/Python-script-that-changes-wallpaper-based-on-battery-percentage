#!/usr/bin/env python3


import os, glob, sys, time
from time import sleep
ON = True
while True:



 maxEnergyFile = open("/sys/class/power_supply/BAT0/energy_full", 'r')
 currentEnergyFile = open("/sys/class/power_supply/BAT0/energy_now", 'r')
 maxEnergy = int(maxEnergyFile.read())
 currentEnergy = int(currentEnergyFile.read())
 batteryPercentage = 100 * currentEnergy / maxEnergy
 sleep_time = 30
 print(f"{batteryPercentage}%")


 if batteryPercentage < 30:
     directory = "/home/elib/Documents/python projects/Batterywallpaper/DEAD/"
 elif batteryPercentage < 80:
    directory = "/home/elib/Documents/python projects/Batterywallpaper/PLUGINBATTERY/"
 else:
    directory = "/home/elib/Documents/python projects/Batterywallpaper/GOODBATTERY/"

 os.chdir(directory)
 files = os.listdir()

 for file in files:
  if file.endswith(".jpg") or file.endswith(".png"):

    full_path = os.path.abspath(file)
    cmd = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops(); for (i=0;i<allDesktops.length;i++) {{ d = allDesktops[i]; d.wallpaperPlugin = \"org.kde.image\"; d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\"); d.writeConfig(\"Image\", \"file://{full_path}\"); }}'"
    os.system(cmd)
    sleep(sleep_time)





import os, glob, sys, time
from time import sleep

while True:


#These all the way to print(f"{batteryPercentage}%") can varie per device I would check if this is correct before running this code 
 maxEnergyFile = open("/sys/class/power_supply/BAT0/energy_full", 'r')
 currentEnergyFile = open("/sys/class/power_supply/BAT0/energy_now", 'r')
 maxEnergy = int(maxEnergyFile.read())
 currentEnergy = int(currentEnergyFile.read())
 batteryPercentage = 100 * currentEnergy / maxEnergy
 sleep_time = 30
 print(f"{batteryPercentage}%") # not required but recommended to keep for testing the program


 if batteryPercentage < 30: # can be changed
     directory = "path/to/folder/of/image" #do not put your image in the directory just the folder your image is in
 elif batteryPercentage < 80: # can be changed
    directory = "path/to/folder/of/image" # again dont put image in the path just the folder your image in
 else:
    directory = "path/to/folder/of/image"  # again dont put image in the path just the folder your image  in

 os.chdir(directory) # changes directory to directory
 files = os.listdir() # lists files in directory

 for file in files:
  if file.endswith(".jpg") or file.endswith(".png"): # files must be either .jpg or .png

    full_path = os.path.abspath(file)
    cmd = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops(); for (i=0;i<allDesktops.length;i++) {{ d = allDesktops[i]; d.wallpaperPlugin = \"org.kde.image\"; d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\"); d.writeConfig(\"Image\", \"file://{full_path}\"); }}'"
    os.system(cmd) # the command can vary depending on your DE so I reccomend checking that before running this; for example, the above command is for kde plasma 5 which covers the root wallpaper or whatever you want to call it otherwise other desktop environments would just use "feh --bg-fill image.png" or something like that
   
    sleep(sleep_time)


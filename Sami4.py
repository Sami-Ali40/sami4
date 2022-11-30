import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://www.facebook.com/profile.php?id=100076381339868')
 
        from RANDOM import Meer
 
        Meer()
 
 
 
elif bit == "32bit":
 
        os.system('xdg-open https://www.facebook.com/profile.php?id=100076381339868')
 
        os.system('python .Sami4.py')

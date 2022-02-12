########################################################################
##  ______                _   _   _      _                      _     ##
## |  ____|              | | | \ | |    | |                    | |    ##
## | |__  __  ____ _  ___| |_|  \| | ___| |___      _____  _ __| | __ ##
## |  __| \ \/ / _` |/ __| __| . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ / ##
## | |____ >  < (_| | (__| |_| |\  |  __/ |_ \ V  V / (_) | |  |   <  ##
## |______/_/\_\__,_|\___|\__|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\ ##
##                          Version 0.1 (BETA)                        ##
##                GitHub Repo -> : xYanis/ExactNetwork                ##
##                 WebSite -> : exactnetwork.cardd.co                 ##
########################################################################

import time
import os
import requests
import subprocess
import urllib.request
from pystyle import Colors, Colorate
t = 1
b = 1

api = requests.get('https://google.fr')
hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
print(Colorate.Horizontal(Colors.yellow_to_red, "[] Loading ExactNetwork...", 5))
time.sleep(t)
os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, "[] Loading : 39%", 1))
time.sleep(t)
os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, "[] Loading : 83%", 1))
time.sleep(t)
os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, "[] Loading : 100%", 1))
time.sleep(t)
os.system('cls') 

try:
    if hardwareid in api.text:
        pass
    else:
        print('[] Your HWID is not into our API')
        time.sleep(2)
        os.system('cls')
        print('[] Your HWID:' + hardwareid + '') 
        time.sleep(5)
        os._exit()
except:
    print('[] Program cannot start, the connexion on our API seem not works, or you are not whitelisted !')
    time.sleep(2)
    os.system('cls')
    print("[] Exiting..")
    time.sleep(1) 
    os._exit()


while True:
    c1a = input("[] Welcome, which version do you want to install? | Supported Version : 1.8.8 - 1.18.1 : ")
    if c1a == "1.8.8":
        print('[] Download 1.8.8 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar'
        urllib.request.urlretrieve(url, './dist/1.8.8.jar', 
        print('[] Downloaded !'))
    if c1a == "1.8":
        print('[] Download 1.8.8 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar'
        urllib.request.urlretrieve(url, './dist/1.8.8.jar', 
        print('[] Downloaded !'))
    if c1a == "1.9.4":
        print('[] Download 1.9.4 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.9.4/builds/773/downloads/paper-1.9.4-773.jar'
        urllib.request.urlretrieve(url, './dist/1.9.4.jar', 
        print('[] Downloaded !'))
    if c1a == "1.9":
        print('[] Download 1.9.4 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.9.4/builds/773/downloads/paper-1.9.4-773.jar'
        urllib.request.urlretrieve(url, './dist/1.9.4.jar', 
        print('[] Downloaded !'))
    if c1a == "1.10.2":
        print('[] Download 1.10.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.10.2/builds/916/downloads/paper-1.10.2-916.jar'
        urllib.request.urlretrieve(url, './dist/1.10.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.10":
        print('[] Download 1.10.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.10.2/builds/916/downloads/paper-1.10.2-916.jar'
        urllib.request.urlretrieve(url, './dist/1.10.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.11.2":
        print('[] Download 1.11.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.11.2/builds/1104/downloads/paper-1.11.2-1104.jar'
        urllib.request.urlretrieve(url, './dist/1.11.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.11":
        print('[] Download 1.11.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.11.2/builds/1104/downloads/paper-1.11.2-1104.jar'
        urllib.request.urlretrieve(url, './dist/1.11.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.12.2":
        print('[] Download 1.12.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar'
        urllib.request.urlretrieve(url, './dist/1.12.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.12":
        print('[] Download 1.12.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar'
        urllib.request.urlretrieve(url, './dist/1.12.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.13.2":
        print('[] Download 1.13.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.13.2/builds/655/downloads/paper-1.13.2-655.jar'
        urllib.request.urlretrieve(url, './dist/1.13.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.13":
        print('[] Download 1.13.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.13.2/builds/655/downloads/paper-1.13.2-655.jar'
        urllib.request.urlretrieve(url, './dist/1.13.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.14.4":
        print('[] Download 1.14.4 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.14.4/builds/243/downloads/paper-1.14.4-243.jar'
        urllib.request.urlretrieve(url, './dist/1.14.4.jar', 
        print('[] Downloaded !'))
    if c1a == "1.14":
        print('[] Download 1.14.4 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.14.4/builds/243/downloads/paper-1.14.4-243.jar'
        urllib.request.urlretrieve(url, './dist/1.14.4.jar', 
        print('[] Downloaded !'))
    if c1a == "1.15.2":
        print('[] Download 1.15.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.15.2/builds/391/downloads/paper-1.15.2-391.jar'
        urllib.request.urlretrieve(url, './dist/1.15.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.15":
        print('[] Download 1.15.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.15.2/builds/391/downloads/paper-1.15.2-391.jar'
        urllib.request.urlretrieve(url, './dist/1.15.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.16.1":
        print('[] Download 1.16.1 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.1/builds/138/downloads/paper-1.16.1-138.jar'
        urllib.request.urlretrieve(url, './dist/1.16.1.jar', 
        print('[] Downloaded !'))
    if c1a == "1.16.2":
        print('[] Download 1.16.2 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.2/builds/189/downloads/paper-1.16.2-189.jar'
        urllib.request.urlretrieve(url, './dist/1.16.2.jar', 
        print('[] Downloaded !'))
    if c1a == "1.16.3":
        print('[] Download 1.16.3 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.3/builds/253/downloads/paper-1.16.3-253.jar'
        urllib.request.urlretrieve(url, './dist/1.16.3.jar', 
        print('[] Downloaded !'))
    if c1a == "1.16.4":
        print('[] Download 1.16.4 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar.jar'
        urllib.request.urlretrieve(url, './dist/1.16.4.jar', 
        print('[] Downloaded !'))
    if c1a == "1.16.5":
        print('[] Download 1.16.5 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/790/downloads/paper-1.16.5-790.jar'
        urllib.request.urlretrieve(url, './dist/1.16.5.jar', 
        print('[] Downloaded !'))
    if c1a == "1.16":
        print('[] Download 1.16.5 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/790/downloads/paper-1.16.5-790.jar'
        urllib.request.urlretrieve(url, './dist/1.16.5.jar', 
        print('[] Downloaded !'))
    if c1a == "1.17":
        print('[] Download 1.17 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.17/builds/66/downloads/paper-1.17-66.jar'
        urllib.request.urlretrieve(url, './dist/1.17.jar', 
        print('[] Downloaded !'))
    if c1a == "1.17.1":
        print('[] Download 1.17.1 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/408/downloads/paper-1.17.1-408.jar'
        urllib.request.urlretrieve(url, './dist/1.17.1.jar', 
        print('[] Downloaded !'))
    if c1a == "1.18":
        print('[] Download 1.18 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.18/builds/66/downloads/paper-1.18-66.jar'
        urllib.request.urlretrieve(url, './dist/1.18.jar', 
        print('[] Downloaded !'))
    if c1a == "1.18.1":
        print('[] Download 1.18.1 !')
        time.sleep(2)
        os.system('cls')
        url = 'https://papermc.io/api/v2/projects/paper/versions/1.18.1/builds/167/downloads/paper-1.18.1-167.jar'
        urllib.request.urlretrieve(url, './dist/1.18.1.jar', 
        print('[] Downloaded !'))
    
    
    
    
    
    
    
    



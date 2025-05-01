# -*- coding: utf-8 -*-
#####################################
#        Pernah Waras               #
#    Code by h0d3_g4n               #
#   Telegram = @h0d3_g4n            #
#   ICQ = @h0d3_g4n                 #
#   Skype = live:f2c962ccea77ec0    #
#####################################
import requests, re, urllib2, os, sys, codecs, random, base64,json  
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time                 
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
biru = '\033[34m'
ungu = '\033[35m'
birumuda = '\033[36m'
grey = '\033[37m'
CEND = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")

try:
        with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
                ooo = f.read().splitlines()
except IndexError:
        print (abang + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)
        pass
ooo = list((ooo))

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

def addadmin(url):
    try:
        get1 = requests.Session()
        response = get1.get(url+'/elfinder', headers=headers, verify=False,timeout=15).text.encode('utf-8')
        if 'elfinder/connector' in response or '/packages/barryvdh/elfinder/js/elfinder.min.js' in response:
            print "Target : {} Success ".format(url)
            open("elfinder.txt","a").write(url+"\n")
        else:
            print "Target : {} Not Laravel".format(url)
    except Exception as error:
        #print(str(error))
        pass

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' 
 ___ ___ ___ __  _  __  _  _   _   _  __  ___  __   __  
| _,| __| _ |  \| |/  \| || | | | | |/  \| _ \/  \/' _/ 
| v_| _|| v | | ' | /\ | >< | | 'V' | /\ | v | /\ `._`. 
|_| |___|_|_|_|\__|_||_|_||_| !_/ \_|_||_|_|_|_||_|___/ 

                    Bot BY h0d3_g4n

             '''
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        pass


logo()

##########################################################################################
def Main():
        try:
                
                start = timer()
                ThreadPool = Pool(25)
                Threads = ThreadPool.map(addadmin, ooo)
                print('TIME TAKE: ' + str(timer() - start) + ' S')
        except:
                pass


if __name__ == '__main__':
        Main()
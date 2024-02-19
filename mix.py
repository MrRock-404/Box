####Create by Rex Hynter
import os
import sys
import time


os.system("clear")


logo=("""\x1b[38;5;46m       

██████╗░███████╗██╗░░██╗
██╔══██╗██╔════╝╚██╗██╔╝
██████╔╝█████╗░░░╚███╔╝░
██╔══██╗██╔══╝░░░██╔██╗░
██║░░██║███████╗██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝   """)



def Main():
	os.system('clear')
	print(logo)
	print(58*'\033[1;32m═')
	print('\x1b[38;5;196m[\x1b[38;5;46m1\x1b[38;5;196m]\033[1;32m TERMUX SETUP  \x1b[38;5;196m[\x1b[38;5;46mBASIC -SETUP\x1b[38;5;196m] ')
	print('\x1b[38;5;196m[\x1b[38;5;46m2\x1b[38;5;196m]\033[1;32m TERMUX SETUP  \x1b[38;5;196m[\x1b[38;5;46mFULL-SETUP\x1b[38;5;196m] ')
	print('\x1b[38;5;196m[\x1b[38;5;46m3\x1b[38;5;196m]\033[1;32m TERMUX SETUP  \x1b[38;5;196m[\x1b[38;5;46m100%-SETUP\x1b[38;5;196m] ')
	print('\x1b[38;5;196m[\x1b[38;5;46m4\x1b[38;5;196m]\033[1;32m Report a problem \x1b[38;5;196m[\x1b[38;5;46mADMIN\x1b[38;5;196m]')
	print('\x1b[38;5;196m[\x1b[38;5;46m0\x1b[38;5;196m]\033[1;32m Exit')
	print(58*'═')
	opt = input('\x1b[38;5;196mChoose :> \x1b[38;5;46m')
	if opt =='1':
		basic()
	if opt =='2':
		pkg()
	if opt =='3':
		setup()
	if opt =='4':
		admin()
	elif opt =='0':
		exit()
	else:
		print('\n\x1b[38;5;196mChoose valid option');time.sleep(1)
		Main()
def basic():
  os.system("rm -rf Compile")
  os.system("git clone https://github.com/MrRock-404/Compile")
  os.system("cd Compile")
  os.system("python Compile.py")	
  print(logo)
  
def pkg():
  
  os.system("python Compile.py")
  print(logo)

  
def setup():
  
  
  os.system("python Fb-Auto-Share.py")
  
  print(logo)
def admin():
	os.system('clear')
	print(logo)
	print(60*'\033[1;32m═')
	print('\033[1;32m [1] Follow Github  ')
	print('\033[1;32m [2] Join Facebook Group ')
	print('\033[1;32m [3] Contact Admin ')
	print('\033[1;32m [0] Back to Main menu')
	print(60*'\033[1;32m═')
	bal = input('Choose :> ')
	if bal =='1':
		os.system('xdg-open https://github.com/MrRock-404');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open https://facebook.com/groups/763961535200112/');time.sleep(1)
		admin()
	if bal =='3':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100092547069162/');time.sleep(1)
		admin()
	if bal =='0':
		Main()
	

Main()

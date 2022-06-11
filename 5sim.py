
import requests
import time
from colorama import Fore
import os
from os import system

token = '' # add your 5sim api key here https://5sim.net

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}
def buy():
    system("title 5sim ")
    r2= requests.get('https://5sim.net/v1/user/profile', headers=headers).json()
    email= r2["email"]
    balance = r2["balance"]
    print(f"""{Fore.BLUE}
███████╗    ███████╗██╗███╗   ███╗    
██╔════╝    ██╔════╝██║████╗ ████║    
███████╗    ███████╗██║██╔████╔██║    
╚════██║    ╚════██║██║██║╚██╔╝██║    
███████║    ███████║██║██║ ╚═╝ ██║    
╚══════╝    ╚══════╝╚═╝╚═╝     ╚═╝{Fore.RESET}""")        
    print(f"{Fore.BLUE}[{Fore.RESET}-{Fore.BLUE}]{Fore.RESET} Mail: {email} {Fore.BLUE}[{Fore.RESET}-{Fore.BLUE}]{Fore.RESET} Balance: {balance}")
    country = input(str(f"{Fore.BLUE}[{Fore.RESET}-{Fore.BLUE}]{Fore.RESET} Country: "))
    product = input(str(f"{Fore.BLUE}[{Fore.RESET}-{Fore.BLUE}]{Fore.RESET} Product: "))
    r = requests.get(f'https://5sim.net/v1/user/buy/activation/russia/any/instagram', headers=headers).json()
    phone_id = r["id"]
    phone_number = r["phone"]
    price = r["price"]
    print(f"{Fore.BLUE}[{Fore.RESET}+{Fore.BLUE}]{Fore.RESET} {price}₽    1₽ =  0,014 Euro (3.6.22)")
    print(f"{Fore.BLUE}[{Fore.RESET}+{Fore.BLUE}]{Fore.RESET} {phone_number}")
    time.sleep(6)
    timer = 0
    while timer < 40:
        time.sleep(3)
        r3 = requests.get('https://5sim.net/v1/user/check/' + str(phone_id), headers=headers).json()
        if r3["status"] == "RECEIVED":
            if r3["sms"]:
                sms = r3["sms"][0]["code"]
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} {sms}")
                r2 = requests.get(f'https://5sim.net/v1/user/finish/{phone_id}', headers=headers).json()

        else:
            print(f"{Fore.BLUE}[{Fore.RESET}/{Fore.BLUE}]{Fore.RESET} Waiting for code ")
            timer += 1
buy()

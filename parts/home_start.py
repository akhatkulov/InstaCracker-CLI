from sys import stdout
from colorama import Fore, init
from tabulate import tabulate
import typer

def home_page():
        stdout.write("                  "+Fore.GREEN   +"________             _____       _________                   ______                  \n")
        stdout.write("                  "+Fore.GREEN   +"____  _/_______________  /______ __  ____/____________ _________  /______________    \n")
        stdout.write("                  "+Fore.GREEN   +" __  / __  __ \_  ___/  __/  __ `/  /    __  ___/  __ `/  ___/_  //_/  _ \_  ___/    \n")
        stdout.write("                  "+Fore.GREEN   +"__/ /  _  / / /(__  )/ /_ / /_/ // /___  _  /   / /_/ // /__ _  ,<  /  __/  /        \n")
        stdout.write("                  "+Fore.GREEN   +"/___/  /_/ /_//____/ \__/ \__,_/ \____/  /_/    \__,_/ \___/ /_/|_| \___//_/         \n")
        stdout.write("                  "+Fore.GREEN   +"                                                                                     \n")
        
        insta_home_table = [
            [f'{typer.style("Apps Target",fg=typer.colors.GREEN)}',typer.style("Brute Force Attack for Instagram",fg=typer.colors.GREEN)],
            [f'{typer.style("Guide",fg=typer.colors.GREEN)}',typer.style("In README.md",fg=typer.colors.GREEN)],
            [f'{typer.style("Author",fg=typer.colors.GREEN)}',typer.style("Akhatkulov Mekhroj",fg=typer.colors.GREEN)],
            [f'{typer.style("Github",fg=typer.colors.GREEN)}',typer.style("github.com/akhatkulov/InstaCracker-CLI",fg=typer.colors.GREEN)],

        ]
        print(tabulate(insta_home_table,headers='firstrow',tablefmt='pqsl'))
##############################################################################################
home_page()
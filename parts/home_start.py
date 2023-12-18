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
##############################################################################################
home_page()
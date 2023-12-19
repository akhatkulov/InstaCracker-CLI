import typer
from typing import Optional
import os
import sys
import inquirer
import colorama 


###################
from parts import *
from helper import *
def main(status:str = typer.Optional('home',help="Status"),username: str = typer.Optional('none'),passwd_w:str=typer.Optional('-1')):
    typer.echo("hello world")
    if status == "home":
      home_page()
    elif status == "start" and passwd_w == "-6w":
      w6_start()
        
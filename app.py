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

    if status == "home":
          home_page()
    elif passwd_w == "-6w":
      w6_start()
    elif passwd_w == "-7w":
      w7_start()
    elif passwd_w == '-8w':
      w8_start()
    elif passwd_w == "-9w":
      w9_start()
    elif passwd_w == "-10w":
      w10_start()
    elif passwd_w == "-11w":
      w11_start()
    elif passwd_w == '-12w':
      w12_start()
    elif passwd_w == '-13w':
      w13_start()
    elif passwd_w == "-14w":
      w14_start()
    else:
      default_start()
        
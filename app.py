import typer
from typing import Optional
import os
import sys
import inquirer
import colorama 
###################
from parts import *
from helper import *
#############################


def main(status: Optional[str]= typer.Argument("home")):
    home_page()
    if status == "home":
          home_page()
    elif status == "-6w":
      w6_start()
    elif status == "-7w":
      w7_start()
    elif status == '-8w':
      w8_start()
    elif status == "-9w":
      w9_start()
    elif status == "-10w":
      w10_start()
    elif status == "-11w":
      w11_start()
    elif status == '-12w':
      w12_start()
    elif status == '-13w':
      w13_start()
    elif status == "-14w":
      w14_start()
    else:
      default_start()
        
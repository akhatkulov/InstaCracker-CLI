import typer
from typing import Optional
import os
import sys
import inquirer

###################
from parts import *
from helper import *
#############################


def main(status: Optional[str]= typer.Argument("home")):
    home_page()
    if status == "home":
      home_page()
    elif status == "hack--6w":
      w6_start()
    elif status == "hack--7w":
      w7_start()
    elif status == 'hack--8w':
      w8_start()
    elif status == "hack--9w":
      w9_start()
    elif status == "hack--10w":
      w10_start()
    elif status == "hack--11w":
      w11_start()
    elif status == 'hack--12w':
      w12_start()
    elif status == 'hack--13w':
      w13_start()
    elif status == "hack--14w":
      w14_start()
    else:
      default_start()
        
if __name__ == "__main__":
  typer.run(main)
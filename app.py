import typer
from typing import Optional
import os
import sys
import inquirer

###################
from parts import *
from helper import *
#############################


def main(status: Optional[str] = typer.Argument("home"), target: Optional[str] = typer.Argument("none")):
    home_page()
    # username = typer.prompt(typer.style("--[x]-- Enter a username",fg=typer.colors.GREEN))
    if status == "home":
      home_page()
    elif status == "hack--6w":
      w6_start(target)
    elif status == "hack--7w":
      w7_start(target)
    elif status == 'hack--8w':
      w8_start(target)
    elif status == "hack--9w":
      w9_start(target)
    elif status == "hack--10w":
      w10_start(target)
    elif status == "hack--11w":
      w11_start(target)
    elif status == 'hack--12w':
      w12_start(target)
    elif status == 'hack--13w':
      w13_start(target)
    elif status == "hack--14w":
      w14_start(target)
    else:
      default_start(target)
        
if __name__ == "__main__":
  typer.run(main)
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
    if status == "home":
      home_page()
      Lang = [
        inquirer.List(
          "language",
           message="Choose language",
           choices=[typer.style('Uzbek',fg=typer.colors.GREEN),typer.style("Russian",fg=typer.colors.GREEN),typer.style("English",typer.colors.GREEN)]
        ),
      ]
      x = inquirer.prompt(Lang)
      if "Uzbek" in x["language"]:
        mode = [
          inquirer.List(
            "mode",
            message="Parol uzunligini tanlang",
            choices=[
              typer.style("odatiy",fg=typer.colors.GREEN),
              typer.style("6",fg=typer.colors.GREEN),
              typer.style("7",fg=typer.colors.GREEN),
              typer.style("8",fg=typer.colors.GREEN),
              typer.style("9",fg=typer.colors.GREEN),
              typer.style("10",fg=typer.colors.GREEN),
              typer.style("11",fg=typer.colors.GREEN),
              typer.style("12",fg=typer.colors.GREEN),
              typer.style("13",fg=typer.colors.GREEN),
              typer.style("14",fg=typer.colors.GREEN),
              
            ]
          ),
        ]
        y = inquirer.prompt(mode)
        if "odatiy" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          default_start(user)
        elif "6" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w6_start(user)
        elif "7" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w7_start(user)
        elif "8" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w8_start(user)
        elif "9" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w9_start(user)
        elif "10" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w10_start(user)
        elif "11" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w11_start(user)
        elif "12" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w12_start(user)
        elif "13" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w13_start(user)
        elif "14" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w14_start(user)
      ######################## Russian ##################################
      if "Russian" in x["language"]:
        mode = [
          inquirer.List(
            "mode",
            message="Parol uzunligini tanlang",
            choices=[
              typer.style("odatiy",fg=typer.colors.GREEN),
              typer.style("6",fg=typer.colors.GREEN),
              typer.style("7",fg=typer.colors.GREEN),
              typer.style("8",fg=typer.colors.GREEN),
              typer.style("9",fg=typer.colors.GREEN),
              typer.style("10",fg=typer.colors.GREEN),
              typer.style("11",fg=typer.colors.GREEN),
              typer.style("12",fg=typer.colors.GREEN),
              typer.style("13",fg=typer.colors.GREEN),
              typer.style("14",fg=typer.colors.GREEN),
              
            ]
          ),
        ]
        y = inquirer.prompt(mode)
        if "odatiy" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          default_start(user)
        elif "6" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w6_start(user)
        elif "7" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w7_start(user)
        elif "8" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w8_start(user)
        elif "9" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w9_start(user)
        elif "10" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w10_start(user)
        elif "11" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w11_start(user)
        elif "12" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w12_start(user)
        elif "13" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w13_start(user)
        elif "14" in y["mode"]:
          user = typer.prompt(f"{typer.style('Foydalanuvchi nomini kiriting',fg=typer.colors.GREEN)}")
          w14_start(user)
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
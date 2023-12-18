import typer
from tabulate import tabulate 

def insta_table():
          
        insta_home_table = [
            [f'{typer.style("Apps Target",fg=typer.colors.GREEN)}',typer.style("Brute Force Attack for Instagram",fg=typer.colors.GREEN)],
            [f'{typer.style("Guide",fg=typer.colors.GREEN)}',typer.style("In README.md",fg=typer.colors.GREEN)],
            [f'{typer.style("Author",fg=typer.colors.GREEN)}',typer.style("Akhatkulov Mekhroj",fg=typer.colors.GREEN)],
            [f'{typer.style("Github",fg=typer.colors.GREEN)}',typer.style("github.com/akhatkulov/InstaCracker-CLI",fg=typer.colors.GREEN)],

        ]
        print(tabulate(insta_home_table,headers='firstrow',tablefmt='pqsl'))
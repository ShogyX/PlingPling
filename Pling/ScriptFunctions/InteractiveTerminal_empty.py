from ScriptFunctions.UmbrellaScript import recieve_command
import os
import sys
from colorama import Fore, Style


plingpling = """ 
+-----------------------------------------------------+    
|     ____  ___                ____  ___              |
|    / __ \/ (_)___  ____ _   / __ \/ (_)___  ____ _  |
|   / /_/ / / / __ \/ __ `/  / /_/ / / / __ \/ __ `/  |
|  / ____/ / / / / / /_/ /  / ____/ / / / / / /_/ /   |
| /_/   /_/_/_/ /_/\__, /  /_/   /_/_/_/ /_/\__, /    |
|                 /____/                   /____/     |
+-----------------------------------------------------+
  Created by Shogy
  Github: https://github.com/ShogyX/PlingPling
"""

def print_colored_plingpling(plingpling_string):
    colored_plingpling = (
        f"{Fore.LIGHTBLUE_EX}{plingpling_string}{Style.RESET_ALL}"
    )
    print(colored_plingpling)

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def main():
    print_colored_plingpling(plingpling)
    print("Type 'help' for instructions.")

    while True:
        pass
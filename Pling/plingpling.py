from ScriptFunctions.InteractiveTerminal import main
from ScriptFunctions.UmbrellaScript import recieve_command
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

# Check if command-line arguments are provided prior to execution
if len(sys.argv) > 1:
    print_colored_plingpling(plingpling)
    command = sys.argv[1:]
    word_list_path = None
    custom_word_list_path = None
    out_path = None
    result_string = " ".join(command)
    command = result_string.lower()
    command_status = recieve_command(command, word_list_path, custom_word_list_path, out_path)
    print(command_status)
else:
    if __name__ == "__main__":
        main()

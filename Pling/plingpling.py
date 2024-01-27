from ScriptFunctions.UmbrellaScript import recieve_command
import os
import sys
from colorama import Fore, Style
import json
import re

def process_input(input_str):
    # Convert to lowercase, remove extra spaces
    cleaned_input = re.sub(r'\s+', ' ', input_str.lower().strip())
    return cleaned_input

def edit_command_preset(preset_name, new_command, file_path="/Presets/all_presets.json"):
    try:
        # Read the command presets from the JSON file
        with open(file_path, 'r') as preset_file:
            command_presets = json.load(preset_file)

        if preset_name in command_presets:
            command_presets[preset_name] = new_command

            # Write the updated dictionary to the file
            with open(file_path, 'w') as updated_file:
                json.dump(command_presets, updated_file, indent=2)

            print(f"Command preset '{preset_name}' updated.")
        else:
            print(f"Error: Command preset '{preset_name}' not found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Unable to load command presets from '{file_path}'.")

def delete_command_preset(preset_name, file_path="/Presets/all_presets.json"):
    try:
        # Read the command presets from the JSON file
        with open(file_path, 'r') as preset_file:
            command_presets = json.load(preset_file)

        if preset_name in command_presets:
            del command_presets[preset_name]

            # Write the updated dictionary to the file
            with open(file_path, 'w') as updated_file:
                json.dump(command_presets, updated_file, indent=2)

            print(f"Command preset '{preset_name}' deleted.")
        else:
            print(f"Error: Command preset '{preset_name}' not found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Unable to load command presets from '{file_path}'.")

def load_command_preset(command_preset_name, file_path="/Presets/all_presets.json"):
    try:
        # Read the command presets from the JSON file
        with open(file_path, 'r') as preset_file:
            command_presets = json.load(preset_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Unable to load command presets from '{file_path}'.")
        return

    # Retrieve the command from the presets based on the provided name
    command = command_presets.get(command_preset_name)

    return command

def print_command_presets(file_path="/Presets/all_presets.json"):
    try:
        # Read the command presets from the JSON file
        with open(file_path, 'r') as preset_file:
            command_presets = json.load(preset_file)

        print("Command Presets:")
        for preset_name, command in command_presets.items():
            print(f"{preset_name}: {command}")

    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Unable to load command presets from '{file_path}'.")

def save_command_preset(command_preset, command_preset_name, file_path="/Presets/all_presets.json"):
    # Validate the command (add your validation logic here)
    if not command_preset:
        print("Warning: Empty command. The command preset may not be valid.")

    # Read existing content or initialize an empty dictionary
    try:
        with open(file_path, 'r') as preset_file:
            existing_data = json.load(preset_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

    # Update the dictionary with the new command
    existing_data[command_preset_name] = command_preset

    # Write the updated dictionary to the file
    with open(file_path, 'w') as preset_file:
        json.dump(existing_data, preset_file, indent=2)

    print(f"Command preset '{command_preset_name}' saved to '{file_path}'.")

def print_colored_plingpling(plingpling_string):
    colored_plingpling = (
        f"{Fore.LIGHTBLUE_EX}{plingpling_string}{Style.RESET_ALL}"
    )
    print(colored_plingpling)

def validate_and_count_words(path):
    try:
        # Validate if the path exists
        if not os.path.exists(path):
            return f"Error: Path '{path}' does not exist."

        # Validate if the path is a file
        if os.path.isfile(path):
            with open(path, 'r') as file:
                content = file.read()
                words_count = len(content.split())
                file_name = os.path.basename(path)
                return f"The file '{file_name}' contains {words_count} words."

        # Check if the path is a directory
        elif os.path.isdir(path):
            return f"Found directory at '{path}'."

        else:
            return f"The path '{path}' is neither a file nor a directory."

    except Exception as e:
        return f"Error: {e}"

script_variables = {"wordlist": None, "custom_input": None, "out_path":None}

def set_variable(script_variables, variable, new_value):
    if variable in script_variables:
        script_variables[variable] = new_value
        print(f"{variable} path set to {new_value}")
    else:
        print(f"Error: '{variable}' not found")

def unset_variable(script_variables, variable):
    if variable in script_variables:
        script_variables[variable] = None
        print(f"Value of variable '{variable}' unset")
    else:
        print(f"Error: Variable '{variable}' not found in script")

def show_variables(script_variables):
    print("SET PATHS:")
    for variable, value in script_variables.items():
        print(f"{variable}: {value}")

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def main():
    
    plingpling = """ 


+-----------------------------------------------------+    
|     ____  ___                ____  ___              |
|    / __ \/ (_)___  ____ _   / __ \/ (_)___  ____ _  |
|   / /_/ / / / __ \/ __ `/  / /_/ / / / __ \/ __ `/  |
|  / ____/ / / / / / /_/ /  / ____/ / / / / / /_/ /   |
| /_/   /_/_/_/ /_/\__, /  /_/   /_/_/_/ /_/\__, /    |
|                 /____/                   /____/     |
+-----------------------------------------------------+
  Created by [creator]   |   Twitter: [Twitter Link]
                         |   Github:  [Github Link]

Type 'help' for instructions.
"""

    print_colored_plingpling(plingpling)
    keywords = []
    while True:
        user_input = input("Enter a command (type 'q' to exit): ")
        user_input = process_input(user_input)

        
        # Check if the user wants to exit
        if user_input.lower() == 'exit' or user_input.lower() == 'quit' or user_input.lower() == 'q':
            #print("Exiting the program. Goodbye!")
            break
        elif user_input.lower() == 'help':
            print("print help instructions")

        elif user_input.lower().startswith('save preset '):
            inp_as_list = user_input.split(" ")
            name = inp_as_list[2]
            del inp_as_list[0]
            del inp_as_list[0]
            del inp_as_list[0]
            command = " ".join(inp_as_list)
            save_command_preset(command, name)

        elif user_input.lower().startswith('edit preset '):
            inp_as_list = user_input.split(" ")
            name = inp_as_list[2]
            del inp_as_list[0]
            del inp_as_list[0]
            del inp_as_list[0]
            command = " ".join(inp_as_list)
            edit_command_preset(name, command)
        elif user_input.lower().startswith('delete preset '):
            name = user_input.split(" ")[-1]
            delete_command_preset(name)

        elif user_input.lower().startswith('load preset '):
            name = user_input.split(" ")[-1]
            
            print(load_command_preset(name))
            
        elif user_input.lower().startswith('set '):
            user_input = user_input.split(" ")
            variable_to_set = user_input[1]
            new_value = user_input[-1]
            set_variable(script_variables, variable_to_set, new_value)
            print(validate_and_count_words(new_value))

        elif user_input.lower().startswith('unset '):
            user_input = user_input.split(" ")
            variable_to_unset = user_input[1]
            unset_variable(script_variables, variable_to_unset)

        elif user_input.lower().startswith('show'):
            if "paths" in user_input or "path" in user_input:
                show_variables(script_variables)
            elif "preset" in user_input or "presets" in user_input:
                print_command_presets()
            else:
                print("SHOW [PATHS] OR [PRESETS]")

        elif user_input == "clear" or user_input == "cls":
            clear_console()

        elif user_input.lower().startswith("validate path "):
            print(validate_and_count_words(user_input[13:]))

        elif user_input.lower().startswith('run '):
            command = user_input[4:]
            word_list_path = script_variables["wordlist"]
            custom_word_list_path = script_variables["custom_input"]
            out_path = script_variables["out_path"]
            command_status = recieve_command(command, word_list_path, custom_word_list_path, out_path)
            print(command_status)
        # If none of the conditions are met, continue the loop
        else:
            if user_input.lower() in keywords:
                pass

if __name__ == "__main__":
    main()

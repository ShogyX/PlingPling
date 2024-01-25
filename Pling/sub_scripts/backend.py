from .caps_handler import handle_capitalization
from .custom_input_handler import handle_custom_input
from .date_handler import handle_dates
from .number_handler import handle_number_combos
from .word_permutation_handler import handle_word_permutations
from .leet_handler import handle_leet
from .special_char_handler import handle_special_char
import os
from colorama import Fore, Style


def save_list_to_file(my_list, file_path="wordlist_ouput/"):
    try:
        # Check if the file path has a .txt extension
        if file_path.lower().endswith('.txt'):
            with open(file_path, 'w') as file:
                for item in my_list:
                    file.write(str(item) + '\n')
            #print(f"List saved to {file_path}")
        else:
            # If the file path does not have a .txt extension, treat it as a directory
            file_name = 'output.txt'
            file_path = os.path.join(file_path, file_name)
            with open(file_path, 'w') as file:
                for item in my_list:
                    file.write(str(item) + '\n')
            #print(f"List saved to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def reverse_words_in_list(word_list):
    reversed_list = [word[::-1] for word in word_list]
    return reversed_list

def parse_commands(input_string):
    commands = input_string.split('-')[1:]
    parameters = [command.strip() for command in commands]

    params_dict = {}
    for param in parameters:
        key_value = param.split()
        if len(key_value) >= 2:
            key = key_value[0]
            value = ' '.join(key_value[1:])
            params_dict[key] = value
        else:
            key = key_value[0]
            params_dict[key] = None

    return params_dict

def read_files_as_list(file_paths):
    combined_content = []

    if not isinstance(file_paths, list):
        file_paths = [file_paths]

    for file_path in file_paths:
        if not os.path.isabs(file_path):
            # If the path is not absolute, make it absolute based on the current working directory
            file_path = os.path.join(os.getcwd(), file_path)

        if os.path.isdir(file_path):
            # If the given path is a directory, traverse it and its subdirectories
            for root, dirs, files in os.walk(file_path):
                for file_name in files:
                    current_file_path = os.path.join(root, file_name)
                    try:
                        with open(current_file_path, 'r') as file:
                                # Read the content of the file and add it as a list
                                file_content = file.read().splitlines()
                                combined_content.extend(file_content)
                    except Exception as e:
                        print(f"Error: {e} for file '{current_file_path}'")
        elif os.path.isfile(file_path):
            # If the given path is a file, read its content
            try:
                with open(file_path, 'r') as file:
                    # Read the content of the file and add it as a list
                    file_content = file.read().splitlines()
                    combined_content.extend(file_content)
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
            except Exception as e:
                print(f"Error: {e} for file '{file_path}'")
        else:
            print(f"Error: Invalid file or directory path '{file_path}'")
    combined_content = [item for item in combined_content if len(item) >= 1]
    combined_content = list(set(combined_content))
    return combined_content

def recieve_command(command_string, wordlist=None, custom_wordlist=None, outpath=None):
    command_info = parse_commands(command_string)
    if "wl" not in command_info and "wordlist" not in command_info:
        if wordlist == None:
            return("No Wordlist Specified!")
        else:
            command_info["wordlist"] = wordlist
    if "ci" not in command_info and "custom_input" not in command_info:
        if custom_wordlist == None:
            pass
        else:
            command_info["ci"] = "&f="+custom_wordlist
    if "op" not in command_info and "out_path" not in command_info:
        if outpath == None:
            pass
        else:
            command_info["op"] = outpath
    info = create_list(command_info)
    return info

def create_list(params_dict):
    commands = params_dict.keys()

    production_list = []
    final_list = []

    # Variables for gathering information
    
    file_saved_at = ""
    total_words_in_final_list = 0
    used_wordlist = ""
    

    if 'wl' in commands or "wordlist" in commands:
        try:
            wordlist = params_dict.get("wl") or params_dict.get("wordlist")
            used_wordlist = wordlist
        except KeyError:
            raise ValueError("Did Not Find A Wordlist")
        
        production_list.extend(read_files_as_list(wordlist))
        

    if 'wp' in commands or "word_permutation" in commands:
        try:
            wp_option = params_dict.get("wp") or params_dict.get("word_permutation")
        except KeyError:
            wp_option = None

        if wp_option and len(wp_option) > 1:
            production_list.extend(handle_word_permutations(production_list, wp_option))
        else:
            
            production_list.extend(handle_word_permutations(production_list))
        
    if "lm" in commands or "leet_mode" in commands:
        try:
            lm_option = params_dict.get("lm") or params_dict.get("leet_mode")
        except KeyError:
            lm_option = None

        production_list.extend(handle_leet(production_list, lm_option))

    if 'rw' in commands or "reverse_words" in commands:
        production_list.extend(reverse_words_in_list(production_list))

    if 'wc' in commands or "word_capitalization" in commands:
        try:
            caps_option = params_dict.get("wc") or params_dict.get("word_capitalization")
        except KeyError:
            caps_option = None

        production_list.extend(handle_capitalization(production_list, caps_option))
        

    if 'ci' in commands or "custom_input" in commands:
        try:
            custom_option = params_dict.get("ci") or params_dict.get("custom_input")
            custom_option = custom_option
        except KeyError:
            custom_option = None

        final_list.extend(handle_custom_input(production_list, custom_option))
        total_words_in_final_list = len(final_list)

    if 'gd' in commands or "generate_dates" in commands:
        try:
            date_option = params_dict.get("gd") or params_dict.get("generate_dates")
        except KeyError:
            date_option = None

        final_list.extend(handle_dates(production_list, date_option))
    
    if 'sc' in commands or "special_character" in commands:
        try:
            sc_option = params_dict.get("sc") or params_dict.get("special_character")
        except KeyError:
            sc_option = None

        final_list.extend(handle_special_char(production_list, sc_option))

    if 'nl' in commands or "number_lists" in commands:
        try:
            num_option = params_dict.get("nl") or params_dict.get("number_lists")
        except KeyError:
            num_option = None

        final_list.extend(handle_number_combos(production_list, num_option))
        

    complete_list = production_list + final_list
    complete_list = list(set(complete_list))
    if 'op' in commands or "out_path" in commands:
        try:
            op_option = params_dict.get("op") or params_dict.get("out_path")
        except KeyError:
            op_option = None

        try:
            file_saved_at = op_option or "Default Location"
            save_list_to_file(complete_list, op_option)
        except Exception as e:
            print(f"Error saving to file: {e}")
    else:
        save_list_to_file(complete_list)

    # Format information into a single string
    total_words_in_final_list = len(complete_list)
    info_string = (
        f"File Saved At: {Fore.BLUE}{file_saved_at}{Style.RESET_ALL}\n"
        f"Used Wordlist: {Fore.CYAN}{used_wordlist}{Style.RESET_ALL}\n"
        f"Total Words in Generated Wordlist: {Fore.GREEN}{total_words_in_final_list}{Style.RESET_ALL}\n"
    )

    return info_string

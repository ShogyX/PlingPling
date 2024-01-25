import os
def filter_list(word_list, x):
    filtered_list = [word for word in word_list if len(word) <= x]
    return filtered_list

def append_words(base_words, words_to_append, position='behind'):
    result_list = []

    if not isinstance(base_words, list):
        base_words = [base_words]

    for base_word in base_words:
        if position == 'behind' or position == "2":
            result_list.extend([base_word + word for word in words_to_append])
        elif position == 'in_front' or position == "1":
            result_list.extend([word + base_word for word in words_to_append])
        elif position == 'both' or position == "3":
            result_list.extend([word + base_word + word for word in words_to_append])
        else:
            raise ValueError("Error: Invalid position option. Please use 'behind' (2), 'in_front' (1), or 'both' (3).")

    return result_list

def read_files_as_list_old(file_paths):
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
    combined_content = list(set(combined_content))
    return combined_content


def read_files_as_list(file_paths):
    combined_content = []

    if not isinstance(file_paths, list):
        file_paths = [file_paths]

    for file_path in file_paths:
        file_path = os.path.normpath(file_path)  # Normalize the path

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
                            # Read the content of the file and add non-empty lines as a list
                            file_content = [line.strip() for line in file.read().splitlines() if line.strip()]
                            combined_content.extend(file_content)
                    except Exception as e:
                        print(f"Error: {e} for file '{current_file_path}'")
        elif os.path.isfile(file_path):
            # If the given path is a file, read its content
            try:
                with open(file_path, 'r') as file:
                    # Read the content of the file and add non-empty lines as a list
                    file_content = [line.strip() for line in file.read().splitlines() if line.strip()]
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

def process_commands(commands_string, base_list, number_list):
    commands_info = {}
    
    return_list = []
    # Split the string based on "&"
    parts = commands_string.split('&')

    for part in parts:
        # Split each part based on "=" to get the command and its argument
        pair = part.split('=')
        
        if len(pair) == 2:
            command, argument = pair
            commands_info[command] = argument

    
    if 'limit' in commands_info or "l" in commands_info:
        try:
            limit_value = int(commands_info['l'])
        except:
            limit_value = int(commands_info['limit'])

        number_list = filter_list(number_list, limit_value)

    if 'position' in commands_info or 'p' in commands_info:
        position_setting = True
        try:
            position_value = int(commands_info['position'])
        except:
            position_value = int(commands_info['p'])
    else:
        position_setting = False

    if 'multi_variation' in commands_info or 'mv' in commands_info:
        try:
            multi_variation_value = commands_info['mv']
            if multi_variation_value == "True" or multi_variation_value == "T" or multi_variation_value == "t" or multi_variation_value == "true":
                mv = True
            else:
                mv = False
        except:
            multi_variation_value = commands_info['multi_variation']
            if multi_variation_value == "True" or multi_variation_value == "T" or multi_variation_value == "t" or multi_variation_value == "true":
                mv = True
            else:
                mv = False
    else:
        mv = False
        
    if mv == False and position_setting == True:
        
        return_list.extend(append_words(base_list, number_list, str(position_value)))
        return return_list
    elif mv == True and position_setting == False:
        
        for x in ["1","2","3"]:
            return_list.extend(append_words(base_list, number_list, x))
        return return_list
        #call func with default position_value = 2
    elif mv == True and position_setting == True:
        position_value += 1
        
        for x in range(1,position_value):
            x = str(x)
            return_list.extend(append_words(base_list, number_list, x))
        return return_list
    else:
        
        return_list.extend(append_words(base_list, number_list))
        return return_list
    
def map_variable_to_string(variable):
    mapping = {
        'A': "SEQUENTIAL.txt",
        'B': "REVERSE_SEQUENTIAL.txt",
        'C': "PURE_NUMBERS.txt",
        'D': "BINARIES.txt",
        'E': "THOUSANDS.txt",
        'F': "REVERSE_THOUSANDS.txt",
        'G' : "STANDARD.txt",
        'H':"RANDOM.txt",
        'CUSTOM': "CUSTOM.txt"
    }

    return mapping.get(variable, "Unknown Option")

def handle_number_combos(wordlist, command_string):
    result_list = []
    path = "NUMBER_COMBOS\\"
    for option in command_string.split("$"):
        if len(option) < 1:
            continue
        if ":" in option:
            sub_settings = option.split(":")[-1]
            option = option.split(":")[0]
            list_path = path + map_variable_to_string(option)
            combo_list = read_files_as_list(list_path)
            
            result_list.extend(process_commands(sub_settings, wordlist, combo_list))
            
        else:
            list_path = path + map_variable_to_string(option)
            combo_list = read_files_as_list(list_path)
            result_list.extend(append_words(wordlist, combo_list))
    result_list = list(set(result_list))
    return result_list


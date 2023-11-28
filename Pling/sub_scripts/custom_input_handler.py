import os

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

def old_read_files_as_list(file_paths):
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
    return combined_content

def read_files_as_list_old(file_paths):
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
                        with open (current_file_path, 'r') as file:
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

def process_commands(commands_string, base_list):
    commands_info = {}
    
    # Split the string based on "&"
    parts = commands_string.split('&')

    for part in parts:
        # Split each part based on "=" to get the command and its argument
        pair = part.split('=')
        
        if len(pair) == 2:
            command, argument = pair
            commands_info[command] = argument

    
    if 'file' in commands_info or "f" in commands_info:
        try:
            file_path = commands_info['f']
            
        except:
            file_path = commands_info['file']
        
        file_paths = [path.strip() for path in file_path.split(",") if len(path.strip()) > 0]

        date_list = read_files_as_list(file_paths)
        
    else:
        print("No file argument or incorrect file argument. Program is skipping this step")


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
            if multi_variation_value == "True" or multi_variation_value == "T" or multi_variation_value == "t":
                mv = True
            else:
                mv = False
        except:
            multi_variation_value = commands_info['multi_variation']
            if multi_variation_value == "True" or multi_variation_value == "T" or multi_variation_value == "t":
                mv = True
            else:
                mv = False
    else:
        mv = False
        
    if mv == False and position_setting == True:
        return_list = []
        return_list.extend(append_words(base_list, date_list, str(position_value)))
        return return_list
    elif mv == True and position_setting == False:
        return_list = []
        for x in ["1","2","3"]:
            return_list.extend(append_words(base_list, date_list, x))
        return return_list
        #call func with default position_value = 2
    elif mv == True and position_setting == True:
        return_list = []
        for x in range(1,position_value+1):
            x = str(x)
            return_list.extend(append_words(base_list, date_list, x))
        return return_list
    else:
        return_list = []
        return_list.extend(append_words(base_list, date_list))
        return return_list
    
def handle_custom_input (base_words, command_string):
    result_list = process_commands(command_string, base_words)
    result_list = list(set(result_list))
    return result_list


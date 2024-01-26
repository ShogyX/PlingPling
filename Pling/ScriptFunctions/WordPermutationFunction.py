from itertools import permutations, combinations, product
from .CapsFunction import handle_capitalization

def all_permutations_func(input_list):
    return [list(permutation) for permutation in permutations(input_list)]

def handle_reverse_words (wordlist):
    reversed_list = []
    for word in wordlist:
        reversed_list.append(word[::-1])
    return reversed_list

def process_word(word, command_info):
    processed_versions = [word]
    
    if "caps" in command_info or "c" in command_info:
        try:
            arguments = command_info["caps"]
        except:
            arguments = command_info["c"]
        processed_versions.extend(handle_capitalization(word, arguments))
    if "reverse" in command_info or "r" in command_info:
        processed_versions.append(word[::-1])
    
    return processed_versions

def get_combinations(org_parts, command_info):
    combined_results = []
    combined_results.extend(org_parts)
    parts = all_permutations_func(org_parts)
    
    
    for sublist in parts:
        word_combinations = product(*(process_word(word, command_info) for word in sublist))

        # Process each permutation and combine the results
        for combination in word_combinations:
            combined_result = "".join(combination)
            combined_results.append(combined_result)
    return combined_results

def handle_word_permutations (wordlist, command_string=""):
    return_list = []
    commands_info = {}
    if len(command_string) >= 1:
        # Split the string based on "&"
        parts = command_string.split('&')
        
        for part in parts:
            # Split each part based on "=" to get the command and its argument
            pair = part.split('=')
            
            if len(pair) == 2:
                command, argument = pair
                commands_info[command] = argument
            else:
                commands_info[pair[0]] = ""
    
    if "delimiter" in commands_info or "d" in commands_info:
        try:
            delimiter = commands_info["delimiter"]
        except:
            delimiter = commands_info["d"]
    else:
        delimiter = "_"
    
    filtered_words = [word for word in wordlist if delimiter in word]
    
    for word in filtered_words:
        parts = word.split(delimiter)
        return_list.extend(get_combinations(parts, commands_info))
    return_list = list(set(return_list))
    return return_list
    


#print(handle_word_permutations(["word_two"]))
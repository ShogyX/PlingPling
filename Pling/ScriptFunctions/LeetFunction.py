from .LeetDicts import get_leet_presets
from itertools import product

def generate_leet_combinations(word, leet_dict, include_chars=None, exclude_chars=None):
    
    leet_combinations = []

    for char in word:
        if exclude_chars and char.lower() in exclude_chars.lower():
            replacements = [char]
        elif include_chars and char.lower() in include_chars.lower():
            replacements = leet_dict.get(char.lower(), [char])
        elif not include_chars and char.isalpha() and char.lower() in leet_dict:
            replacements = leet_dict[char.lower()]
        else:
            replacements = [char]

        leet_combinations.append(replacements)

    all_leet_words = [''.join(combination) for combination in product(*leet_combinations)]
    return all_leet_words


def generate_all_leet_combinations(word_list, leet_dict, include_chars=None, exclude_chars=None):
    all_leet_words = []

    for word in word_list:
        leet_combinations = generate_leet_combinations(word, leet_dict, include_chars, exclude_chars)
        all_leet_words.extend(leet_combinations)

    return all_leet_words


def handle_leet(input_list, input_string):
    return_list = []
    # Parse the string to extract parameters and values
    params = {}
    param_pairs = input_string.split('&')[1:]
    for pair in param_pairs:
        key, value = pair.split('=')
        params[key] = value

    leet_dict = {}
    e = True
    i = True
    # Process the list based on the parameters and values
    if "di" in params or "dict" in params:
        try:
            preset = params["di"]
        except:
            preset = params["dict"]
        argument = int(preset)
        leet_dict.update(get_leet_presets(argument))
    
    if "w" in params or "whitelist" in params:
        try:
            include = params["w"]
        except:
            include = params["whitelist"]
        
    else:
        i = False
        

    if "b" in params or "blacklist" in params:
        
        try:
            exclude = params["b"]
        except:
            exclude = params["blacklist"]
        
    else:
        e = False
        
    if e == True and i == True:
        
        return_list.extend(generate_all_leet_combinations(input_list, leet_dict, include_chars=include, exclude_chars=exclude))
    elif e == False and i == True:
        return_list.extend(generate_all_leet_combinations(input_list, leet_dict, include_chars=include))
    elif e == True and i == False:
       
        return_list.extend(generate_all_leet_combinations(input_list, leet_dict, exclude_chars=exclude))
    else:
        return_list.extend(generate_all_leet_combinations(input_list, leet_dict))
    
    return_list = list(dict.fromkeys(return_list))
    return return_list




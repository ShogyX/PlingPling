from .LeetRules import get_leet_presets, get_single_leet_rule
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
    if "p" in params or "preset" in params:
        try:
            preset = params["p"]
        except:
            preset = params["preset"]
        preset = get_leet_presets(preset)
        leet_dict.update(preset)
    
    if "i" in params or "include" in params:
        try:
            include = params["i"]
        except:
            include = params["include"]
        
    else:
        i = False
        

    if "e" in params or "exclude" in params:
        
        try:
            exclude = params["e"]
        except:
            exclude = params["exclude"]
        
    else:
        e = False
        

    if "d" in params or "dict" in params:
        try:
            single_dict = params["d"]
        except:
            single_dict = params["dict"]
        single_dict = get_single_leet_rule(single_dict)
        leet_dict.update(single_dict)

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



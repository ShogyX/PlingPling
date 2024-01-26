import itertools
import string

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

def handle_special_char(wordlist, option):
    return_list = []
    # Parse the string to extract parameters and values
    params = {}
    if option != None:
        param_pairs = option.split('&')[1:]
        for pair in param_pairs:
            key, value = pair.split('=')
            params[key] = value
        
    i = True
    e = True
    limit = True
    # Process the list based on the parameters and values
    if "l" in params or "limit" in params:
        try:
            limit = params["l"]
        except:
            limit = params["limit"]
    else:
        limit = False
        
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

    char_list = generate_combinations(limit, i, e)


    if "p" in params or "position" in params:
        try:
            position = params["p"]
        except:
            position = params["position"]
    else:
        position = '2'

    if "mv" in params or "multi_variation" in params:
        mv = True
    else:
        mv = False
        
    if mv == True:
        return_list = []
        position = int(position)
        for x in range(1,position+1):
            x = str(x)
            return_list.extend(append_words(wordlist, char_list, x))
            return_list = list(set(return_list))
        return return_list

    else:
        return append_words(wordlist, char_list, position)

def generate_combinations(max_length, include, exclude):
    if max_length == False:
        max_length = 3
    if include == False:
        include="!?@%=._#123456789"
    if exclude == False:
        exclude = None
    max_length = int(max_length)
    all_characters = string.digits + string.punctuation
    characters = all_characters

    if include:
        characters = ''.join(c for c in all_characters if c in include)
    elif exclude:
        characters = ''.join(c for c in all_characters if c not in exclude)

    combinations = []

    for length in range(1, max_length + 1):
        # Generate all combinations of characters with the given length
        combos = itertools.product(characters, repeat=length)

        # Join each combination into a string
        combo_strings = [''.join(combo) for combo in combos]

        # Exclude combinations that consist only of digits
        valid_combos = [combo for combo in combo_strings if not combo.isdigit()]

        # Append valid combinations to the result list
        combinations.extend(valid_combos)
    combinations = list(set(combinations))
    return combinations



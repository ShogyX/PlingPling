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
        
    # Process the list based on the parameters and values
    if "l" in params or "limit" in params:
        limit = True
        max_length = int(limit)
    else:
        limit = False
        max_length = 3
        
    if "w" in params or "whitelist" in params:
        try:
            include = params["w"]
        except:
            include = params["whitelist"]
    else:
        include="!?@%=._#-*&|<>[]()\}{/£¤\"',§:;123456789"
        

    if "b" in params or "blacklist" in params:
        try:
            exclude = params["b"]
        except:
            exclude = params["blacklist"]
    else:
        exclude = None

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

    char_list = list(set(combinations))

    if "p" in params or "position" in params:
        try:
            position = params["p"]
        except:
            position = params["position"]
    else:
        position = '2'

    if "re" in params or "recursion" in params:
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




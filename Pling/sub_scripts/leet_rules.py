
def common_letter_substitutions():
    return {
        'a': ['4', '@', '^'],
        'e': ['3', '€', '&', ],
        'l': ['1', '|'],
        'o': ['0', "ø"],
        's': ['$', '5', 'z'],
        't': ['7', '1'],
        'b': ['8'],
        'g': ['9'],
        'i': ['1'],
        'z': ['2'],
    }

def uncommon_letter_substitutions():
    return {
        'a': ['å', '^', "æ"],
        'e': ['&', '[-'],
        'l': ['|_', '|-'],
        'o': ['<>', '()'],
        's': ['z', 'ehs'],
        't': ['+'],
    }

def extensive_uncommon_combinations():
    return {
        'a': ['4', '@', '/-\\', '^', '^_^', '∀', 'λ'],
        'e': ['3', '€', '&', '[-', '£', '∑'],
        'l': ['1', '|', '|_', '|-', '1_', '¬'],
        'o': ['0', '()', '[]', '<>', 'Ø', 'Θ'],
        's': ['$', '5', 'z', 'ehs', '§', '∫'],
        't': ['7', '+', '-|-', '1', '†', '↑'],
    }

def word_patterns():
    return {
        'ck': ['x'],
        'er': ['0r', '3r', '£r'],
        'ing': ['1n\'', '1n', '1ñ'],
        'le': ['1e', '£e'],
    }

def uncommon_combinations():
    return {
        'a': ['@', '^', '^_^'],
        'e': ['&', '[-', '£'],
        'l': ['|_', '|-', '1_'],
        'o': ['<>', '()', 'Ø'],
        's': ['z', 'ehs', '§'],
        't': ['1', '+', '†'],
    }

def common_leet_password():
    return {
        'a': ['@', '4', '^'],
        'b': ['8', '13'],
        'e': ['3', '€'],
        'g': ['9', '6'],
        'i': ['1', '!'],
        'l': ['1', '|'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7', '+', '1'],
    }



def map_preset_to_number(preset):
    if isinstance(preset, str):
        preset = preset.strip()  # Remove leading/trailing whitespaces
    preset_mapping = {
        'password': 1,
        'common': 2,
        'uncommon': 3,
        'all': 4,
        '1': 1,  # Allow '1' as a string to map to 1
        '2': 2,
        '3': 3,
        '4': 4,
    }
    try:
        preset_number = int(preset)
        if preset_number < 1:
            raise ValueError("Preset number must be greater than or equal to 1")
    except ValueError:
        preset_number = preset_mapping.get(preset, 0)

    return preset_number
def get_leet_presets(preset=1):
    preset = map_preset_to_number(preset)
    # Standard Leet Speak
    if preset == 1:
        passwrod_leet  = {
            'PasswordLeet': common_leet_password(),
        }
        return {key: value for sub_dict in passwrod_leet.values() for key, value in sub_dict.items()}

    elif preset == 1:
        common = {
            'PasswordLeet': common_leet_password(),
            'Common': common_letter_substitutions(),
            'words': word_patterns(),
        }
        return {key: value for sub_dict in common.values() for key, value in sub_dict.items()}

    # Diverse Leet Speak
    elif preset == 2:
        uncommon = {
            'PasswordLeet': common_leet_password(),
            'Common': common_letter_substitutions(),
            'Words': word_patterns(),
            "Uncommon" : uncommon_letter_substitutions(),
            "uncommon_2": uncommon_combinations(),
        }
        return {key: value for sub_dict in uncommon.values() for key, value in sub_dict.items()}

    # Advanced Leet Speak
    elif preset == 3:
        alll = {
            'PasswordLeet': common_leet_password(),
            'Common': common_letter_substitutions(),
            'Words': word_patterns(),
            "Uncommon" : uncommon_letter_substitutions(),
            "uncommon_2": uncommon_combinations(),
            "extensive" : extensive_uncommon_combinations,
        }
        return {key: value for sub_dict in alll.values() for key, value in sub_dict.items()}

    

def map_leet_rule_to_number(leet_rule):
    leet_rule_mapping = {
        'common_letter_substitutions': 1,
        'uncommon_letter_substitutions': 2,
        'extensive_uncommon_combinations': 3,
        'word_patterns': 4,
        'uncommon_combinations': 5,
        'common_leet_password': 6,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        # Add more mappings as needed
    }

    if isinstance(leet_rule, str):
        leet_rule = leet_rule.strip()  # Remove leading/trailing whitespaces

    numeric_value = leet_rule_mapping.get(leet_rule, None)
    return numeric_value

def get_single_leet_rule(leet_rule):
    leet_rule = map_leet_rule_to_number(leet_rule)
    if leet_rule == 1:
        return common_letter_substitutions()
    elif leet_rule == 2:
        return uncommon_letter_substitutions()
    elif leet_rule == 3:
        return extensive_uncommon_combinations()
    elif leet_rule == 4:
        return word_patterns()
    elif leet_rule == 5:
        return uncommon_combinations()
    elif leet_rule == 6:
        common_leet_password()
    else:
        raise ValueError(f"Invalid leet rule: {leet_rule}")
    

def convert_with_preset(word_list, preset='all_caps'):
    result = []
    word_list = word_list if isinstance(word_list, list) else [word_list]
    
    word_list = [item for item in word_list if len(item) > 1]

    if preset == 'all_caps' or preset == '1':
        for word in word_list:
            result.append(word.upper())

    elif preset == 'first_letter' or preset == '2':
        for word in word_list:
            result.append(word[0].upper() + word[1:])

    elif preset == 'middle_letter' or preset == '3':
        for word in word_list:
            length = len(word)
            mid_index = length // 2
            if length % 2 == 0:  # Even length
                result.append(word[:mid_index - 1] + word[mid_index - 1:mid_index + 1].upper() + word[mid_index + 1:])
            else:
                result.append(word[:mid_index] + word[mid_index].upper() + word[mid_index + 1:])

    elif preset == 'last_letter' or preset == '4':
        for word in word_list:
            result.append(word[:-1] + word[-1].upper())

    elif preset == 'all_except_first_last' or preset == '5':
        for word in word_list:
            result.append(word[0] + word[1:-1].upper() + word[-1])

    elif preset == 'all_except_first' or preset == '6':
        for word in word_list:
            result.append(word[0:1] + word[1:-1].upper()+ word[-1].upper())

    elif preset == 'all_except_last' or preset == '7':
        for word in word_list:
            result.append(word[:-1].upper() + word[-1])

    elif preset == 'none_except_first_last' or preset == '8':
            for word in word_list:
                result.append(word[0].upper() + word[1:-1] + word[-1].upper())

    else:
        for word in word_list:
            result.append(word.upper())  # Default: all_caps

    return result


def handle_capitalization (base_list, command_string):
    result_list = []
    for call in command_string.split("$"):
        if len(call) >= 1:
            result_list.extend(convert_with_preset(base_list, call))
    result_list = list(set(result_list))
    return result_list

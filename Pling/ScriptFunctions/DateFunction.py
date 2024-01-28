from datetime import datetime, timedelta
from itertools import product

def generate_dates(format_and_ranges, date_range = ""):
    current_date = datetime.now()
    all_dates = []
    format_and_ranges = format_and_ranges if isinstance(format_and_ranges, list) else [format_and_ranges]

    try:
        for format_and_range in format_and_ranges:
            try:
                # Split the input into format and range
                if 'R' in format_and_range or 'r' in format_and_range:
                    try:
                        format_part, range_part = format_and_range.split('R')
                    except:
                        format_part, range_part = format_and_range.split('r')
                    if ':' in range_part:
                        start_year, end_year = map(int, range_part.split(':'))
                        range_years = range(start_year, end_year + 1)
                    else:
                        range_years = range(current_date.year - int(range_part), current_date.year)
                else:
                    format_part = format_and_range
                    range_part = '1'
                    range_years = range(current_date.year - int(range_part), current_date.year)
                format_part = format_part.upper()
                # Validate the format
                placeholders = ['DD', 'MM', 'YYYY', 'YY', "DDMM", "MMDD", "MMYY", "MMYYYY", "DDYY", "DDYYYY", "DDMMYY", "YYMMDD", "YYDDMM"]
                placeholder_present = any(placeholder in format_part for placeholder in placeholders)
                if not placeholder_present:
                    raise ValueError(f"Invalid input format '{format_and_range}'. Please use placeholders {placeholders} in any order.")
                    
                # Generate all combinations of DDMM
                if 'MM' in format_part and 'DD' in format_part:
                    day_month_combinations = product(range(1, 32), range(1, 13))
                elif 'MM' in format_part:
                    day_month_combinations = [(1, month) for month in range(1, 13)]
                elif 'DD' in format_part:
                    day_month_combinations = [(day, 1) for day in range(1, 32)]
                else:
                    day_month_combinations = [(current_date.day, current_date.month)]

                for day, month in day_month_combinations:
                    # Replace placeholders with actual date format
                    date_format = format_part.replace('DD', f'{day:02d}').replace('MM', f'{month:02d}')

                    # Append years based on the position of YYYY or YY
                    for year in range_years:
                        formatted_date = date_format.replace('YYYY', f'{year:04d}').replace('YY', f'{year % 100:02d}')
                        all_dates.append(formatted_date)

            except ValueError as e:
                print(f"Error in processing '{format_and_range}': {e}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None
    unique_list = list(set(all_dates))
    return unique_list

def append_words(base_words, words_to_append, position="2"):
    result_list = []

    if not isinstance(base_words, list):
        base_words = [base_words]

    for base_word in base_words:
        if len(base_word) <1:
            continue
        if position == 'behind' or position == "2":
            result_list.extend([base_word + word for word in words_to_append])
        elif position == 'in_front' or position == "1":
            result_list.extend([word + base_word for word in words_to_append])
        elif position == 'both' or position == "3":
            
            result_list.extend([word + base_word + word for word in words_to_append])
        else:
            raise ValueError("Error: Invalid position option. Please use 'behind' (2), 'in_front' (1), or 'both' (3).")
    return result_list

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

    # if "r" in commands_info or "range" in commands_info:
    #     range_factor = True
    #     try:
    #         date_range = commands_info['r']
    #     except:
    #         date_range = commands_info['range']
    # else:
    #     range_factor = False
    
    if 'format' in commands_info or "f" in commands_info:
        try:
            format = commands_info['f']
        except:
            format = commands_info['format']
        # if range_factor == True:
        #     date_list = generate_dates(format, date_range)
        # else:
        date_list = generate_dates(format)
        
    else:
        date_list = generate_dates("DDMMYYYY")


    if 'position' in commands_info or 'p' in commands_info:
        position_setting = True
        try:
            position_value = int(commands_info['position'])
        except:
            position_value = int(commands_info['p'])

    else:
        position_setting = False

    if 'recursion' in commands_info or 're' in commands_info:
        mv = True
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
    
def handle_dates (base_words, commands_string):
    result_list = process_commands(commands_string, base_words)
    result_list = list(set(result_list))
    return result_list

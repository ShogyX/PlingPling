def parse_commands(input_string):
    commands = input_string.split('-')[1:]
    parameters = [command.strip() for command in commands]

    params_dict = {}
    for param in parameters:
        key_value = param.split()
        key = key_value[0]

        if len(key_value) >= 2:
            values = key_value[1:]
            params_dict[key] = values if len(values) > 1 else values[0]
        else:
            params_dict[key] = None

    return params_dict

# Example input
input_string = "-param1 value1 $1:p=1&l=3 -param2 position=3 limit=3 recursion -param3"

# Call the function
output_dict = parse_commands(input_string)

# Example output
print("Input String:", input_string)
print("Parsed Output:", output_dict)

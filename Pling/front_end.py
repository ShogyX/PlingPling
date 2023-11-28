import re
import json

inout = "-wl [path] -wl $a $b:&t=8 $c$f &f=f &l=2 -wp -wc $1$2$3 -lm $1 &exclude=ABCDEF"

def sanitize_input(input_str):
    # Remove extra spaces and convert to lowercase
    cleaned_input = re.sub(r'\s+', ' ', input_str.lower().strip())
    return cleaned_input

def parse_input(input_str):
    result = {'commands': {}}

    current_command = None

    # Split the input string by '-'
    parts = input_str.split('-')

    for part in parts:
        # Ignore empty parts
        if not part.strip():
            continue

        # Check if the part starts with '$' (preset)
        if part.startswith('$'):
            preset_args = {}

            # Check if there are arguments after ':'
            if ':' in part:
                preset, arg_str = part[1:].split(':')
                preset_args = dict(arg.split('=') for arg in arg_str.split('&'))
            else:
                preset = part[1:]

            result.setdefault('presets', {})[preset] = preset_args

        # Check if the part starts with '&'
        elif part.startswith('&'):
            args = [arg.split('=') if '=' in arg else (arg, None) for arg in part[1:].split('&')]
            for key, value in args:
                result.setdefault('arguments', {}).update({key: value})

        # Otherwise, it's a command
        else:
            command, *args = part.split()
            command_entry = {'args': args, 'presets': [], 'arguments': {}}

            # Add presets and arguments to the command entry
            for arg in args:
                if arg.startswith('$'):
                    command_entry['presets'].append(result.setdefault('presets', {}).get(arg[1:], {}))
                elif arg.startswith('&'):
                    key, value = arg.split('=') if '=' in arg else (arg, None)
                    command_entry['arguments'][key] = value

            result['commands'][command] = command_entry

    return result


# Example usage:
sample_string = "-wl [path] -wl $a $b:&t=8 $c$f &f=f &l=2 -wp -wc $1$2$3 -lm $1 &exclude=ABCDEF"
sample_string = sanitize_input(sample_string)
result = parse_input(sample_string)
print(json.dumps(result, indent=2))


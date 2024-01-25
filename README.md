# PlingPling Documentation

## Introduction

Welcome to PlingPling, a powerful script tool designed to generate variations and combinations of words based on a user-provided wordlist. PlingPling offers a range of customization options, allowing users to create diverse and unique sets of words tailored to their requirments.




### Custom Input

- **Command**: `-ci, -custom_input`

- **Description**: 

    Specifies the path to a file containing additional words or phrases that you want to concatenate with the base wordlist. Each line in the file should only be one word or phrase. Spaces between words may or may not be removed. The calling of this command will ensure that the files specified here is used instead of any file you may have preset in the program earlier.

    **Sample Use:**

    `-ci &f=C:\\your\\path\\here\\file.txt&position=3&mv=t`
    - Note that if you use windows paths you will need to use `\\` instead of just `\`.
    - Note that there should be no space between arguments, only the `&` separator

  **Command Settings:**
  - `&file=[ARG], &f=[ARG]`
  
    Specify the path to the file containing your input. Include only the path without additional characters. 

    Multiple file paths may be specified using `f=[PATH1,PATH2,PATH3]`. 

    Standard Bash and Windows paths are accepted (use `\\` for Windows paths).

  - `&position=[ARG], &p=[ARG]`
  
    Specify the position to add your input to the base word: `in_front (1)`, `behind (2)`, or `both (3)`.


  - `&multi_variation=[ARG], &mv=[ARG]`

    Is used in tandem with the position argument, if you want to create all variants of the positions argument.

    eg. if you call `position=3` with `mv` there will be 3 variants generated like so `[i][BASE]`, `[BASE][i]`, `[i][BASE][i]`


### Wordlist

- **Command**: `-wl, -wordlist`
- **Description**: 

    Specifies the path to the base wordlist file. The wordlist file should contain one word per line, with or without spaces.

    **Sample Use:**

    `-wl C:\\your\\path\\here\\file.txt`
    - Note that if you use windows paths you will need to use `\\` instead of just `\`.

  **Command Settings:**
  - `[PATH]`  

    Specify the path to the file containing your base wordlist. 

    Include only the path without additional characters. 

    Standard Bash and Windows paths are accepted (use `\\` instead of just `\` for Windows paths).

### Output Path

- **Command**: `-op, -out_path`
- **Description** 

    Specifies the directory path where the output files will be saved. If you wish for the output file to have a custom name this must be included in the path with a `.txt` exstention 

    **Sample Use:**

    `-op C:\\your\\path\\here\\file_name.txt`
    - Note that if you use windows paths you will need to use `\\` instead of just `\`.

  **Command Settings:**
  - `[PATH]`
    
    Specify the path to the directory where you want your output. 

    Include only the path without additional characters. 

    If you wish to designate the name of your output file, you may include that at the end of your path with a `.txt` extension. 

    Standard Bash and Windows paths are accepted (use `\\` in Windows paths).

### Generate Dates

- **Command**: `-gd, -generate_dates`
- **Description**:
    Generate large ranges of dates or specicify days, months or years based on requirements. 
    Supports any date format based on user input. 

    This functions will generate a list of dates and append them to each word in the base wordlist based on positional arguments.

    The user is urged to be carful in selecting date ranges as this a large date list will quickly affect the time it takes to generate the output wordlist if run in parallel with others generativ commands.

    **Sample Use:**

    > `-gd &format=DDMMYYYYR6&position=3&mv=t`
    - Note that there should be no space between arguments, only the `&` separator

  **Command Settings:**
  - `&format=, &f=[ARGUMENT]`

    Determines the date format and range of dates. 
    The format can include any combination of `(DD, MM, YY, YYYY)`. 

    Specify the range of years with `R`, e.g., `R4` or `R2001:2005`.
    The base numeric `R4` will tells the script that the range is the last 4 years.


  - `&position=, &p=[ARGUMENT]` 

    Specify the position to add your input to the base word: `in_front (1)`, `behind (2)`, or `both (3)`.

  - `&multi_variation=[ARG], &mv=[ARG]`

    Is used in tandem with the position argument, if you want to create all variants of the positions argument.

    eg. if you call `position=3` with `mv` there will be 3 variants generated like so `[i][BASE]`, `[BASE][i]`, `[i][BASE][i]`

### Word Capitalization

- **Command** `-wc, -word_capitalization`

- **Description**: 
    Generates variants of words with different capitalization patterns, including uppercase, lowercase, and title case.

  **Command Settings:**
  - `&[PRESET]`: 
    Specify which capitalization presets to use (e.g., `&1&2&3`). Default: ALL CAPS - SAMPLE
    <ol>
    <li>PRESETS:</li>
    <li> All                        [$1] - SAMPLE </li>
    <li> First Letter		        [$2] - Sample </li>
    <li> Middle Letter		        [$3] - saMPle </li>
    <li> Last Letter		        [$4] - samplE </li>
    <li> All Except First Last	    [$5] - sAMPLe </li>
    <li> All Except First	 	    [$6] - sAMPLE </li>
    <li> All Except Last	 	    [$7] - SAMPle </li>
    <li> First and Last 		    [$8] - SamplE </li>
    <li> Default: ALL CAPS - SAMPLE </li>
    </ol>

### Number Lists

- **Command**: `-nl, -number_lists`
- **Description**: Appends numerical values to each word in the wordlist. Useful for creating variations with numbers.

  **Command Settings:**
  - `$[PRESET]`: Signal the use of a pre-made file containing number combinations. Available presets: Sequential, Reverse Sequential, Pure Numbers, Binaries, Thousands, Reverse Thousands, Standards, Random, Custom.
  - `:[SETTINGS FOR PRESET]`: Apply settings for the given preset.
  - `&limit=, &l=[ARGUMENT]`: Exclude numbers longer than the specified limit.
  - `&position=, &p=[ARGUMENT]`: Specify the position to add your input to the base word.

   - `&multi_variation=[ARG], &mv=[ARG]`

    Is used in tandem with the position argument, if you want to create all variants of the positions argument.

    eg. if you call `position=3` with `mv` there will be 3 variants generated like so `[i][BASE]`, `[BASE][i]`, `[i][BASE][i]`

### Word Permutation

- **Command**: `-wp, -word_permutation`
- **Description**: Generates word permutations for designated words in the base list. Permutations represent all possible arrangements of the words. The prerequisite for processing words this way is that they are on the same line in the input wordlist and are separated by a known delimiter.

  **Command Settings:**
  - `&reverse_word, &rw`: Create variations where one or more words are reversed.
  - `&caps=, &c=[PRESETS]`: Apply different preset capitalization patterns to one or more words before being combined.
  - `&delimiter=, d=[DELIMITER]`: Specify a new delimiter to separate words.

### Reverse Words

- **Command**: `-rw, -reverse_word`
- **Description**: Reverses the order of characters in each word. Useful for creating variations with reversed words.

### Leet Mode

- **Command**: `-lm, -leet_mode`
- **Description**: Generates leetspeak variants for each word in the wordlist. Leetspeak replaces characters with similar-looking alphanumeric characters.

  **Command Settings:**
  - `&preset=, &p=[PRESET]`: Determine the preset of leet characters to use.
  - `&include=, &i=[CHAR]`: Include characters to be affected by leet conversion.
  - `&exclude=, &e=[CHAR]`: Exclude characters from being affected by leet conversion.
  - `&dict=, &d=[ARGUMENT]`: Use one dict from the source code for leet conversion.

### Special Characters

- **Command**: `-sc, -special_char`
- **Description**: Appends special characters to each word in the wordlist. Useful for creating variations with symbols.

  **Command Settings:**
  - `&limit=, &l=[ARGUMENT]`: Avoid generating output above the given length.
  - `&include=, &i=[CHAR]`: Use only the specified special characters.
  - `&exclude=, &e=[CHAR]`: Exclude specified special characters from the preset.

  - `&multi_variation=[ARG], &mv=[ARG]`

    Is used in tandem with the position argument, if you want to create all variants of the positions argument.

    eg. if you call `position=3` with `mv` there will be 3 variants generated like so `[i][BASE]`, `[BASE][i]`, `[i][BASE][i]`

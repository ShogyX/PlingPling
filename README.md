# PlingPling - Dictionary Generator

## General


### Introduction
Written in Python, PlingPling is a dictionary generator meant to be used after collecting information about a target. Inteded to produce dictionaries for potential email, username or password bruteforcing. The script supports various ways of transforming and generating new words from a base wordlist, with highly customizable options to produce broad and precise dictionaries for effective use in bruteforcing.

### Important
- Using all/many options with large base lists may take time to finish and produce dictionaries exceeding 100 million words. 
- Any custom list input should only have 1 word per line.
- Use of multiple lists may result in small amounts of duplication as lists may contain some identicle words/numbers.
- The interactive command line interface allows you to save presets of multiple commands for quick use in the future.
- Commands are not case sensitive but written with caps in the documentation for better readability.
- The sequence of commands affects the final ouput. See the section below for more info.
- Paths must be passed as dir/dir/file or dir\\dir\\file. Normals windows paths will cause the script to break. 


## Production Order

The order in which commands are enteret into the script will have an impact upon the final dictionary. The way the script processes commands and generate words is sequential.Meaning all new variations are added back to the production list and used by the next script option to generate new words. An example of this is would be using a "base list" with the leet option and reverse word option. The script will use the base list and generate leet verisions of each word, it will then add those words to the production list which already consists of the base list. The reverse words option will use the entire production list which consists of the base words and leet words, and create reversed versions of these words and add it back to the production list. The only exceptions from this are the -wl and -op commands, their execution will always be first and last.


## Special Commands
Commands in this section handle the input, ouput and transformation of the base wordlist provided by the user.

### Wordlist
- Short: -WL
- Long: -Wordlist
- Description: Specify the path to an existing wordlist file. PlingPling will use this wordlist as a base and apply other transformations as specified by other options.
- Example: `-wl [Path To Wordlist]`

### WordPermutation
- Short: -WP
- Long: -WordPermutation
- Description: Enable word permutation mode. PlingPling will generate permutations of words in the base list that are separated by a specific delimiter, the default is "_".
- Example: `-wp [Options]`
    #### Exclusive Options
    - **&ReverseWord, &rw**
    - Description: Calls the reverse words function to also generate word permutations including reversed words.
    - Example: `-wp &ReverseWords`

    - **&Caps=, &c=**
    - Description: Calls the wordcapitalization function to allow for word permutations to include capitalization patterns. Arguments can be provided in the same way as you would for the capitalization command. See the section on the capitalization function to view available patterns.
    - Example: `-wp &caps=$1$3$6`

    - **&Delimiter=, &d=**
    - Description: Specify a custom word delimiter if you dont want to use the default one.
    - Example: `-wp &d=,`

### OutPath
- Short: -OP
- Long: -OutPath
- Description: Specify the output path for the generated dictionary file. If not specified, the default output path is the DefaultOuput folder where the script is stored.
- Example: `-op [Path To Wordlist]`

## Transformative Commands
Commands in this section will generate new transformed versions of words in the base wordlist and/or production list.

### LeetMode
- Short: -LM
- Long: -LeetMode
- Description: Enables leet mode PlingPling will generate leet versions of words in the production list, and add them back to the production list.
- Example: `-lm [Options]`
    #### Required Option
    - Short: &di=
    - Long: &dict=
    - Description: Specify what leet dictionary you want the script to use. The function will default to the password(1) dict if no argument is prvoided. An overview of dicts and their contents can be found in the LeetDicts.py file within the ScriptFunctions folder.
    - Example: `-lm &dict=3`

- Available Options: **Whitelist**, **Blacklist**

### ReverseWords
- Short: -RW
- Long: -ReverseWords
- Description: Enable word reversal. PlingPling will add reversed versions of words in the production list to the production list. This command takes no arguments.
- Example: `-rw`
- Available Options: **None**

### WordCapitalization
- Short: -WC
- Long: -WordCapitalization
- Description: Enable word capitalization mode. PlingPling will generate variations of words in the production list with different capitalization patterns based on requested patterns.
- Example: `-wc $[Presets]`
    #### Required Option
    - Short: $[Preset]
    - Long: $[Preset]
    - Description: Specify the desired capitalization patterns to be used. The current presets available are the following:
    - [$1] - SAMPLE - All Caps
    - [$2] - Sample - First letter Caps
    - [$3] - saMPle - Middle letter(s) Caps
    - [$4] - samplE - Last letter Caps
    - [$5] - sAMPLe - All letters except first and last
    - [$6] - sAMPLE - All letters except first
    - [$7] - SAMPle - All letters except last
    - [$8] - SamplE - First and Last only
    - Example: `-wc $1$2$3$4`


## Connotative Commands
Commands in this section will connotate words, numbers or characters to words in the production list.

### CustomInput
- Short: -CI
- Long: -CustomInput
- Description: Allows you to provide a custom list of words. PlingPling will connotate these words to words in the production list and apply transformations as specified.
- Example: `-ci [Path To Wordlist][Other options]`

### GenerateDates
- Short: -GD
- Long: -GenerateDates
- Description: Enable date generation mode. PlingPling will generate dates to be connotated to words in the production list based on specified rules.
- Example: `-gd [Options]`
    #### Required Option
    - Short: &f=
    - Long: &format=
    - Description: Specify the date format & range. The command accepts formats in the following way &f=DDMMYYYYR3. You may pass any Combination of DDMMYYYY I.E only DD, MM, YYYY or a combination of them. You may also pass YY which will append the last 2 digits of the year ie DDMMYY = 240617 (24.06.2017). The R parameter determines the range of dates, calculated in years meaning that R2 will provide dates for 2 years. You may also specify a specific range of years by providing a start and end year like so R2001:2005. 
    - Example: `-gd &format=MMYYYYR10`
- Available Options: **Position**, **Recursion**

### SpecialCharacter
- Short: -SC
- Long: -SpecialCharacter
- Description: Enable special character mode. PlingPling will connotate various special characters to the words in the production list based on specified rules. The deault characters used are `!?@%=._#-*&|<>[]()\}{/£¤\"',§:;123456789` if nothing else is specified. The function also defaults to position 2 (behind) and a limit of 3 if no other argument is given.
- Example: `-sc [Options]`
- Available Options: **Whitelist**, **Blacklist**, **Position**, **Recursion**, **limit**

### NumberLists
- Short: -NL
- Long: -NumberLists
- Description: Enable number lists mode. PlingPling will append specific number patterns to words in production list based on requested patterns.
- Example: `-nl $[Preset]:[Options]`
    #### Required Option
    - Short: $[Preset]
    - Long: $[Preset]
    - Description: Specify the precompiled lists of integers to be used by the command. Current presets available are listed below. The user is encouraged to view the lists in the NumberLists folder on Github or locally to better understand what lists suit their needs. Custom lists can be added to the CUSTOM.txt document.
    - [$1] - SEQUENTIAL.txt
    - [$2] - REVERSE_SEQUENTIAL.txt
    - [$3] - PURE_NUMBERS.txt
    - [$4] - BINARIES.txt
    - [$5] - THOUSANDS.txt
    - [$6] - REVERSE_THOUSANDS.txt
    - [$7] - STANDARD.txt
    - [$8] - RANDOM.txt
    - [$CUSTOM] - CUSTOM.txt
    - Example: `-nl $A$D$E$CUSTOM`
    - Note: Fruther options can be applied to each list by passing a ':' followed by the reqused options, an example of this is `-nl $A:limit=4&position=3&re`
- Available Options: **Position**, **Recursion**, **limit**

## Command Options
The following section contains the way to pass paramaters and rules to the above mentioned commands in order to make a precise and accurate dictionary.

### Position
- Short: &p=
- Long: &position=
- Description: This option determines the postion(s) for any string that will be connotated to a word in the production wordlist.
- Options: 1(Before), 2(After), 3(Before & After)
- Example: `-gd &format=YYR10&position=3`

### Recursion
- Short: &re
- Long: &recursion
- Description: This option only works alongside the position option, by calling this option, the position option will call it self recursivly based on the integer (1-3) passed to the position argument. If 3 is the argument passed to the position option then the position option will call itself 3 times to produce word variations with position formats 1, 2, and 3. If 2 is the argument passed to the position option then the produced variations will be with position formats 1 and 2.
- Example: `-gd &format=YYR10&position=3&recursion`

### Limit
- Short: &l=
- Long: &limit=
- Description: Determines the max length of any string to be connatated to a word in the production wordlist. Accepts an integer argument.
- Example: `-gd &format=YYR10&limit=5`

### Whitelist
- Short: &w=
- Long: &Whitelist=
- Description: Allows the user to specify only certain characters to be used in the scipts operation. Any character not in the whitelist will be excluded.
- Example: `-lm &whitelist=!#%&£$`

### Blacklist
- Short: &b=
- Long: &Blacklist=
- Description: Allows the user to specify certain characters to be excluded from the scripts operation.
- Example: `-lm &blacklist=!#%&£$`







#### Last Updated 27.01.2024
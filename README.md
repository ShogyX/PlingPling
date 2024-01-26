# PlingPling - Python Dictionary Generator

## General

### Introduction
Written in Python, PlingPling is a dictionary generator meant to be used after collecting information about a target. Inteded to produce dictionaries for potential email, username or password enumeration. The script supports various ways of transforming and generating new words from a base wordlist, with a highly customizable options to produce broad and/or precise dictionaries for effective use in enumeration/bruteforcing.

### Important
- Using all/many options with large base lists may take time to finish and produce dictionaries exceeding 100 million words. 
- Number lists are precompiled in .txt files under the NumberLists folder. The CUSTOM.txt file can be used to add custom number lists, use $CUSTOM to refrence it in the commandline.
- Any custom list input should only have 1 word per line.
- Use of multiple lists may result in small amounts of duplication as lists may contain some identicle words/numbers.
- The interactive command line interface allows you to save presets of multiple commands for quick use in the future.
- Commands are not case sensitive but written with caps in the documentation for better readability.
- The sequence of commands affects the final ouput. See the section below for more info.

## Production Order

The order in which commands are enteret into the script will have an impact upon the final dictionary. The way the script processes commands and generate words is sequential.Meaning all new variations are added back to the production list and used by the next script option to generate new words. An example of this is would be using a "base list" with the leet option and reverse word option. The script will use the base list and generate leet verisions of each word, it will then add those words to the production list which already consists of the base list. The reverse words option will use the entire production list which consists of the base words and leet words, and create reversed versions of these words and add it back to the production list. The only exceptions from this are the -wl and -op commands, their execution will always be first and last.


## Output & Input
Commands in this section handle the input of the base wordlist and the output path of the finished dictionary.

### Wordlist
- Short: -wl
- Long: -Wordlist
- Description: Specify the path to an existing wordlist file. PlingPling will use this wordlist as a base and apply other transformations as specified by other options.
- Example: `-wl [Path To Wordlist]`

### OutPath
- Short: -op
- Long: -OutPath
- Description: Specify the output path for the generated dictionary file. If not specified, the default output path is the DefaultOuput folder where the script is stored.
- Example: `-op [Path To Wordlist]`

## Transformative Commands
Commands in this section will generate new transformed versions of words in the base word list.

### LeetMode
- Short: -lm
- Long: -LeetMode
- Description: Enables leet mode PlingPling will generate additional versions of words with leet transformations based on the specified leet rules.
- Example: `-lm [Options]`

### ReverseWords
- Short: -rw
- Long: -ReverseWords
- Description: Enable word reversal. PlingPling will add reversed versions of words to the output dictionary.
- Example: `-rw [Options]`

### WordCapitalization
- Short: -wc
- Long: -WordCapitalization
- Description: Enable word capitalization mode. PlingPling will generate variations of words with different capitalization patterns based on requested patterns.
- Example: `-wc [Options]`

## Connotative Commands
Commands in this section will connotate words, numbers or characters to words in the base list.

### CustomInput
- Short: -ci
- Long: -CustomInput
- Description: Allows you to provide a custom list of words. PlingPling will connotate these words to words in the base list and apply transformations as specified.
- Example: `-ci [Path To Wordlist][Other options]`

### WordPermutation
- Short: -wp
- Long: -WordPermutation
- Description: Enable word permutation mode. PlingPling will generate permutations of words in the base wordlist that a separated by a sepcific delimiter, the default is "_".
- Example: `-wp [Options]`

### GenerateDates
- Short: -gd
- Long: -GenerateDates
- Description: Enable date generation mode. PlingPling will generate dates to be connotated to words in the base list based on specified rules.
- Example: `-gd [Options]`

### SpecialCharacter
- Short: -sc
- Long: -SpecialCharacter
- Description: Enable special character mode. PlingPling will connotate various special characters to the words in the base worlist based on specified rules.
- Example: `-sc [Options]`

### NumberLists
- Short: -nl
- Long: -NumberLists
- Description: Enable number lists mode. PlingPling will append specific number patterns to words in base wordlist based on requested patterns.
- Example: `-nl [Options]`





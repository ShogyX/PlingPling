# PlingPling - Python Dictionary Generator

## General

### Introduction
Written in Python, PlingPling is a dictionary generator meant to be used after collecting information about a target. Inteded to produce dictionaries for potential email, username or password enumeration. The script supports various ways of transforming and generating new words from a base wordlist, with a highly customizable options to produce broad and/or precise dictionaries for effective use in enumeration/bruteforcing.

### Important
- Suppporting many different means of transformation and connotation the user is highly encouraged to only use options deemed likely to help in enumeration/bruteforcing. Words in the dictionary can quickly exceed 100 million with multiple options in use. 
- The user is encouraged to view any precompiled list in order to understand what list is the best fit for their use case.
- Any custom list input should only have 1 word per line.
- Note that use of multiple lists may result in small amounts of duplication as lists may contain some identicle words/numbers.
- Multi option commands may become quite lengthy, the user is encouraged to save queries in the presets folder for easy future use.
- Commands are case insensitive but written with caps in the documentation for better readability.
- The user is highly encouraged to view the diagram outlining the production pipeline of the script in order to better understand how the dictionary is built and how commands interact with eachother. 

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

## Production Pipeline Order
### <img align="Right" width="520" height="862" src="Documentation/Diagram view of production pipeline.png">

- The image presented outlines the priority of commands in the production pipeline of the script.
- As of 26.01.2024 there is no way of changing the order in which commands are prioritized. 
- The order is the sequence in which the script will generate new words. 
- All new variations are added back to the production list and used by the next script option to generate new words.
- An example of this is whould be using a Base list with the leet option and reverse word option. The script will use the base list and generate leet verisions of each word, it will then add those words to the production list which already consists of the base list. The reverse words option will use the entire production list which consists of the base words and leet words, and create reversed versions of these words and add it back to the production list.


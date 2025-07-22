# ================================
# REGULAR EXPRESSIONS IN PYTHON
# ================================

# What is a Regular Expression (Regex)?
# A regular expression is a sequence of characters that forms a search pattern.
# It is used for string searching and manipulation, such as validation, searching, extracting, or replacing text.

# Python provides a built-in module called `re` to work with regex.

import re

# ====================================
# BASIC FUNCTIONS IN re MODULE
# ====================================

# re.match()   --> Checks for a match only at the beginning of the string
# re.search()  --> Searches for a match anywhere in the string
# re.findall() --> Returns all occurrences of the pattern in a list
# re.sub()     --> Replaces one or many matches with a string

# ====================================
# EXAMPLES
# ====================================

# Example 1: Using re.match()
text = "Python is powerful"
match_result = re.match("Python", text)
print(match_result)  # Output: <re.Match object; span=(0, 6), match='Python'>

# Example 2: Using re.search()
search_result = re.search("power", text)
print(search_result)  # Output: <re.Match object; span=(10, 15), match='power'>

# Example 3: Using re.findall()
data = "My phone number is 123-456-7890 and my friend's number is 987-654-3210"
all_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", data)
print(all_numbers)  # Output: ['123-456-7890', '987-654-3210']

# Example 4: Using re.sub()
sentence = "I love cats. Cats are cute."
modified = re.sub(r"cats", "dogs", sentence, flags=re.IGNORECASE)
print(modified)  # Output: I love dogs. dogs are cute.

# ====================================
# COMMON PATTERNS
# ====================================

# .        --> Matches any character except newline
# ^        --> Matches beginning of the string
# $        --> Matches end of the string
# \d       --> Matches any digit (0–9)
# \D       --> Matches any non-digit
# \w       --> Matches any alphanumeric character (a-z, A-Z, 0-9, _)
# \W       --> Matches any non-alphanumeric character
# \s       --> Matches any whitespace (space, tab, newline)
# \S       --> Matches any non-whitespace character
# *        --> 0 or more repetitions
# +        --> 1 or more repetitions
# ?        --> 0 or 1 repetition
# {n}      --> Exactly n repetitions
# {n,}     --> At least n repetitions
# {n,m}    --> Between n and m repetitions

# ====================================
# USE CASES OF REGEX IN PYTHON
# ====================================

# 1. Validate email, phone number, password, etc.
# 2. Data cleaning (removing unwanted characters)
# 3. Tokenizing text
# 4. Log parsing
# 5. Web scraping and data extraction
# 6. Text replacement or substitution

# ====================================
# EXAMPLE: EMAIL VALIDATION
# ====================================
email = "user@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,3}$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# ====================================
# EXAMPLE: EXTRACT HASHTAGS FROM TEXT
# ====================================
tweet = "Learning #Python and #MachineLearning with #OpenAI"
hashtags = re.findall(r"#\w+", tweet)
print(hashtags)  # Output: ['#Python', '#MachineLearning', '#OpenAI']

BOLD = '\033[1m'
RESET = '\033[0m'
ITALIC = '\033[3m'
YELLOW = '\033[33m'
RED = '\033[31m'
BLUE = '\033[34m'
CYAN = '\033[36m'
PURPLE = '\033[35m'

def show_help():
    print(f"{BOLD}Available Commands:{RESET}")
    print(f"{YELLOW}help{RESET}      - Show this help message")
    print(f"{YELLOW}encode{RESET}    - Encode a message")
    print(f"{YELLOW}decode{RESET}    - Decode a message")
    print(f"{YELLOW}ciper:{RESET}    - Out of the list above, enter a number")
    print(f"{YELLOW}bigram{RESET}    - Uses bigrams to detect how likely input text is English")
    print(f"{YELLOW}exit{RESET}      - Exit the program\n")

def bigram_finder(string):
    confidence = 0
    input_bigrams = []
    common_bigrams = ["th", "he", "in", "en", "nt", "re", "er", "an", "ti", "es", "on", "at", "se", "nd", "or", "ar", "al", "te", "co", "de", "to", "ra", "et", "ed", "it", "sa", "em", "ro"]
    no_spaces = string.replace(" ", "")
    string_letters = list(no_spaces)
    string_letters = [c for c in string_letters if c.isalpha() and c.isascii()]
    for i, char in enumerate(string_letters[:-1]):
        current_bigram = char + string_letters[i + 1]
        if current_bigram.isalpha():
            input_bigrams.append(current_bigram.lower())
    confidence = sum(1 for bg in input_bigrams if bg in common_bigrams)
    confidence_value = confidence/len(input_bigrams)
    return confidence_value
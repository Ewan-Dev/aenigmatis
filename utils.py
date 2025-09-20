BOLD = '\033[1m'
RESET = '\033[0m'
ITALIC = '\033[3m'
YELLOW = '\033[33m'

def show_help():
    print(f"{BOLD}Available Commands:{RESET}")
    print(f"{YELLOW}help{RESET}      - Show this help message")
    print(f"{YELLOW}encode{RESET}    - Encode a message")
    print(f"{YELLOW}decode{RESET}    - Decode a message")
    print(f"{YELLOW}exit{RESET}      - Exit the program\n")

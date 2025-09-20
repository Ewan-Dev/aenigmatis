# ANSI escape codes
BOLD = '\033[1m'
RESET = '\033[0m'
ITALIC = '\033[3m'
YELLOW = '\033[33m'

# ASCII art
ascii_art = f"""
 █████╗ ███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗███████╗
██╔══██╗██╔════╝████╗  ██║██║██╔════╝ ████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝
███████║█████╗  ██╔██╗ ██║██║██║  ███╗██╔████╔██║███████║   ██║   ██║███████╗
██╔══██║██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║╚════██║
██║  ██║███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝
"""

print(ascii_art)
print(f"-------------------------------")
print(f"{ITALIC} gen. sing.{RESET}{BOLD} · puzzle{RESET}")
print(f"-------------------------------")
print(f" ")
print(f"{BOLD}Welcome to Aenigmatis{RESET}") 
print(f"{ITALIC}A quick, simple, and powerful tool for enciphering/deciphering.{RESET}")
print(f" ")
print(f"Type {BOLD}'help'{RESET} to see a list of commands.")

def show_help():
    print(f"{BOLD}Available Commands:{RESET}")
    print(f"{YELLOW}help{RESET}      - Show this help message")
    print(f"{YELLOW}encode{RESET}    - Encode a message")
    print(f"{YELLOW}decode{RESET}    - Decode a message")
    print(f"{YELLOW}exit{RESET}      - Exit the program\n")

while True:
    command = input(f">").strip().lower()
    
    if command == 'help':
        show_help()

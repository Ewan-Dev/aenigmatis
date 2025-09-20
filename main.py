from utils import show_help, BOLD, RESET, ITALIC, YELLOW # ANSI codes and help CLI function
from ciphers import caesar_encipher # Import ciphers

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

while True:
    command = input(f"> ").strip().lower()
    
    ciphers = ["caesar"]

    if command == "help":
        show_help()
    elif command == "encode":
        for cipher in ciphers:
            print(f"{YELLOW}{ciphers.index(cipher) + 1}. {cipher}{RESET}")
        command = input(f"cipher: ")
        if command == "1":
            print("\n")
            plaintext = input("Plaintext: ")
            shift = input("Shift: ")
            caesar_ciphertext = caesar_encipher(plaintext, shift)
            print(caesar_ciphertext)
    else:
        print(f"Command {command} not found. ")
        print(f"Type {BOLD}'help'{RESET} to see a list of commands.")

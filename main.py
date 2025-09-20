from utils import show_help, BOLD, RESET, ITALIC # ANSI codes and help CLI function
from ciphers import ceaser_encipher # Import ciphers

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
    
    ciphers = ["ceaser"]

    if command == "help":
        show_help()
    elif command == "encode":
        for cipher in ciphers:
            print(f"{ciphers.index(cipher) + 1}. {cipher}")
        command = input(f"cipher: ")
        if command == "1":
            print("\n")
            plaintext = input("Plaintext: ")
            shift = input("Shift: ")
            ceaser_ciphertext = ceaser_encipher(plaintext, shift)
            print(ceaser_ciphertext)
    else:
        print(f"Command {command} not found. ")
        print(f"Type {BOLD}'help'{RESET} to see a list of commands.")

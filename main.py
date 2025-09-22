from utils import show_help, bigram_finder, trigram_finder, BOLD, RESET, ITALIC, YELLOW, RED, BLUE, CYAN, PURPLE # ANSI codes and help CLI function
from ciphers import caesar_encipher, caesar_decipher, vignere_encipher # Import ciphers

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
    
    ciphers = ["caesar", "vignere"]

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
            command = input(f"cipher: ")
        elif command == "2":
            print("\n")
            plaintext = input("Plaintext: ")
            key = input("Key: ")
            vignere_cipherttext = vignere_encipher(plaintext, key)
            print(vignere_cipherttext)  
    elif command == "decode":
        for cipher in ciphers:
            print(f"{YELLOW}{ciphers.index(cipher) + 1}. {cipher}{RESET}")
        command = input(f"cipher: ")
        if command == "1":
            print("\n")
            ciphertext = input("Ciphertext: ")
            shift = input("Shift: ")
            caesar_plaintext = caesar_decipher(ciphertext, shift)
            print(caesar_plaintext)
        elif command == "2":
            print("\n")
            print(f"{RED}Feature not available yet!{RESET}")
    elif command == "bigram":
            text = input("Paste you text here: ")
            english_score = round(bigram_finder(text), 2)
            colour_message = (CYAN, "LIKELY ENGLISH") if english_score > 0.75 else ((RED, "UNLIKELY ENGLISH") if english_score < 0.25 else (YELLOW, "PROBABLY ENGLISH"))
            colour, message = colour_message
            print(f"English confidence: {colour}{BOLD}{english_score}{RESET} - {message}")
    elif command == "trigram":
            text = input("Paste you text here: ")
            english_score = round(trigram_finder(text), 2)
            colour_message = (CYAN, "LIKELY ENGLISH") if english_score > 0.75 else ((RED, "UNLIKELY ENGLISH") if english_score < 0.25 else (YELLOW, "PROBABLY ENGLISH"))
            colour, message = colour_message
            print(f"English confidence: {colour}{BOLD}{english_score}{RESET} - {message}")
    else:
        print(f"Command {command} not found. ")
        print(f"Type {BOLD}'help'{RESET} to see a list of commands.")

from utils import show_help, bigram_finder, trigram_finder, BOLD, RESET, ITALIC, YELLOW, RED, BLUE, CYAN, PURPLE # ANSI codes and help CLI function
from ciphers import caesar_encipher, caesar_decipher, vignere_encipher, polybius_encipher, polybius_decipher, ADFGVX_encipher, ADFGVX_decipher, morse_encipher # Import ciphers

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
    
    ciphers = ["caesar", "vignere", "polybius", "ADFGVX", "morse"]

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
            print(f"{BOLD}{caesar_ciphertext}{RESET}")
            command = input(f"cipher: ")
        elif command == "2":
            print("\n")
            plaintext = input("Plaintext: ")
            key = input("Key: ")
            vignere_cipherttext = vignere_encipher(plaintext, key)
            print(f"{BOLD}{vignere_cipherttext}{RESET}")
        elif command == "3":
            print("\n")
            plaintext = input("Plaintext: ")
            keyword = input("Keyword: ")
            columns = input("Columns (type 5 for alphabet): ")
            rows = input("Rows (type 5 for alphabet): ")
            alphabet = input("Alphabet (Leave blank for default A-Z ): ")
            alphabet = alphabet if alphabet else "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            polybius_ciphertext = polybius_encipher(plaintext, keyword, columns, rows, alphabet)
            print(f"{BOLD}{polybius_ciphertext}{RESET}")
        elif command == "4":
            print("\n")
            plaintext = input("Plaintext: ")
            trans = input("Transpositional key: ")
            sub = input("Substitution key: ")
            ADFGVX_ciphertext = ADFGVX_encipher(plaintext, sub, trans)
            print(f"{BOLD}{ADFGVX_ciphertext}{RESET}")
        elif command == "5":
            plaintext = input("Plaintext: ")
            morse_encipher = morse_encipher(plaintext)
            print(f"{BOLD}{morse_encipher}{RESET}")
        
    elif command == "decode":
        for cipher in ciphers:
            print(f"{YELLOW}{ciphers.index(cipher) + 1}. {cipher}{RESET}")
        command = input(f"cipher: ")
        if command == "1":
            print("\n")
            ciphertext = input("Ciphertext: ")
            shift = input("Shift: ")
            caesar_plaintext = caesar_decipher(ciphertext, shift)
            print(f"{BOLD}{caesar_plaintext}{RESET}")
        elif command == "2":
            print("\n")
            print(f"{RED}Feature not available yet!{RESET}")
        elif command == "3":
            print("\n")
            ciphertext = input("Ciphertext: ")
            keyword = input("Keyword: ")
            columns = input("Columns (type 5 for alphabet): ")
            rows = input("Rows (type 5 for alphabet): ")
            alphabet = input("Alphabet (Leave blank for default A-Z ): ")
            alphabet = alphabet if alphabet else "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            polybius_ciphertext = polybius_decipher(ciphertext, keyword, columns, rows, alphabet)
            print(f"{BOLD}{polybius_ciphertext}{RESET}")
        elif command == "4":
            print("\n")
            ciphertext = input("Ciphertext: ")
            trans = input("Transpositional key: ")
            sub = input("Substitution key: ")
            ADFGVX_plaintext = ADFGVX_decipher(ciphertext, sub, trans)
            print(f"{BOLD}{ADFGVX_plaintext}{RESET}")
        elif command == "5":
            pass # TODO: next commit
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

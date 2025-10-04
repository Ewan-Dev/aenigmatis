from utils import show_help, bigram_finder, trigram_finder, overall_english_score, read_input, kasiskis_method, remove_non_alphabetic, BOLD, RESET, ITALIC, YELLOW, RED, BLUE, CYAN, PURPLE # ANSI codes and help CLI function
from ciphers import caesar_encipher, caesar_decipher, vignere_encipher,vignere_decipher, polybius_encipher, polybius_decipher, ADFGVX_encipher, ADFGVX_decipher, morse_encipher, morse_decipher, columnar_transposition_encipher, columnar_transposition_decipher, ROT13_encipher, ROT13_decipher, railfence_encipher, railfence_decipher, autokey_encipher, autokey_decipher # Import ciphers

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
    
    ciphers = ["caesar", "vignere", "polybius", "ADFGVX", "morse", "columnar transposition", "ROT13", "railfence (zig-zag)", "autokey"]

    if command == "help":
        show_help()
    elif command == "encode":
        for cipher in ciphers:
            print(f"{YELLOW}{ciphers.index(cipher) + 1}. {cipher}{RESET}")
        command = input(f"cipher: ")
        if command == "1":
            print("\n")
            print("Ciphertext:")
            plaintext = read_input()
            print(plaintext)
            shift = input("Shift: ")
            caesar_ciphertext = caesar_encipher(plaintext, shift)
            print(f"{BOLD}{caesar_ciphertext}{RESET}")
            command = input(f"cipher: ")
        elif command == "2":
            print("\n")
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            key = input("Key: ")
            vignere_cipherttext = vignere_encipher(plaintext, key)
            print(f"{BOLD}{vignere_cipherttext}{RESET}")
        elif command == "3":
            print("\n")
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            keyword = input("Keyword: ")
            columns = input("Columns (type 5 for alphabet): ")
            rows = input("Rows (type 5 for alphabet): ")
            alphabet = input("Alphabet (Leave blank for default A-Z ): ")
            alphabet = alphabet if alphabet else "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            polybius_ciphertext = polybius_encipher(plaintext, keyword, columns, rows, alphabet)
            print(f"{BOLD}{polybius_ciphertext}{RESET}")
        elif command == "4":
            print("\n")
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            trans = input("Transpositional key: ")
            sub = input("Substitution key: ")
            ADFGVX_ciphertext = ADFGVX_encipher(plaintext, sub, trans)
            print(f"{BOLD}{ADFGVX_ciphertext}{RESET}")
        elif command == "5":
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            morse_encipher = morse_encipher(plaintext)
            print(f"{BOLD}{morse_encipher}{RESET}")
        elif command == "6":
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            key = input("Key: ")
            col_trans_ciphertext = columnar_transposition_encipher(plaintext, key)
            print(f"{BOLD}{col_trans_ciphertext}{RESET}")
        elif command == "7":
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            ROT13_ciphertext = ROT13_encipher(plaintext)
            print(f"{BOLD}{ROT13_ciphertext}{RESET}")
        elif command == "8":
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            rows = input("Rows: ")
            offset = input("Offset: ")
            railfence_ciphertext = railfence_encipher(plaintext, int(rows), int(offset))
            print(f"{BOLD}{railfence_ciphertext}{RESET}")
        elif command == "9":
            print("Plaintext: ")
            plaintext = read_input()
            print(plaintext)
            keyword = input("Keyword: ")
            autokey_ciphertext = autokey_encipher(plaintext, keyword)
            print(f"{BOLD}{autokey_ciphertext}{RESET}")
    elif command == "decode":
        for cipher in ciphers:
            print(f"{YELLOW}{ciphers.index(cipher) + 1}. {cipher}{RESET}")
        command = input(f"cipher: ")
        if command == "1":
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            shift = input("Shift: ")
            caesar_plaintext = caesar_decipher(ciphertext, shift)
            print(f"{BOLD}{caesar_plaintext}{RESET}")
        elif command == "2":
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            key = input("Keyword: ")
            vignere_plaintext = vignere_decipher(ciphertext, key)
            print(f"{BOLD}{vignere_plaintext}{RESET}")
        elif command == "3":
            print("\n")
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            keyword = input("Keyword: ")
            columns = input("Columns (type 5 for alphabet): ")
            rows = input("Rows (type 5 for alphabet): ")
            alphabet = input("Alphabet (Leave blank for default A-Z ): ")
            alphabet = alphabet if alphabet else "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            polybius_ciphertext = polybius_decipher(ciphertext, keyword, columns, rows, alphabet)
            print(f"{BOLD}{polybius_ciphertext}{RESET}")
        elif command == "4":
            print("\n")
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            trans = input("Transpositional key: ")
            sub = input("Substitution key: ")
            ADFGVX_plaintext = ADFGVX_decipher(ciphertext, sub, trans)
            print(f"{BOLD}{ADFGVX_plaintext}{RESET}")
        elif command == "5":
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            morse_plaintext = morse_decipher(ciphertext)
            print(f"{BOLD}{morse_plaintext}{RESET}")
        elif command == "6":
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            key = input("Key: ")
            col_trans_plaintext = columnar_transposition_decipher(ciphertext, key)
            print(f"{BOLD}{col_trans_plaintext}{RESET}")
        elif command == "7":
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            ROT13_plaintext = ROT13_decipher(ciphertext)
            print(f"{BOLD}{ROT13_plaintext}{RESET}")
        elif command == "8":
            print("Ciphertext: ")
            ciphertext = read_input()
            print(ciphertext)
            rows = input("Rails: ")
            offset = input("Offset: ")
            railfence_plaintext = railfence_decipher(ciphertext, int(rows), int(offset))
            print(f"{BOLD}{railfence_plaintext}{RESET}")
        elif command == "9":
            print("Plaintext: ")
            ciphertext = read_input()
            print(ciphertext)
            keyword = input("Keyword: ")
            autokey_plaintext = autokey_decipher(ciphertext, keyword)
            print(f"{BOLD}{autokey_plaintext}{RESET}")
    elif command == "bigram":
            print("Paste you text here: ")
            text = read_input()
            print(text)
            english_score = round(bigram_finder(text), 2)
            colour_message = (CYAN, "LIKELY ENGLISH") if english_score > 0.75 else ((RED, "UNLIKELY ENGLISH") if english_score < 0.25 else (YELLOW, "PROBABLY ENGLISH"))
            colour, message = colour_message
            print(f"English confidence: {colour}{BOLD}{english_score}{RESET} - {message}")
    elif command == "trigram":
            print("Paste you text here: ")
            text = read_input()
            print(text)
            english_score = round(trigram_finder(text), 2)
            colour_message = (CYAN, "LIKELY ENGLISH") if english_score > 0.75 else ((RED, "UNLIKELY ENGLISH") if english_score < 0.25 else (YELLOW, "PROBABLY ENGLISH"))
            colour, message = colour_message
            print(f"English confidence: {colour}{BOLD}{english_score}{RESET} - {message}")
    elif command == "overall_eng_score":
            print("Paste you text here: ")
            text = read_input()
            print(text)
            english_score = round(overall_english_score(text), 2)
            colour_message = (CYAN, "LIKELY ENGLISH") if english_score > 0.75 else ((RED, "UNLIKELY ENGLISH") if english_score < 0.25 else (YELLOW, "PROBABLY ENGLISH"))
            colour, message = colour_message
            print(f"English confidence: {colour}{BOLD}{english_score}{RESET} - {message}")
    elif command == "kasiski":
            print("Paste you text here: ")
            text = read_input()
            print(text)
            kasiski_result = kasiskis_method(text, 3)
            print(f"Kasiski results: \n")
            print(f"{BLUE}{ITALIC}Frequency{RESET}    {PURPLE}{BOLD}Length{RESET}")
            print('\n'.join(f"{BLUE}{ITALIC}{freq}{RESET}    {PURPLE}{BOLD}{length}{RESET}" for length, freq in kasiski_result))
    elif command == "non_alpha":
            print("Paste you text here: ")
            text = read_input()
            print(text)
            non_alpha_result = remove_non_alphabetic(text)
            print(f"Non-alphabetic string: {non_alpha_result}")
    elif command == "exit":
            exit()
    else:
        print(f"Command {command} not found. ")
        print(f"Type {BOLD}'help'{RESET} to see a list of commands.")

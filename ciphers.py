import math
from utils import remove_non_alphabetic, mod_inverse, matrix_mod_inverse
from math import gcd
import numpy as np

def caesar_encipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_shift = ord('A') if char.isupper() else ord('a')
            result += chr((((ord(char) - ascii_shift) + int(shift)) % 26) + ascii_shift)
        else:
            result += char
    return result
 
def caesar_decipher(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_shift = ord('A') if char.isupper() else ord('a')
            result += chr((((ord(char) - ascii_shift) - int(shift)) % 26) + ascii_shift)
        else:
            result += char
    return result

def vignere_encipher(text, key):
    result = ""
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65 if str(key[i % len(key)]).isupper() else ord(key[i % len(key)]) - 97
            ascii_shift = ord('A') if char.isupper() else ord('a')
            result += chr((((ord(char) - ascii_shift) + int(shift)) % 26) + ascii_shift)
        else:
            result += char
        i = i + 1
    return result

def vignere_decipher(text, key):
    result = ""
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65 if str(key[i % len(key)]).isupper() else ord(key[i % len(key)]) - 97
            ascii_shift = ord('A') if char.isupper() else ord('a')
            result += chr((((ord(char) - ascii_shift) - int(shift)) % 26) + ascii_shift)
        else:
            result += char
        i = i + 1
    return result


def polybius_encipher(text, keyword, cols, rows, alphabet):
    cols = range(1, int(cols) + 1)
    rows = range(1, int(rows) + 1)
    text = text.upper()
    letters_dict = {}
    alphabet = list(alphabet)
    keyword = keyword.replace("J", "I")
    keyword = keyword.upper()
    key_letters = list(keyword)
    key = ""
    for char in keyword:
        if char in key_letters and char not in key:
            key += char
    for char in alphabet:
        if char not in key_letters:
            key += char
    count = 0
    for row in rows:
        for col in cols:
            current_char = key[count]
            coordinate = str(row) + str(col)
            letters_dict.update({current_char: coordinate})
            count += 1
    result = "".join(letters_dict[char] if char in letters_dict else char for char in text )
    return result


def polybius_decipher(ciphertext, keyword, cols, rows, alphabet):
    cols = range(1, int(cols) + 1)
    rows = range(1, int(rows) + 1)
    ciphertext = ciphertext.replace(" ", "")
    ciphertext = "".join(char for char in ciphertext if char.isdigit())
    ciphertext_list = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    print(ciphertext)
    letters_dict = {}
    alphabet = list(alphabet)
    keyword = keyword.replace("J", "I")
    keyword = keyword.upper()
    key_letters = list(keyword)
    key = ""
    for char in keyword:
        if char in key_letters and char not in key:
            key += char
    for char in alphabet:
        if char not in key_letters:
            key += char
    count = 0
    for row in rows:
        for col in cols:
            current_char = key[count]
            coordinate = str(row) + str(col)
            letters_dict.update({coordinate: current_char})
            count += 1
    result = "".join(letters_dict[str(num)] for num in ciphertext_list)
    return result

def ADFGVX_encipher(text, keyword_sub, keyword_trans):
    cols = range(1, 7)
    rows = range(1, 7)
    text = text.upper()
    text = text.replace(" ", "")
    keyword_sub = keyword_sub.upper().replace(" ", "")
    keyword_trans = keyword_trans.upper().replace(" ", "")
    letters_dict = {}
    ADFGVX_list = list("ADFGVX")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    if  keyword_sub.isalpha():
         keyword_sub =  keyword_sub.upper()
    else: 
        raise TypeError("Key can only contain letters (for now)")

    key_letters = list(keyword_sub)
    key = ""
    for char in keyword_sub:
        if char in key_letters and char not in key:
            key += char
    for char in alphabet:
        if char not in key_letters:
            key += char
    count = 0
    for row in rows:
        for col in cols:
            current_char = key[count]
            coordinate = str(ADFGVX_list[row - 1]) + str(ADFGVX_list[col - 1])
            letters_dict.update({current_char: coordinate})
            count += 1
            
    substituted = "".join(letters_dict[char] if char in letters_dict else char for char in text )

    trans_key = ""
    for char in keyword_trans:
        if char not in trans_key:
            trans_key += char
    columns_num = len(trans_key) 
    columns = [ '' for i in range(columns_num)]

    for i, char in enumerate(substituted):
        columns[ i % columns_num ] += char

    order = sorted(range(columns_num), key=lambda x: trans_key[x] )
    ciphertext = ""
    for n in order:
        ciphertext += columns[n]

    return ciphertext

def ADFGVX_decipher(ciphertext, keyword_sub, keyword_trans):
    cols = range(1, 7)
    rows = range(1, 7)
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace(" ", "")
    keyword_sub = keyword_sub.upper().replace(" ", "")
    keyword_trans = keyword_trans.upper().replace(" ", "")
    letters_dict = {}
    ADFGVX_list = list("ADFGVX")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    if  keyword_sub.isalpha() and keyword_trans.isalpha():
        keyword_sub =  keyword_sub.upper()
        keyword_trans =  keyword_trans.upper()
    else: 
        raise TypeError("Key can only contain letters (for now)")

    trans_key = ""
    for char in keyword_trans:
        if char not in trans_key:
            trans_key += char
    columns_num = len(trans_key) 
    order = sorted(range(len(trans_key)), key=lambda x: trans_key[x] )
    column_min, column_add = divmod(len(ciphertext), columns_num)
    column_lengths = [column_min + 1 if i < column_add else column_min for i in range(columns_num)]
    columns = [''] * columns_num
    pos = 0
    for col_index in order:
        length = column_lengths[col_index]
        columns[col_index] = ciphertext[pos:pos+length]
        pos += length

    substituted = ""
    reconstructed= ""
    for row in range(column_lengths[0]):
        for col in range(columns_num):
            if row < len(columns[col]):
                reconstructed += columns[col][row]
    letters_dict = {}
    ADFGVX_list = list("ADFGVX")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    key_letters = list(keyword_sub)
    key = ""
    for char in keyword_sub:
        if char in key_letters and char not in key:
            key += char
    for char in alphabet:
        if char not in key_letters:
            key += char
    count = 0
    coordinates_dict = {}
    for row in rows:
        for col in cols:
            current_char = key[count]
            coordinate = str(ADFGVX_list[row - 1]) + str(ADFGVX_list[col - 1])
            coordinates_dict.update({coordinate: current_char})
            count += 1
            
    substituted = "".join(coordinates_dict[reconstructed[i:i+2]] for i in range(0, len(reconstructed), 2) )
    return substituted

def morse_encipher(ciphertext):
    morse_code = {
    # Letters
    'A': ".-",    'B': "-...",  'C': "-.-.",  'D': "-..",
    'E': ".",     'F': "..-.",  'G': "--.",   'H': "....",
    'I': "..",    'J': ".---",  'K': "-.-",   'L': ".-..",
    'M': "--",    'N': "-.",    'O': "---",   'P': ".--.",
    'Q': "--.-",  'R': ".-.",   'S': "...",   'T': "-",
    'U': "..-",   'V': "...-",  'W': ".--",   'X': "-..-",
    'Y': "-.--",  'Z': "--..",

    # Numbers
    '0': "-----", '1': ".----", '2': "..---", '3': "...--",
    '4': "....-", '5': ".....", '6': "-....", '7': "--...",
    '8': "---..", '9': "----.",

    # Common symbols
    '.': ".-.-.-",   ',': "--..--",   '?': "..--..",  "'": ".----.",
    '!': "-.-.--",   '/': "-..-.",    '(': "-.--.",   ')': "-.--.-",
    '&': ".-...",    ':': "---...",   ';': "-.-.-.",  '=': "-...-",
    '+': ".-.-.",    '-': "-....-",   '_': "..--.-",  '"': ".-..-.",
    '$': "...-..-",  '@': ".--.-.",   ' ': '/'        
}

    ciphertext = ciphertext.replace("’", "'")
    plaintext = ""
    for char in ciphertext.upper():
        if char in morse_code:
            plaintext += (morse_code[char] + ' ')
        else:
            plaintext += '?'
    
    return plaintext


def morse_decipher(ciphertext):
    morse_code = {
    # Letters
    'A': ".-",    'B': "-...",  'C': "-.-.",  'D': "-..",
    'E': ".",     'F': "..-.",  'G': "--.",   'H': "....",
    'I': "..",    'J': ".---",  'K': "-.-",   'L': ".-..",
    'M': "--",    'N': "-.",    'O': "---",   'P': ".--.",
    'Q': "--.-",  'R': ".-.",   'S': "...",   'T': "-",
    'U': "..-",   'V': "...-",  'W': ".--",   'X': "-..-",
    'Y': "-.--",  'Z': "--..",

    # Numbers
    '0': "-----", '1': ".----", '2': "..---", '3': "...--",
    '4': "....-", '5': ".....", '6': "-....", '7': "--...",
    '8': "---..", '9': "----.",

    # Common symbols
    '.': ".-.-.-",   ',': "--..--",   '?': "..--..",  "'": ".----.",
    '!': "-.-.--",   '/': "-..-.",    '(': "-.--.",   ')': "-.--.-",
    '&': ".-...",    ':': "---...",   ';': "-.-.-.",  '=': "-...-",
    '+': ".-.-.",    '-': "-....-",   '_': "..--.-",  '"': ".-..-.",
    '$': "...-..-",  '@': ".--.-.",   ' ': '/'        
}
    morse_code_decipher = {morse: char for char, morse in morse_code.items()}
    ciphertext_list = ciphertext.split(" ")
    plaintext = ""
    for morse in ciphertext_list:
        if morse in morse_code_decipher:
            plaintext += morse_code_decipher[morse]
        else:
            plaintext += '?'
    
    return plaintext

def columnar_transposition_encipher(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    key = key.upper().replace(" ", "")
    trans_key = ""
    for char in key:
        if char not in trans_key:
            trans_key += char

    columns_num = len(trans_key) 
    columns = [ '' for i in range(columns_num)]

    for i, char in enumerate(plaintext):
        columns[ i % columns_num ] += char

    order = sorted(range(columns_num), key=lambda x: trans_key[x] )
    ciphertext = ""
    for n in order:
        ciphertext += columns[n]
    return ciphertext


def columnar_transposition_decipher(ciphertext, key, type):
    if type == 1:
        ciphertext = ciphertext.upper().replace(" ", "")
        key = key.upper().replace(" ", "")
        
        trans_key = ""
        for char in key:
            if char not in trans_key:
                trans_key += char
        print(trans_key)
        columns_num = len(trans_key) 

        order = sorted(range(len(trans_key)), key=lambda x: trans_key[x] )
        
        column_min, column_add = divmod(len(ciphertext), columns_num)
        column_lengths = [column_min + 1 if i <  column_add else column_min for i in range(columns_num)]
        columns = [''] * columns_num 
        
        pos = 0
        for col_index in order:
            length = column_lengths[col_index]
            columns[col_index] = ciphertext[pos:pos+length]
            pos += length
        
        plaintext = ""
        for row in range(column_lengths[0]):
            for col in range(columns_num):
                if row < len(columns[col]):
                    plaintext += columns[col][row]
        
        return plaintext
    
    if type == 2:
        ciphertext = ciphertext.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

        trans_key = ""
        for char in key:
            if char not in trans_key:
                trans_key += char
        print(trans_key)
        columns_num = len(trans_key) 
        rows_num = math.ceil(len(ciphertext) / columns_num)
        order = sorted(range(len(trans_key)), key=lambda x: trans_key[x] )

        full_cols = len(ciphertext) % columns_num
        if full_cols == 0:
            full_cols = columns_num

        grid = [[''] * columns_num for i in range(rows_num)]
        pos = 0
        for row in range(rows_num):
            for col in range(columns_num):
                if pos < len(ciphertext):
                    grid[row][col] = ciphertext[pos]
                    pos += 1

        original_grid = [[''] * columns_num for x in range(rows_num)]
        pos = 0

        for i in order:
            col_height = rows_num if (order.index(i) < full_cols) else rows_num - 1
            for row in range(col_height):
                if pos < len(ciphertext):
                    original_grid[row][i] = grid[row][order.index(i)]
                    pos += 1

        plaintext = ""
        for row in range(rows_num):
            for col in range(columns_num):
                if original_grid[row][col]:
                    plaintext += original_grid[row][col]
        
        return plaintext

def ROT13_encipher(text):
    ciphertext = caesar_encipher(text, 13)
    return ciphertext

def ROT13_decipher(text):
    plaintext = caesar_decipher(text, 13)
    return plaintext

def railfence_encipher(text, rails, offset):
    rail_lists = ["" for _ in range(rails)]
    current_rail = offset
    direction = 1

    if current_rail == rails - 1:
        direction = -1

    else:
        direction = 1

    for i, char in enumerate(text):
        rail_lists[current_rail] += char
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction


    ciphertext = ''.join(rail_lists)
    return ciphertext


def railfence_decipher(text, rails, offset):
    pattern = []
    current_rail = offset
    direction = 1

    if current_rail == rails - 1:
        direction = -1
    else:
        direction = 1

    for i in range(len(text)):
        pattern.append(current_rail)
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction

    rail_lengths = [pattern.count(r) for r in range(rails)]
    rail_list = []
    rail_index = 0
    for count in rail_lengths:
        rail_list.append(list(text[rail_index:rail_index+count]))
        rail_index += count
    
    plainntext = ""
    rail_positions = [0] * rails
    current_rail = offset
    direction = 1

    if current_rail == rails - 1:
        direction = -1
    else:
        direction = 1

    for i in range(len(text)):
        plainntext += rail_list[current_rail][rail_positions[current_rail]]
        rail_positions[current_rail] += 1

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction

    return plainntext

def autokey_encipher(text, keyword):
    result = ""
    key = remove_non_alphabetic(keyword + text)
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65 if str(key[i % len(key)]).isupper() else ord(key[i % len(key)]) - 97
            ascii_shift = ord('A') if char.isupper() else ord('a')
            result += chr((((ord(char) - ascii_shift) + int(shift)) % 26) + ascii_shift)
            i = i + 1
        else:
            result += char
    return result

def autokey_decipher(text, keyword):
    result = ""
    key = keyword
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65 if str(key[i % len(key)]).isupper() else ord(key[i % len(key)]) - 97
            ascii_shift = ord('A') if char.isupper() else ord('a')
            plain_char = chr((((ord(char) - ascii_shift) - int(shift)) % 26) + ascii_shift)
            key += plain_char
            result += plain_char
            i += 1
        else:
            result += char
    return result

def hill_encipher(plaintext, key, size):
    key_nums = []
    plaintext = remove_non_alphabetic(plaintext)
    if len(key) == size ** 2:
        for char in key:
            if char.isalpha():
                key_nums.append(ord(char.upper()) - ord('A'))
    else:
        raise ValueError("Key is invalid: key must be equal to size squared!")
    key = np.array(key_nums).reshape(-1, size)
    print("Key: ", key)
    determinant = round(np.linalg.det(key))
    if gcd(determinant, 26) == 1:
        plaintext_nums = []
        plaintext = ''.join(char.upper() for char in plaintext if char.isalpha())
        if len(plaintext) % size != 0:
                plaintext += 'X' * (size - (len(plaintext) % size))
        for char in plaintext:
            if char.isalpha():
                plaintext_nums.append(ord(char.upper()) - ord('A'))
        matrix = np.array(plaintext_nums).reshape(-1, size).T
        cipher_matrix = (key @ matrix) % 26
        ciphertext = ''.join(chr(int(num) + ord('A')) for num in cipher_matrix.flatten('F'))
        ciphertext_spaces = ""
        ciphertexgit_list = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
        ciphertext_spaces = ' '.join(ciphertext_list)
        return ciphertext_spaces
    else:
        raise ValueError("Key is invalid: determinant of key matrix is not coprime with 26")
    

def hill_decipher(ciphertext, key, size):
    key_nums = [] 
    ciphertext = remove_non_alphabetic(ciphertext)
    if len(key) == size ** 2:
        for char in key:
            if char.isalpha():
                key_nums.append(ord(char.upper()) - ord('A'))
    else:
        raise ValueError("Key is invalid: key must be equal to size squared!")
    key = np.array(key_nums).reshape(-1, size).T
    print("Key: ", key)
    determinant = round(np.linalg.det(key))
    determinant_inverse = mod_inverse(determinant, 26)
    if gcd(determinant, 26) == 1:
        ciphertext_nums = []
        ciphertext = ''.join(char.upper() for char in ciphertext if char.isalpha())
        if len(ciphertext) % size != 0:
                ciphertext += 'X' * (size - (len(ciphertext) % size))
        for char in ciphertext:
            if char.isalpha():
                ciphertext_nums.append(ord(char.upper()) - ord('A'))
        inverse_key = matrix_mod_inverse(key, 26)
        plaintext = ''
        for i in range(0, len(ciphertext_nums), size):
            chunk = np.array(ciphertext_nums[i:i+size])
            decrypted_chunk = (inverse_key @ (chunk)) % 26
            plaintext += ''.join(chr(int(num) + ord('A')) for num in decrypted_chunk)
            plaintext_list = [plaintext[i:i+5] for i in range(0, len(plaintext), 5)]
            plaintext_spaces = ' '.join(plaintext_list)
        return plaintext_spaces
    else:
        raise ValueError("Key is invalid: determinant of key matrix is not coprime with 26")
    
def six_needle_wheatstone_telegraph_encode(plaintext, needule_number):
    dict = {}
    wheatstone_telegraph_5needle = {
        'A': '/|||\\',
        'B': '/||\\|',
        'D': '|/||\\',
        'E': '/|\\||',
        'F': '|/|\\|',
        'G': '||/|\\',
        'H': '/\\|||',
        'I': '|/\\||',
        'K': '||/\\|',
        'L': '|||/\\',
        'M': '\\/|||',
        'N': '|\\/||',
        'O': '||\\/|',
        'P': '|||\\/',
        'R': '\\|/||',
        'S': '|\\|/|',
        'T': '||\\|/',
        'U': '\\||/|',
        'W': '|\\||/',
        'Y': '\\|||/',
        ' ': '|||||'
    }
    if needule_number == 5:
        dict = wheatstone_telegraph_5needle

    ciphertext = ""
    for char in plaintext.upper():

        if char in dict:
            ciphertext += dict[char] + " "
        else:
            ciphertext += char + ' '
    
    return ciphertext


def six_needle_wheatstone_telegraph_decode(ciphertext, needle_number):
    dict = {}
    wheatstone_telegraph_5needle = {
        'A': '/|||\\',
        'B': '/||\\|',
        'D': '|/||\\',
        'E': '/|\\||',
        'F': '|/|\\|',
        'G': '||/|\\',
        'H': '/\\|||',
        'I': '|/\\||',
        'K': '||/\\|',
        'L': '|||/\\',
        'M': '\\/|||',
        'N': '|\\/||',
        'O': '||\\/|',
        'P': '|||\\/',
        'R': '\\|/||',
        'S': '|\\|/|',
        'T': '||\\|/',
        'U': '\\||/|',
        'W': '|\\||/',
        'Y': '\\|||/',
        ' ': '|||||'
    }
    if needle_number == 5:
        dict = wheatstone_telegraph_5needle
    wheatstone_telegraph_decipher = {morse: char for char, morse in wheatstone_telegraph_5needle.items()}
    plaintext = ""
    ciphertext = ciphertext.split(" ")
    for letter in ciphertext:

        if letter in wheatstone_telegraph_decipher:
            plaintext += wheatstone_telegraph_decipher[letter]
        else:
            plaintext += letter
    
    return plaintext

#TODO: Debug solitaire cipher
# def solitaire_encipher(plaintext, cardstream, splitting_char):
    plaintext = plaintext.replace(" ", "")
    cardstream = cardstream.replace("A", "53")
    cardstream = cardstream.replace("B", "54")
    cleaned_plaintext = ""
    for char in plaintext:
        if char.isalpha():
            cleaned_plaintext += char
    whole_keystream = ""
    i = 0
    deck = [int(x) for x in cardstream.split(splitting_char)]
    while i < len(cleaned_plaintext):
        joker_a_index = deck.index(53)
        joker_b_index = deck.index(54)
        if joker_a_index == len(deck) - 1:
            deck.insert(1, deck.pop(joker_a_index))
        else:
            deck.insert(joker_a_index + 1, deck.pop(joker_a_index))
        
        if joker_b_index == len(deck) - 1:
            deck.insert(2, deck.pop(joker_b_index))
        elif  joker_b_index == len(deck) - 2:
            deck.insert(1, deck.pop(joker_b_index))
        else:
            deck.insert(joker_b_index + 2, deck.pop(joker_b_index))

        first_joker = min(deck.index(53), deck.index(54))
        second_joker = max(deck.index(53), deck.index(54))
        deck_first_section = deck[:first_joker]
        deck_second_section = deck[first_joker:second_joker + 1]
        deck_third_section = deck[second_joker + 1:]
        print(str(deck_third_section) + "2nd," + str(deck_second_section) + "3rd," + str(deck_first_section))
        deck = deck_third_section + deck_second_section + deck_first_section
        bottom_card_value = ""
        if deck[-1] == 54:
            bottom_card_value = 53
        else:
            bottom_card_value = int(deck[-1])
        top_cut = deck[:bottom_card_value]
        del deck[:bottom_card_value]
        for card in top_cut:
            deck.insert(-2, card)
        
        top_card = int(deck[0])
        print(top_card)
        keystream = deck[top_card]
        if keystream != 53 and keystream != 54:
            whole_keystream += str((keystream % 26) - 1) + ' '
            i += 1 
    ciphertext = ""
    print(whole_keystream)
    for char, keystream in zip(cleaned_plaintext, whole_keystream.split(' ')):
        #  print(ord(char.upper()) - ord('A') + 1)
        ciphertext += chr((((ord(char.upper()) - ord('A') )+ int(keystream))) + ord('A') )
    return ciphertext
#print(solitaire_encipher("DO NOT USE PC", """5, 12, 7, 3, 49, 23, 2, 18, 34, 8, 21, 1, 42, 5, 11, 53, 27, 36, 50, 6, 30, 9, 14, 45, 17, 26, 19, 13, 38, 4, 24, 29, 10, 35, 31, 46, 16, 39, 25, 41, 32, 54, 20, 22, 44, 15, 48, 28, 33, 40, 47, 37, 51, 52, 43""", ", "))
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

def columnar_transposition_decipher(ciphertext, key):
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

print(railfence_decipher("el olhlowrd", 2, 1))
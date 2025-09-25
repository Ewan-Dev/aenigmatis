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

    keyword_trans_len = len(keyword_trans)
    columns = [ '' for i in range(keyword_trans_len)]

    for i, char in enumerate(substituted):
        columns[ i % keyword_trans_len ] += char
    cleaned_trans_keyword = ""
    for char in keyword_trans:
        if char in keyword_trans and char not in cleaned_trans_keyword:
            cleaned_trans_keyword  += char
    cleaned_trans_keyword = list(cleaned_trans_keyword)
    order = sorted(range(len(keyword_trans)), key=lambda x: keyword_trans[x] )
    ciphertext = ""
    for n in order:
        ciphertext += columns[n]

    print(columns)
    return ciphertext
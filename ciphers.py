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

def caesar_encipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_shift = ord('A') if char.isupper() else ord('a')
            result += chr((((ord(char) - ascii_shift) + int(shift)) % 26) + ascii_shift)
        else:
            result += char
    return result
 
# aenigmatis  
A deciphering, enciphering and cryptanalysis CLI tool.

---

## Installation  
- Run `git clone https://github.com/Ewan-Dev/aenigmatis`  
- Or download the executable file from [Releases](https://github.com/Ewan-Dev/aenigmatis/releases) and run it  
- Or download the Python files from [Releases](https://github.com/Ewan-Dev/aenigmatis/releases)

---

## Usage  
1. Run `python main.py` to get started  
2. Run `help` for a list of commands  
3. To encode/encipher, type `encode` or `decode` for deciphering — then you will see a list of numbered ciphers.  
4. Type the number of the cipher you want.  
   - Example: if you see `1. Caesar`, type `1` then press **Enter**.  
5.  
   - **Windows:** Notepad should open — paste the plaintext or ciphertext in, save it, then close it.  
   - **Linux/Mac:** The nano editor will appear — paste your text in, then to close and save do this:  
     - Press `Ctrl + X`  
     - Type `y`  
     - Press **Enter**  
6. Follow the remaining prompts (it may ask for dimensions, keyword, etc.)  
7. Your plaintext or ciphertext will be printed!  
8. To use tools such as cryptanalysis and other useful commands, use:  
   - `kasiski` — Enter Vigenère ciphertext (in nano/Notepad) → outputs predicted keyword length  
   - `bigram` — Enter text → outputs English score based on bigram frequency  
   - `trigram` — Enter text → outputs English score based on trigram frequency  
   - `non_alpha` — Enter text → removes all non-alphabetic characters and outputs cleaned text  
   - `overall_eng_score` — Enter text → outputs English score using dynamic weighting of bigram and trigram analysis  
   - `exit` — Exits the program  

---

## Available Tools  

### Encoding/Decoding  
- Caesar cipher  
- Vigenère cipher  
- Polybius square cipher  
- ADFGVX cipher  
- Morse code  
- Columnar transposition  
- ROT13  
- Rail fence (zig-zag)  
- Autokey/Autoclave  
- Hill
- Cooke-Wheatson telegraph

### Text Analysis  
- Bigram frequency analysis  
- Trigram frequency analysis  
- Overall English (trigram + bigram with dynamic weighting)  
- Remove all non-alphabetic characters from a string  

### Cryptanalysis  
- Kasiski's method  

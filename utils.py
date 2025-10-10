import numpy as np

BOLD = '\033[1m'
RESET = '\033[0m'
ITALIC = '\033[3m'
YELLOW = '\033[33m'
RED = '\033[31m'
BLUE = '\033[34m'
CYAN = '\033[36m'
PURPLE = '\033[35m'

def show_help():
    print(f"{BOLD}Available Commands:{RESET}")
    print(f"{YELLOW}help{RESET}            - Show this help message")
    print(f"{YELLOW}encode{RESET}            - Encode a message")
    print(f"{YELLOW}decode{RESET}            - Decode a message")
    print(f"{YELLOW}ciper:{RESET}            - Out of the list above, enter a number")
    print(f"{YELLOW}bigram{RESET}            - Uses bigrams to detect how likely input text is English")
    print(f"{YELLOW}trigram{RESET}           - Uses trigrams to detect how likely input text is English")
    print(f"{YELLOW}kasiski{RESET}           - Uses Kasiski's method to determine vignere cipher keyword length")
    print(f"{YELLOW}non_alpha{RESET}         - Removes non-alphabetic characters from a string, including spaces")
    print(f"{YELLOW}overall_eng_score{RESET} - Combines trigram and bigram with dynamic weighting for overalal score")
    print(f"{YELLOW}exit{RESET}              - Exit the program\n")

def bigram_finder(string):
    confidence = 0
    input_bigrams = []
    common_bigrams = ["th", "he", "in", "en", "nt", "re", "er", "an", "ti", "es", "on", "at", "se", "nd", "or", "ar", "al", "te", "co", "de", "to", "ra", "et", "ed", "it", "sa", "em", "ro"]
    no_spaces = string.replace(" ", "")
    string_letters = list(no_spaces)
    string_letters = [c for c in string_letters if c.isalpha() and c.isascii()]
    for i, char in enumerate(string_letters[:-1]):
        current_bigram = char + string_letters[i + 1]
        if current_bigram.isalpha():
            input_bigrams.append(current_bigram.lower())
    confidence = sum(1 for bg in input_bigrams if bg in common_bigrams)
    confidence_value = confidence/len(input_bigrams)
    return confidence_value

def trigram_finder(string):
    confidence = 0
    input_trigrams = []
    # Top 500 English character trigrams (list only)
    common_trigrams = [
        'the',
        'and',
        'ing',
        'ent',
        'ion',
        'her',
        'for',
        'tha',
        'nth',
        'int',
        'ere',
        'tio',
        'ter',
        'est',
        'ers',
        'ati',
        'hat',
        'ate',
        'all',
        'eth',
        'hes',
        'ver',
        'his',
        'oft',
        'ith',
        'fth',
        'sth',
        'oth',
        'res',
        'ont',
        'dth',
        'are',
        'rea',
        'ear',
        'was',
        'sin',
        'sto',
        'tth',
        'sta',
        'thi',
        'tin',
        'ted',
        'ons',
        'edt',
        'wit',
        'san',
        'din',
        'ort',
        'con',
        'rth',
        'eve',
        'eco',
        'era',
        'ist',
        'ngt',
        'ast',
        'ill',
        'com',
        'ore',
        'ive',
        'nce',
        'one',
        'edi',
        'pro',
        'ess',
        'out',
        'ein',
        'att',
        'men',
        'hec',
        'esa',
        'hen',
        'ina',
        'eri',
        'ert',
        'ame',
        'iti',
        'ome',
        'son',
        'art',
        'man',
        'ean',
        'ona',
        'eof',
        'tor',
        'hea',
        'ran',
        'rin',
        'ine',
        'eda',
        'nto',
        'ave',
        'nin',
        'ove',
        'oun',
        'ain',
        'ant',
        'str',
        'eto',
        'hem',
        'sof',
        'per',
        'nde',
        'ste',
        'nte',
        'eas',
        'dto',
        'our',
        'red',
        'rom',
        'tof',
        'ght',
        'tot',
        'ese',
        'cha',
        'ica',
        'hei',
        'hin',
        'ide',
        'ndt',
        'han',
        'tan',
        'lin',
        'not',
        'der',
        'ect',
        'tra',
        'igh',
        'fro',
        'eat',
        'sti',
        'hep',
        'ndi',
        'ins',
        'she',
        'nal',
        'pla',
        'als',
        'een',
        'nti',
        'you',
        'lan',
        'und',
        'nda',
        'rat',
        'lea',
        'can',
        'has',
        'nds',
        'nga',
        'hel',
        'hed',
        'inc',
        'use',
        'esi',
        'gth',
        'asa',
        'het',
        'nts',
        'hav',
        'hew',
        'tho',
        'but',
        'nan',
        'ass',
        'hef',
        'ies',
        'ret',
        'end',
        'par',
        'wer',
        'cti',
        'ren',
        'rec',
        'cal',
        'its',
        'ree',
        'ene',
        'rst',
        'eal',
        'ana',
        'nst',
        'cou',
        'tur',
        'min',
        'ity',
        'yth',
        'hey',
        'eca',
        'oul',
        'lle',
        'ard',
        'rou',
        'anc',
        'ost',
        'pre',
        'age',
        'efo',
        'les',
        'ssi',
        'ema',
        'eso',
        'tat',
        'ath',
        'wor',
        'ust',
        'heb',
        'ewa',
        'sho',
        'ind',
        'sed',
        'hou',
        'lly',
        'uld',
        'ase',
        'ure',
        'ono',
        'ele',
        'enc',
        'nat',
        'ead',
        'whe',
        'ell',
        'ble',
        'kin',
        'ans',
        'tic',
        'ali',
        'sco',
        'ero',
        'whi',
        'ces',
        'own',
        'nta',
        'act',
        'ber',
        'ven',
        'tim',
        'don',
        'dan',
        'ose',
        'ice',
        'isa',
        'ton',
        'den',
        'ngs',
        'ugh',
        'nes',
        'lat',
        'tal',
        'edo',
        'ten',
        'ime',
        'eme',
        'ack',
        'tes',
        'ple',
        'ous',
        'off',
        'tto',
        'chi',
        'ani',
        'orm',
        'ned',
        'ens',
        'sha',
        'mor',
        'iss',
        'ite',
        'nge',
        'tis',
        'ora',
        'lli',
        'ede',
        'sse',
        'ade',
        'rie',
        'aid',
        'emo',
        'ral',
        'sit',
        'oin',
        'hth',
        'tre',
        'any',
        'ake',
        'ern',
        'mer',
        'ric',
        'dis',
        'ish',
        'oug',
        'ini',
        'ong',
        'ntr',
        'eli',
        'wil',
        'led',
        'sar',
        'how',
        'edb',
        'ich',
        'spe',
        'sea',
        'lit',
        'yin',
        'sai',
        'ndo',
        'gin',
        'shi',
        'ord',
        'mon',
        'ena',
        'new',
        'por',
        'ser',
        'ial',
        'ori',
        'tte',
        'mar',
        'epr',
        'ach',
        'har',
        'yea',
        'tri',
        'che',
        'tea',
        'unt',
        'omp',
        'who',
        'tar',
        'owe',
        'rit',
        'ded',
        'ors',
        'day',
        'hee',
        'thr',
        'eir',
        'ond',
        'mes',
        'efi',
        'had',
        'ner',
        'ela',
        'let',
        'lso',
        'ris',
        'ire',
        'isi',
        'met',
        'ars',
        'hic',
        'cen',
        'ari',
        'fin',
        'tob',
        'nsi',
        'las',
        'ope',
        'lar',
        'des',
        'fte',
        'nit',
        'sen',
        'ang',
        'som',
        'abo',
        'sio',
        'two',
        'ian',
        'eis',
        'tsa',
        'ngi',
        'uni',
        'ses',
        'rep',
        'rac',
        'top',
        'abl',
        'eti',
        'ebe',
        'eha',
        'now',
        'oni',
        'ves',
        'fir',
        'erc',
        'ofa',
        'ace',
        'sal',
        'get',
        'app',
        'ane',
        'rsa',
        'nof',
        'heh',
        'gre',
        'win',
        'car',
        'ete',
        'mat',
        'cho',
        'lay',
        'swe',
        'esp',
        'pri',
        'tiv',
        'rof',
        'gra',
        'llo',
        'cor',
        'eac',
        'nis',
        'dit',
        'gan',
        'gto',
        'eno',
        'bou',
        'obe',
        'esh',
        'tos',
        'ery',
        'rma',
        'ngo',
        'ewi',
        'ara',
        'rto',
        'rel',
        'oma',
        'ala',
        'asi',
        'tst',
        'utt',
        'irs',
        'yan',
        'lla',
        'sfo',
        'ork',
        'ett',
        'lth',
        'sid',
        'aso',
        'swi',
        'ita',
        'set',
        'twa',
        'erm',
        'epa',
        'ron',
        'tit',
        'aft',
        'dre',
        'tle',
        'mil',
        'dby',
        'ale',
        'pen',
        'bec',
        'mbe',
        'toa',
        'heg',
        'sch',
        'sis',
        'rti',
        'heo',
        'low',
        'lis',
        'oll',
        'war',
        'alt',
        'elo',
        'tro',
        'cat',
        'med',
        'lic',
        'hil',
        'ile',
        'tht',
        'rem',
        'rre',
        'ays',
        'oli',
        'rso',
        'nsa',
        'omm',
        'old',
        'cre',
        'ata',
        'ise',
        'cia',
        'pos',
        'ger',
        'sma',
        'uti',
        'sts',
        'sec',
        'sbe',
        'eni',
        'sre']
    no_spaces = string.replace(" ", "")
    string_letters = list(no_spaces)
    string_letters = [c for c in string_letters if c.isalpha() and c.isascii()]
    for i, char in enumerate(string_letters[:-2]):
        current_trigram = char + string_letters[i + 1] + string_letters[i + 2]
        if current_trigram.isalpha(): 
            input_trigrams.append(current_trigram.lower())
    confidence = sum(1 for tg in input_trigrams if tg in common_trigrams)
    confidence_value = confidence/len(input_trigrams)
    return confidence_value

def combine_ngrams(bigram_score, trigram_score):
    weight = 1 / (1 + trigram_score)
    score = ((bigram_score * weight) + (trigram_score * (1 - weight)))
    return score

def overall_english_score(string):
    bigram_score = bigram_finder(string)
    trigram_score = trigram_finder(string)
    overall_score = combine_ngrams(bigram_score, trigram_score)
    return overall_score

def read_input():
    import platform
    import subprocess
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".txt", delete=False) as file:
        path = file.name
    
    try:
        if platform.system() == "Windows":
            subprocess.run(["notepad.exe", path])
        else: 
            subprocess.run(["nano", path])

        with open(path, "r") as file:
            content = file.read()
        content = content[:-1] if content.endswith('\n') else content
        return content

    finally: 
        try:
            os.unlink(path)
        except:
            pass

def kasiskis_method(ciphertext, sequence_len):
    text = ciphertext.upper().replace(" ", "")
    groups = []
    for i in range(len(text) - sequence_len + 1):
        group = text[i:i + sequence_len]
        groups.append((group, i))

    sequences = {}
    for seq, pos in groups:
        if seq not in sequences:
            sequences[seq] = []
        sequences[seq].append(pos)

    repeated_sequences = {}
    for seq, pos in sequences.items():
        if len(pos) > 1:
            repeated_sequences[seq] = pos

    sequence_distances = []
    for seq, pos in repeated_sequences.items():
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                distance = pos[j] - pos[i]
                sequence_distances.append(distance)

    factors = []
    for distance in sequence_distances:
        for i in range(2, distance + 1):
            if distance % i == 0:
                factors.append(i)
    
    factors_count = {}
    for factor in factors:
        if factor in factors_count:
            factors_count[factor] += 1
        else:
            factors_count[factor] = 1
    
    factors_sorted = sorted(factors_count.items(), key=lambda x : x[1], reverse=True )
    
    return factors_sorted

def remove_non_alphabetic(text):
    non_alphabetic = ""
    for char in text:
        if char.isalpha():
            non_alphabetic += char
    return non_alphabetic

def mod_inverse(num, modulo):
    for x in range(1, modulo):
        if (num * x) % modulo == 1:
            return x
        
def matrix_mod_inverse(matrix, modulo):
    determinant = int(round(np.linalg.det(matrix)))
    determinant_inverse = mod_inverse(determinant, modulo)
    cofactor_matrix = np.linalg.inv(matrix).T * np.linalg.det(matrix)
    matrix_adjugate = np.round(cofactor_matrix).astype(int) % modulo
    return (determinant_inverse * matrix_adjugate) % modulo

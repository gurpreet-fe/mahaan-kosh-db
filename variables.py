# Gurmukhi to Latin
GURMUKHI_LATIN_ALPHABET = {
    'ੳ': 'A', 'ਅ': 'd', 'ੲ': 'D', 'ਸ': 'm', 'ਹ': 'u',
    'ਕ': 'k', 'ਖ': 'K', 'ਗ': 'i', 'ਘ': 'I', 'ਙ': 'ù',
    'ਚ': 'W', 'ਛ': 'Q', 'ਜ': 'p', 'ਝ': 'P', 'ਞ': 'ø',
    'ਟ': 'R', 'ਠ': 'T', 'ਡ': 'G', 'ਢ': 'F', 'ਣ': 'C',
    'ਤ': 'l', 'ਥ': 'L', 'ਦ': 'o', 'ਧ': 'O', 'ਨ': 'v',
    'ਪ': 'h', 'ਫ': 'H', 'ਬ': 'y', 'ਭ': 'Y', 'ਮ': 'c',
    'ਯ': 'U', 'ਰ': 'j', 'ਲ': 'n', 'ਵ': 'b', 'ੜ': 'V'
}

# LATIN_GURMUKHI_DIACRITICS = {
#     'e': 'ਾ', # 'e': '0x0A3E',
#     'f': 'ਿ', 'r': 'ੀ', # 'f': '0x0A3F', 'r': '0x0A40',
#     'g': 'ੁ', 't': 'ੂ', # 'g': '0x0A41', 't': '0x042',
#     's': 'ੇ', 'w': 'ੈ', # 's': '0x0A47', 'w': '0x0A48',
#     'a': 'ੋ', 'q': 'ੌ', # 'a': '0x0A4B', 'q': '0x0A4C',
#     'N': 'ਂ', 'x': 'ੰ', 'z': 'ੱ', # 'N': '0x0A02', 'x': '0x0A70', 'z': '0x0A71'
# }

# LATIN_GURMUKHI_SUBSCRIPTS = {
#     'J': '੍ਰ', 'Í': '੍ਵ', 'B': '੍ਹ',
# }

# LATIN_GURMUKHI_NUMERALS = {
#   "0": "੦",
#   "1": "੧",
#   "2": "੨",
#   "3": "੩",
#   "4": "੪",
#   "5": "੫",
#   "6": "੬",
#   "7": "੭",
#   "8": "੮",
#   "9": "੯",
# }

# LATIN_GURMUKHI_BINDI = {
#   "M": "ਸ਼",
#   "Å": "ਖ਼",
#   "Æ": "ਗ਼",
#   "Z": "ਜ਼",
#   "Ä": "ਫ਼",
# }

# Latin to Gurmukhi
LATIN_GURMUKHI_ALPHABET = {
    'A': 'ੳ', 'd': 'ਅ', 'D': 'ੲ', 'm': 'ਸ', 'u': 'ਹ',
    'k': 'ਕ', 'K': 'ਖ', 'i': 'ਗ', 'I': 'ਘ', 'ù': 'ਙ',
    'W': 'ਚ', 'Q': 'ਛ', 'p': 'ਜ', 'P': 'ਝ', 'ø': 'ਞ',
    'R': 'ਟ', 'T': 'ਠ', 'G': 'ਡ', 'F': 'ਢ', 'C': 'ਣ',
    'l': 'ਤ', 'L': 'ਥ', 'o': 'ਦ', 'O': 'ਧ', 'v': 'ਨ',
    'h': 'ਪ', 'H': 'ਫ', 'y': 'ਬ', 'Y': 'ਭ', 'c': 'ਮ',
    'U': 'ਯ', 'j': 'ਰ', 'n': 'ਲ', 'b': 'ਵ', 'V': 'ੜ',
}

LATIN_GURMUKHI_DIACRITICS = {
    'e': 'ਾ',  # '0x0A3E'
    'f': 'ਿ', 'r': 'ੀ',  # '0x0A3F', '0x0A40'
    'g': 'ੁ', 't': 'ੂ',  # '0x0A41', '0x042'
    's': 'ੇ', 'w': 'ੈ',  # '0x0A47', '0x0A48'
    'a': 'ੋ', 'q': 'ੌ',  # '0x0A4B', '0x0A4C'
    'N': 'ਂ', 'x': 'ੰ', 'z': 'ੱ',  # '0x0A02', '0x0A70', '0x0A71'
}

LATIN_GURMUKHI_SUBSCRIPTS = {
    'J': '੍ਰ',
    'Í': '੍ਵ',
    'B': '੍ਹ',
}

LATIN_GURMUKHI_NUMERALS = {
    "0": "੦",
    "1": "੧",
    "2": "੨",
    "3": "੩",
    "4": "੪",
    "5": "੫",
    "6": "੬",
    "7": "੭",
    "8": "੮",
    "9": "੯",
}

LATIN_GURMUKHI_BINDI = {
    "M": "ਸ਼",
    "Å": "ਖ਼",
    "Æ": "ਗ਼",
    "Z": "ਜ਼",
    "Ä": "ਫ਼",
}

SPECIAL_CHARS = ['(', '-', ' ', '\n', ',', ';', ')', '.', '“', '”',]
# MISSING_CHARS = ['å', 'ë', 'ö', 'û', 'Ç', 'ê', 'é', '´', 'œ', 'Ñ', 'ú', 'ˆ', 'ç', 'æ', 'X', 'E', 'Â', 'È', 'Á', '†', 'Ê', 'Ô', 'S', 'Ì', 'ì', 'í', 'Ú', 'Ã', 'ü', '>', 'µ',]
MISSING_CHARS = ['å', 'é', 'ú', 'E', 'È', 'Ê', 'Ì', 'ì', 'í', 'Ã', '>', 'µ',]
MISSING_DIACRITICS = ['ë', 'ö', 'û', 'Ç', 'ê', '´', 'œ', 'Ñ', 'ˆ', 'ç', 'æ', 'X', 'Â', 'Á', '†', 'Ô', 'S', 'Ú', 'ü',]

LATIN_GURMUKHI = {}
LATIN_GURMUKHI.update(LATIN_GURMUKHI_ALPHABET)
LATIN_GURMUKHI.update(LATIN_GURMUKHI_DIACRITICS)
LATIN_GURMUKHI.update(LATIN_GURMUKHI_SUBSCRIPTS)
LATIN_GURMUKHI.update(LATIN_GURMUKHI_NUMERALS)
LATIN_GURMUKHI.update(LATIN_GURMUKHI_BINDI)
LATIN_GURMUKHI.update(dict.fromkeys(SPECIAL_CHARS, None))
LATIN_GURMUKHI.update(dict.fromkeys(MISSING_CHARS, None))
LATIN_GURMUKHI.update(dict.fromkeys(MISSING_DIACRITICS, None))

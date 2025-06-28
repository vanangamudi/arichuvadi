import re
from .arichuvadi import ARICHUVADI
from .arichuvadi import get_letters_coding

from pprint import pprint

def generate_tace16_map(start=0xE000):
    mapping = {}
    code = start
    for letter in ARICHUVADI:
        mapping[letter] = chr(code)
        code += 1
    return mapping


TACE16_MAP = generate_tace16_map()
REVERSE_MAP = {v: k for k, v in TACE16_MAP.items()}

import unicodedata

# Tamil Unicode ranges
TAMIL_START = 0x0B80
TAMIL_END = 0x0BFF
COMBINING_MARKS = set(range(0x0BBE, 0x0BCD + 1))  # Vowel signs, virama, etc.

def is_tamil(ch):
    return TAMIL_START <= ord(ch) <= TAMIL_END

def is_combining_mark(ch):
    return ord(ch) in COMBINING_MARKS

def split_graphemes(text):
    return get_letters_coding(text)

class TACE16String:
    def __init__(self, text):
        self.original = text
        self.graphemes = split_graphemes(text)
        self.internal = ''.join(TACE16_MAP.get(g, g) for g in self.graphemes)

    def __str__(self):
        return ''.join(REVERSE_MAP.get(ch, ch) for ch in self.internal)

    def __repr__(self):
        return f"TACE16String({str(self)!r})"

    def __len__(self):
        return len(self.internal)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return TACE16String.from_internal(self.internal[idx])
        else:
            return REVERSE_MAP.get(self.internal[idx], self.internal[idx])

    def __eq__(self, other):
        if isinstance(other, TACE16String):
            return self.internal == other.internal
        elif isinstance(other, str):
            return str(self) == other
        return False

    def encode(self):
        return self.internal

    def decode(self):
        return str(self)

    @classmethod
    def from_internal(cls, internal_str):
        unicode_str = ''.join(REVERSE_MAP.get(ch, ch) for ch in internal_str)
        return cls(unicode_str)

    def replace(self, old, new):
        internal_old = TACE16_MAP.get(old, old)
        internal_new = TACE16_MAP.get(new, new)
        new_internal = self.internal.replace(internal_old, internal_new)
        return TACE16String.from_internal(new_internal)

    def find(self, sub):
        internal_sub = TACE16_MAP.get(sub, sub)
        return self.internal.find(internal_sub)

    def count(self, sub):
        internal_sub = TACE16_MAP.get(sub, sub)
        return self.internal.count(internal_sub)

    def startswith(self, sub):
        internal_sub = TACE16_MAP.get(sub, sub)
        return self.internal.startswith(internal_sub)

    def endswith(self, sub):
        internal_sub = TACE16_MAP.get(sub, sub)
        return self.internal.endswith(internal_sub)

    def search(self, pattern):
        return re.search(TACE16String(pattern).internal, self.internal)

    def match(self, pattern):
        return re.match(TACE16String(pattern).internal, self.internal)

    def findall(self, pattern):
        return re.findall(TACE16String(pattern).internal, self.internal)

if __name__ == "__main__":
    s = TACE16String("காகி hello")
    print(str(s))           # காகி hello
    print(s.encode())       # Internal PUA string
    print(s[0])             # கா
    print(s[1:3])           # TACE16String('கி hello')
    print(s.find("கி"))     # Position of "கி"
    print(s.replace("கி", "கூ"))  # Replaces கி → கூ

    words = [
        "கடி",
        "கழி",
        "கலி",
        "கலை",
        "கா",
        "கோடு",
        "குல்",
        "சேர்",
        "சரி",
        "கை",
        "கரை",
        "சாய்",
        "குல்",
        "குழை",
        "குறை",
        "சிலை",
        "குறி",
        "குரு",
        "சிறை",
        "குடி",
        "குடை",
        "சிதை",
        "சேர்",
        "சுலை",
    ]

    pattern = r'^[சிகு]'
    re_matches = []
    tacere_matches = []
    for word in words:
        s = TACE16String(word)
        if re.search(pattern, word):
            re_matches.append(word)
        if s.search(pattern):
            tacere_matches.append(word)


    print('re_matches :=')
    pprint(re_matches)

    print('tacere_matches :=')
    pprint(tacere_matches)
